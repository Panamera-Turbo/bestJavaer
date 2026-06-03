#!/usr/bin/env python3
"""Generate English mirrors for ai-articles without overwriting Chinese originals."""

from __future__ import annotations

import hashlib
import json
import re
import shutil
from pathlib import Path
from urllib.parse import unquote

import argostranslate.translate


ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = ROOT / "ai-articles"
TARGET_ROOT = ROOT / "en" / "ai-articles"

CATEGORY_META = {
    "01-agent-and-coding": {
        "title": "AI Agent & Coding Tools",
        "description": "Codex, Claude Code, Claw, Agent workflows, AI coding tools, and real usage notes.",
    },
    "02-models-and-research": {
        "title": "Models, Research & Prompt",
        "description": "Model capabilities, papers and reports, prompt methods, evaluations, and LLM observations.",
    },
    "03-tools-and-resources": {
        "title": "Tools, Resources & Workbench",
        "description": "AI websites, resource lists, knowledge management, publishing workbenches, and personal tools.",
    },
    "04-industry-and-business": {
        "title": "Industry, Companies & Business",
        "description": "Company updates, platform changes, commercialization, infrastructure, security incidents, and industry judgment.",
    },
    "05-ai-creation-and-media": {
        "title": "AI Creation & Media",
        "description": "Images, video, 3D, creative generation, and AI content experiments.",
    },
    "06-notes-and-observations": {
        "title": "Notes, Essays & Incidents",
        "description": "Personal observations, essays, pitfalls, incidents, and cross-topic records.",
    },
}

SELECTED_TITLE_OVERRIDES = {
    "Codex 官方：goal 的正确打开方式": "The Official Codex Guide: How to Use /goal Correctly",
    "Codex 把我家网给优化了，我 TM 直接原地起飞了。": "Codex Optimized My Home Network, and the Result Was Absurdly Good",
    "Agent Workflow Kit 接入你的项目": "Connecting Agent Workflow Kit to Your Project",
    "我终于把 Codex 的用量扒出来了，原来最贵的不是输出": "I Finally Figured Out Codex Usage: Output Is Not the Most Expensive Part",
    "Layweout 公众号排版工作台": "Layweout: a WeChat Article Formatting Workbench",
    "如何把 Codex 用到极致": "How to Get the Most Out of Codex",
    "离谱，OpenAI 把我的开源赞助账号封了": "OpenAI Blocked My Open-Source Sponsorship Account",
    "Deepseek 会泄露其他玩家的对话": "DeepSeek Can Leak Other Players' Conversations",
    "给大家详细介绍下 weread skills": "A Detailed Introduction to weread skills",
}

PROTECT_PATTERNS = [
    re.compile(r"!\[[^\]]*]\([^)]+\)"),
    re.compile(r"\[[^\]]+]\([^)]+\)"),
    re.compile(r"`[^`]+`"),
    re.compile(r"https?://[^\s)]+"),
    re.compile(r"<[^>]+>"),
]


def translate_text(text: str) -> str:
    if not text.strip():
        return text
    if not re.search(r"[\u4e00-\u9fff]", text):
        return text
    return argostranslate.translate.translate(text, "zh", "en").strip()


def translate_protected(text: str) -> str:
    spans: list[tuple[int, int]] = []
    for pattern in PROTECT_PATTERNS:
        spans.extend(match.span() for match in pattern.finditer(text))
    if not spans:
        return translate_text(text)

    spans.sort()
    merged: list[tuple[int, int]] = []
    for start, end in spans:
        if not merged or start > merged[-1][1]:
            merged.append((start, end))
        else:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))

    pieces: list[str] = []
    cursor = 0
    for start, end in merged:
        pieces.append(translate_text(text[cursor:start]))
        pieces.append(text[start:end])
        cursor = end
    pieces.append(translate_text(text[cursor:]))
    return "".join(pieces)


def title_from_markdown(path: Path) -> str:
    for line in path.read_text(encoding="utf-8").splitlines():
        match = re.match(r"^#\s+(.+?)\s*$", line)
        if match:
            return match.group(1).strip()
    return path.stem


def english_title(title: str) -> str:
    title = title.replace("/goal", "goal")
    if title in SELECTED_TITLE_OVERRIDES:
        return SELECTED_TITLE_OVERRIDES[title]
    translated = translate_text(title)
    translated = translated.replace("Codex official: goal", "The Official Codex Guide: /goal")
    return translated[:1].upper() + translated[1:] if translated else title


def slugify(title: str, used: set[str], source_path: Path) -> str:
    slug = title.lower()
    slug = slug.replace("&", " and ")
    slug = re.sub(r"[^a-z0-9]+", "-", slug).strip("-")
    slug = re.sub(r"-+", "-", slug)
    if not slug:
        slug = "article-" + hashlib.sha1(str(source_path).encode("utf-8")).hexdigest()[:8]
    base = slug[:82].strip("-") or slug
    slug = base
    counter = 2
    while slug in used:
        slug = f"{base}-{counter}"
        counter += 1
    used.add(slug)
    return slug + ".md"


def translate_markdown(source: str, title_en: str, chinese_href: str, english_href: str) -> str:
    lines = source.splitlines()
    out: list[str] = []
    block: list[str] = []
    in_fence = False
    inserted_switch = False
    skipped_first_h1 = False

    def flush_block() -> None:
        if not block:
            return
        text = "\n".join(block)
        block.clear()
        if re.search(r"(`[^`]+`|\[[^\]]+]\([^)]+\)|https?://)", text):
            out.extend(translate_line(line) for line in text.splitlines())
        else:
            translated = translate_text(text)
            out.extend(translated.splitlines() if translated else text.splitlines())

    for line in lines:
        if line.startswith("```") or line.startswith("~~~"):
            flush_block()
            in_fence = not in_fence
            out.append(line)
            continue
        if in_fence:
            out.append(line)
            continue

        if not skipped_first_h1 and re.match(r"^#\s+", line):
            flush_block()
            out.append("# " + title_en)
            out.append("")
            out.append(f"[English]({english_href}) | [中文原文]({chinese_href})")
            out.append("")
            out.append("> English translation of the Chinese original. This version is generated for international readers and may be refined over time.")
            out.append("")
            skipped_first_h1 = True
            inserted_switch = True
            continue

        if not line.strip():
            flush_block()
            out.append(line)
            continue

        if line.lstrip().startswith("![") or re.match(r"^\s*(-{3,}|\*{3,}|_{3,})\s*$", line):
            flush_block()
            out.append(line)
            continue

        if re.match(r"^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?\s*$", line):
            flush_block()
            out.append(line)
            continue

        if "|" in line and re.search(r"[\u4e00-\u9fff]", line):
            flush_block()
            out.append(translate_line(line))
            continue

        block.append(line)

    flush_block()

    if not inserted_switch:
        out.insert(0, f"# {title_en}")
        out.insert(1, "")
        out.insert(2, f"[English]({english_href}) | [中文原文]({chinese_href})")
        out.insert(3, "")
        out.insert(4, "> English translation of the Chinese original. This version is generated for international readers and may be refined over time.")
        out.insert(5, "")

    return "\n".join(out).rstrip() + "\n"


def translate_line(line: str) -> str:
    if not line.strip():
        return line
    if re.match(r"^\s*(-{3,}|\*{3,}|_{3,})\s*$", line):
        return line
    if line.lstrip().startswith("!["):
        return line
    if re.match(r"^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?\s*$", line):
        return line
    if "|" in line and re.search(r"[\u4e00-\u9fff]", line):
        parts = line.split("|")
        return "|".join(translate_protected(part) for part in parts)

    heading = re.match(r"^(\s*#{1,6}\s+)(.+)$", line)
    if heading:
        return heading.group(1) + translate_protected(heading.group(2))

    quote = re.match(r"^(\s*>\s?)(.+)$", line)
    if quote:
        content = quote.group(2)
        if content.startswith("日期："):
            return quote.group(1) + content.replace("日期：", "Date: ", 1)
        return quote.group(1) + translate_protected(content)

    bullet = re.match(r"^(\s*(?:[-*+]|\d+[.)])\s+)(.+)$", line)
    if bullet:
        return bullet.group(1) + translate_protected(bullet.group(2))

    return translate_protected(line)


def parse_index_items(readme_path: Path) -> list[tuple[str, str, str]]:
    items: list[tuple[str, str, str]] = []
    pattern = re.compile(r"^\s*-\s*(\d{4}-\d{2}-\d{2})\s*-\s*\[([^\]]+)]\(([^)]+)\)")
    for line in readme_path.read_text(encoding="utf-8").splitlines():
        match = pattern.match(line)
        if match:
            items.append((match.group(1), match.group(2), match.group(3)))
    return items


def main() -> None:
    if TARGET_ROOT.exists():
        shutil.rmtree(TARGET_ROOT)
    TARGET_ROOT.mkdir(parents=True, exist_ok=True)

    used_slugs_by_category: dict[str, set[str]] = {}
    article_map: dict[str, dict[str, str]] = {}

    for category_dir in sorted(path for path in SOURCE_ROOT.iterdir() if path.is_dir()):
        category = category_dir.name
        if category not in CATEGORY_META:
            continue
        used = used_slugs_by_category.setdefault(category, set())
        (TARGET_ROOT / category).mkdir(parents=True, exist_ok=True)

        for source_path in sorted(category_dir.glob("*.md")):
            if source_path.name == "README.md":
                continue
            relative_source = source_path.relative_to(ROOT).as_posix()
            title_zh = title_from_markdown(source_path)
            title_en = english_title(title_zh)
            file_name = slugify(title_en, used, source_path)
            target_path = TARGET_ROOT / category / file_name
            english_rel = target_path.relative_to(ROOT).as_posix()
            chinese_href = "../../../" + relative_source
            english_href = "./" + file_name
            target_path.write_text(
                translate_markdown(
                    source_path.read_text(encoding="utf-8"),
                    title_en,
                    chinese_href,
                    english_href,
                ),
                encoding="utf-8",
            )
            article_map[relative_source] = {
                "category": category,
                "english_path": english_rel,
                "english_title": title_en,
                "source_title": title_zh,
            }

    write_indexes(article_map)
    update_english_readme_links(article_map)

    map_path = TARGET_ROOT / "translation-map.json"
    map_path.write_text(json.dumps(article_map, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Generated {sum(1 for value in article_map.values())} English article files under {TARGET_ROOT.relative_to(ROOT)}")


def write_indexes(article_map: dict[str, dict[str, str]]) -> None:
    lines = [
        "# AI Articles",
        "",
        "English mirror of the Chinese AI article collection. The Chinese originals remain available in the main `ai-articles` directory.",
        "",
        "| Category | Description |",
        "| --- | --- |",
    ]

    for category, meta in CATEGORY_META.items():
        lines.append(f"| [{meta['title']}](./{category}/README.md) | {meta['description']} |")

    lines.extend(["", "## All Articles", ""])

    for category, meta in CATEGORY_META.items():
        lines.extend([f"### {meta['title']}", ""])
        write_category_index(category, meta, article_map)
        source_items = parse_index_items(SOURCE_ROOT / category / "README.md")
        for date, _title, href in source_items:
            source_path = (SOURCE_ROOT / category / unquote(href.split("?")[0].split("#")[0].replace("./", ""))).resolve()
            source_rel = source_path.relative_to(ROOT).as_posix()
            mapped = article_map.get(source_rel)
            if not mapped:
                continue
            article_href = "./" + str(Path(mapped["english_path"]).relative_to("en/ai-articles")).replace("\\", "/")
            lines.append(f"- {date} - [{mapped['english_title']}]({article_href})")
        lines.append("")

    (TARGET_ROOT / "README.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def write_category_index(category: str, meta: dict[str, str], article_map: dict[str, dict[str, str]]) -> None:
    lines = [
        f"# {meta['title']}",
        "",
        meta["description"],
        "",
    ]
    source_items = parse_index_items(SOURCE_ROOT / category / "README.md")
    for date, _title, href in source_items:
        source_path = (SOURCE_ROOT / category / unquote(href.split("?")[0].split("#")[0].replace("./", ""))).resolve()
        source_rel = source_path.relative_to(ROOT).as_posix()
        mapped = article_map.get(source_rel)
        if not mapped:
            continue
        file_name = Path(mapped["english_path"]).name
        lines.append(f"- {date} - [{mapped['english_title']}](./{file_name})")

    lines.extend(["", '<p class="branch-back"><a href="#/en/ai-articles/README">Back</a></p>', ""])
    (TARGET_ROOT / category / "README.md").write_text("\n".join(lines), encoding="utf-8")


def update_english_readme_links(article_map: dict[str, dict[str, str]]) -> None:
    readme_path = ROOT / "README.md"
    text = readme_path.read_text(encoding="utf-8")
    text = text.replace("./ai-articles/README.md", "./en/ai-articles/README.md")
    for source_rel, mapped in article_map.items():
        encoded_path = encode_markdown_link(source_rel)
        target = "./" + mapped["english_path"]
        text = text.replace("./" + encoded_path, target)
        text = text.replace(source_rel, mapped["english_path"])
    readme_path.write_text(text, encoding="utf-8")


def encode_markdown_link(path: str) -> str:
    from urllib.parse import quote

    return "/".join(quote(part) for part in path.split("/"))


if __name__ == "__main__":
    main()
