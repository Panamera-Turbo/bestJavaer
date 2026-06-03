#!/usr/bin/env python3
"""Generate English mirrors for non-legacy main docs."""

from __future__ import annotations

import json
import re
from pathlib import Path

import importlib.util


ROOT = Path(__file__).resolve().parents[1]
ARTICLE_MAP_PATH = ROOT / "en" / "ai-articles" / "translation-map.json"

spec = importlib.util.spec_from_file_location("article_gen", ROOT / "scripts" / "generate_english_articles.py")
article_gen = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(article_gen)


DOCS = [
    ("ai-resources/README.md", "en/ai-resources/README.md"),
    ("works/README.md", "en/works/README.md"),
    ("development-guidelines/README.md", "en/development-guidelines/README.md"),
    (
        "development-guidelines/openspec-superpowers-gstack-project-onboarding.md",
        "en/development-guidelines/openspec-superpowers-gstack-project-onboarding.md",
    ),
]

TITLE_OVERRIDES = {
    "# AI 资源": "# AI Resources",
    "# 我的作品 & 开源项目": "# Works & Open Source",
    "# Development Guidelines": "# Development Guidelines",
}


def translate_doc(source: str, target_path: Path, article_map: dict[str, dict[str, str]]) -> str:
    lines = source.splitlines()
    out: list[str] = []
    in_fence = False
    fence_lang = ""
    fence_lines: list[str] = []

    def flush_fence() -> None:
        nonlocal fence_lines
        if fence_lang in {"", "prompt", "text", "txt", "markdown", "md"} and any(re.search(r"[\u4e00-\u9fff]", line) for line in fence_lines):
            translated = article_gen.translate_text("\n".join(fence_lines))
            out.extend(translated.splitlines())
        else:
            out.extend(fence_lines)
        fence_lines = []

    for line in lines:
        fence_match = re.match(r"^(```|~~~)\s*([A-Za-z0-9_-]*)", line)
        if fence_match:
            if in_fence:
                flush_fence()
                out.append(line)
                in_fence = False
                fence_lang = ""
            else:
                out.append(line)
                in_fence = True
                fence_lang = fence_match.group(2).lower()
            continue

        if in_fence:
            fence_lines.append(line)
            continue

        if line in TITLE_OVERRIDES:
            out.append(TITLE_OVERRIDES[line])
        else:
            out.append(article_gen.translate_line(line))

    if in_fence:
        flush_fence()

    text = "\n".join(out).rstrip() + "\n"
    return fix_links(text, target_path, article_map)


def fix_links(text: str, target_path: Path, article_map: dict[str, dict[str, str]]) -> str:
    target_dir = target_path.parent

    replacements = {
        "../README.md": rel_link(target_dir, ROOT / "README.md"),
        "./openspec-superpowers-gstack-project-onboarding.md": "./openspec-superpowers-gstack-project-onboarding.md",
    }

    for source_rel, mapped in article_map.items():
        source_abs = ROOT / source_rel
        english_abs = ROOT / mapped["english_path"]
        replacements[rel_link(target_dir, source_abs)] = rel_link(target_dir, english_abs)
        replacements["../" + source_rel] = rel_link(target_dir, english_abs)
        replacements["./" + source_rel] = rel_link(target_dir, english_abs)

    for old, new in sorted(replacements.items(), key=lambda item: len(item[0]), reverse=True):
        text = text.replace(f"]({old})", f"]({new})")
    return text


def rel_link(from_dir: Path, to_path: Path) -> str:
    return Path.relative_to(to_path.resolve(), ROOT.resolve()).as_posix() if False else _rel(from_dir, to_path)


def _rel(from_dir: Path, to_path: Path) -> str:
    import os

    return os.path.relpath(to_path, from_dir).replace("\\", "/")


def main() -> None:
    article_map = json.loads(ARTICLE_MAP_PATH.read_text(encoding="utf-8"))
    for source_rel, target_rel in DOCS:
        source_path = ROOT / source_rel
        target_path = ROOT / target_rel
        target_path.parent.mkdir(parents=True, exist_ok=True)
        text = translate_doc(source_path.read_text(encoding="utf-8"), target_path, article_map)
        target_path.write_text(text, encoding="utf-8")
        print(f"{source_rel} -> {target_rel}")


if __name__ == "__main__":
    main()
