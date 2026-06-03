#!/usr/bin/env python3
"""Clean generated English article mirrors."""

from __future__ import annotations

import re
from pathlib import Path

import argostranslate.translate


ROOT = Path(__file__).resolve().parents[1]
TARGET_ROOT = ROOT / "en" / "ai-articles"
TRANSLATABLE_FENCES = {"", "prompt", "text", "txt", "markdown", "md"}


def translate_text(text: str) -> str:
    if not text.strip() or not re.search(r"[\u4e00-\u9fff]", text):
        return text
    return argostranslate.translate.translate(text, "zh", "en").strip()


def clean_text(text: str) -> str:
    lines = text.splitlines()
    out: list[str] = []
    in_fence = False
    fence_lang = ""
    fence_lines: list[str] = []

    def flush_fence() -> None:
        nonlocal fence_lines
        if fence_lang in TRANSLATABLE_FENCES and any(re.search(r"[\u4e00-\u9fff]", line) for line in fence_lines):
            translated = translate_text("\n".join(fence_lines))
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

        cleaned = re.sub(r"^(\s*)::\s+", r"\1- ", line)
        cleaned = re.sub(r"\s+\*\*$", "**", cleaned)
        cleaned = cleaned.replace("Cordex", "Codex")
        out.append(cleaned)

    if in_fence:
        flush_fence()

    return "\n".join(out).rstrip() + "\n"


def main() -> None:
    count = 0
    for path in TARGET_ROOT.glob("*/*.md"):
        before = path.read_text(encoding="utf-8")
        after = clean_text(before)
        if after != before:
            path.write_text(after, encoding="utf-8")
            count += 1
    print(f"postprocessed {count} English article files")


if __name__ == "__main__":
    main()
