#!/usr/bin/env python3
"""Clean residual Chinese text from generated English Markdown mirrors."""

from __future__ import annotations

import functools
import re
from pathlib import Path

import argostranslate.translate


ROOT = Path(__file__).resolve().parents[1]
TARGET_ROOT = ROOT / "en"
HAN_RE = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]")
PROTECT_RE = re.compile(
    r"(!?\[[^\]]*]\([^)]+\)|`[^`]+`|https?://[^\s)\]，。；、,]+|<[^>]+>)"
)
MARKDOWN_LINK_RE = re.compile(r"(!?)\[([^\]]*[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff][^\]]*)]\(([^)]*)\)")
HTML_ALT_RE = re.compile(r'(alt=["\'])([^"\']*[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff][^"\']*)(["\'])')
STRING_RE = re.compile(r"([\"'`])([^\"'`]*[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff][^\"'`]*)(\1)")

DIRECT_REPLACEMENTS = {
    "中文原文": "Chinese Original",
    "图像": "image",
    "截图": "screenshot",
    "点击快速配置": "click Quick Setup",
    "课程首屏": "course hero screen",
    "课程大纲": "course outline",
    "用户名": "username",
    "久": "long time",
    "三体": "The Three-Body Problem",
    "你好呀！👋 我是 Clawra，有什么我可以帮你的吗？💃": "Hi! I am Clawra. How can I help you?",
    "请求太频繁了，请1分钟后再试": "Requests are too frequent. Please try again in one minute.",
    "几千行重复": "thousands of repeated lines",
    "响应回来了": "The response came back",
    "暂停执行目标": "pause the goal",
    "暂停恢复目标": "resume the goal",
    "清除执行目标": "clear the goal",
    "发送给 OpenClaw: 用户": "Sending to OpenClaw: user ",
    "条消息": " messages",
    "已经有": "already has ",
    "这篇文章一经发布引起了巨大的影响": "this post had a huge impact as soon as it was published",
    "我最近也是把这篇内容详读": "I recently read it closely",
    "并结合我自己的亲身经历来发表我自己的看法": "and I am sharing my view based on my own experience",
    "它的定位能说明": "its positioning explains ",
    "舶": "ship",
    "香": "fragrance",
    "量子位": "QbitAI",
    "智源社区": "BAAI Community",
    "中国人工智能学会": "Chinese Association for Artificial Intelligence",
    "新智元": "AI Era",
    "原文": "original article",
    "项目接入规约": "project onboarding rules",
    "腾讯云": "Tencent Cloud",
    "知乎专栏": "Zhihu Column",
    "前沿快讯": "Frontier News",
    "吐槽": "Complaints",
    "华道数据股份有限公司": "China Data Group",
    "网易": "NetEase",
}

PUNCT_REPLACEMENTS = {
    "，": ", ",
    "。": ".",
    "；": "; ",
    "：": ": ",
    "、": ", ",
    "“": '"',
    "”": '"',
    "‘": "'",
    "’": "'",
    "（": "(",
    "）": ")",
    "【": "[",
    "】": "]",
    "《": '"',
    "》": '"',
    "！": "!",
    "？": "?",
    "—": "-",
    "「": '"',
    "」": '"',
}


@functools.lru_cache(maxsize=8192)
def translate_fragment(text: str) -> str:
    if not HAN_RE.search(text):
        return normalize_punctuation(text)

    replaced = text
    for old, new in DIRECT_REPLACEMENTS.items():
        replaced = replaced.replace(old, new)
    if not HAN_RE.search(replaced):
        return normalize_punctuation(replaced)

    leading = re.match(r"^\s*", replaced).group(0)
    trailing = re.search(r"\s*$", replaced).group(0)
    core = replaced[len(leading) : len(replaced) - len(trailing)]
    if not core:
        return replaced

    translated = argostranslate.translate.translate(core, "zh", "en").strip()
    return leading + normalize_punctuation(translated) + trailing


def normalize_punctuation(text: str) -> str:
    for old, new in PUNCT_REPLACEMENTS.items():
        text = text.replace(old, new)
    text = re.sub(r" {2,}", " ", text)
    text = re.sub(r"\s+([,.;:!?])", r"\1", text)
    return text


def repair_broken_urls(text: str) -> str:
    previous = None
    while previous != text:
        previous = text
        text = re.sub(r"(https?://[^\s)\]]+?)\. (?=[A-Za-z0-9_-])", r"\1.", text)
        text = re.sub(r"(https?://[^\s)\]]+?)\? (?=[A-Za-z0-9_-])", r"\1?", text)
        text = re.sub(r"(https?://[^\s)\]]+?)& (?=[A-Za-z0-9_-])", r"\1&", text)
        text = re.sub(r"(https?://[^\s)\]]+?)= (?=[A-Za-z0-9_-])", r"\1=", text)
        text = re.sub(r"(https?://[^\s)\]]+?)# (?=[A-Za-z0-9_-])", r"\1#", text)
    return text


def repair_href_spacing(href: str) -> str:
    previous = None
    while previous != href:
        previous = href
        href = re.sub(r"\. (?=[A-Za-z0-9_%/-])", ".", href)
        href = re.sub(r"\? (?=[A-Za-z0-9_%/-])", "?", href)
        href = re.sub(r"& (?=[A-Za-z0-9_%/-])", "&", href)
        href = re.sub(r"= (?=[A-Za-z0-9_%/-])", "=", href)
        href = re.sub(r"# (?=[A-Za-z0-9_%/-])", "#", href)
    return href


def repair_markdown_hrefs(text: str) -> str:
    def replace(match: re.Match[str]) -> str:
        return "](" + repair_href_spacing(match.group(1)) + ")"

    return re.sub(r"]\(([^)]*)\)", replace, text)


def repair_path_spacing(text: str) -> str:
    text = text.replace("~/. ", "~/.")
    text = text.replace("/. ", "/.")
    text = text.replace("$HOME/. ", "$HOME/.")
    text = text.replace("~/.zhsrc", "~/.zshrc")
    for extension in (
        "asar",
        "codex",
        "config",
        "git",
        "hermes",
        "json",
        "jsonl",
        "js",
        "md",
        "openclaw",
        "py",
        "service",
        "toml",
        "ts",
        "yaml",
        "yml",
        "zshrc",
    ):
        text = re.sub(rf"\. {extension}\b", f".{extension}", text)
    return text


def translate_link_text(line: str) -> str:
    def replace(match: re.Match[str]) -> str:
        bang, text, href = match.groups()
        return f"{bang}[{translate_fragment(text)}]({href})"

    return MARKDOWN_LINK_RE.sub(replace, line)


def translate_html_alt(line: str) -> str:
    def replace(match: re.Match[str]) -> str:
        return match.group(1) + translate_fragment(match.group(2)) + match.group(3)

    return HTML_ALT_RE.sub(replace, line)


def translate_mixed_text(line: str) -> str:
    line = repair_markdown_hrefs(repair_path_spacing(repair_broken_urls(line)))
    if not HAN_RE.search(line):
        return normalize_punctuation(line)

    line = translate_link_text(line)
    line = translate_html_alt(line)
    parts = PROTECT_RE.split(line)
    for index, part in enumerate(parts):
        if index % 2 == 0 and HAN_RE.search(part):
            parts[index] = translate_fragment(part)
        else:
            parts[index] = normalize_protected(part)
    return normalize_punctuation("".join(parts))


def normalize_protected(text: str) -> str:
    if text.startswith("http://") or text.startswith("https://"):
        return repair_broken_urls(text)
    if text.startswith("[") or text.startswith("!["):
        return text
    if text.startswith("<") and not HAN_RE.search(text):
        return text

    def replace(match: re.Match[str]) -> str:
        content = match.group(0)
        for old, new in DIRECT_REPLACEMENTS.items():
            content = content.replace(old, new)
        return normalize_punctuation(content)

    return re.sub(r"`[^`]+`|<[^>]+>", replace, text)


def clean_code_line(line: str) -> str:
    line = repair_markdown_hrefs(repair_path_spacing(repair_broken_urls(line)))
    if not HAN_RE.search(line):
        return normalize_punctuation(line)

    def replace_string(match: re.Match[str]) -> str:
        return match.group(1) + translate_fragment(match.group(2)) + match.group(3)

    line = STRING_RE.sub(replace_string, line)

    comment_match = re.search(r"(^\s*(?://|#)\s*)(.*)$", line)
    if comment_match and HAN_RE.search(comment_match.group(2)):
        return comment_match.group(1) + translate_fragment(comment_match.group(2))

    trailing_comment = re.search(r"(\s(?://|#)\s*)(.*)$", line)
    if trailing_comment and HAN_RE.search(trailing_comment.group(2)):
        start = trailing_comment.start(2)
        line = line[:start] + translate_fragment(line[start:])

    if HAN_RE.search(line):
        line = translate_mixed_text(line)
    return normalize_punctuation(line)


def clean_markdown(text: str) -> str:
    out: list[str] = []
    in_fence = False

    for line in text.splitlines():
        if re.match(r"^(```|~~~)", line):
            in_fence = not in_fence
            out.append(line)
            continue
        out.append(clean_code_line(line) if in_fence else translate_mixed_text(line))

    return "\n".join(out).rstrip() + "\n"


def main() -> None:
    changed = 0
    for path in sorted(TARGET_ROOT.rglob("*.md")):
        before = path.read_text(encoding="utf-8")
        after = clean_markdown(before)
        if after != before:
            path.write_text(after, encoding="utf-8")
            changed += 1
    print(f"cleaned {changed} English Markdown files")


if __name__ == "__main__":
    main()
