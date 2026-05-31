#!/usr/bin/env python3
"""Guard Markdown articles against one-line or underdeveloped submissions."""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


ARTICLE_ROOTS = ("ai-articles", "archive-bestjavaer")
DEFAULT_MIN_CHARS = int(os.getenv("ARTICLE_QUALITY_MIN_CHARS", "600"))
DEFAULT_MIN_PARAGRAPHS = int(os.getenv("ARTICLE_QUALITY_MIN_PARAGRAPHS", "5"))
DEFAULT_MIN_SENTENCES = int(os.getenv("ARTICLE_QUALITY_MIN_SENTENCES", "8"))
MIN_PARAGRAPH_CHARS = 20
ZERO_SHA = re.compile(r"^0{40}$")


@dataclass(frozen=True)
class Metrics:
    chars: int
    paragraphs: int
    sentences: int


@dataclass(frozen=True)
class Failure:
    path: Path
    metrics: Metrics
    issues: tuple[str, ...]


def run_git(args: list[str], *, check: bool = True) -> str:
    result = subprocess.run(
        ["git", *args],
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if check and result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or f"git {' '.join(args)} failed")
    return result.stdout


def is_article_path(path: Path) -> bool:
    parts = path.parts
    if not parts or path.suffix.lower() != ".md":
        return False
    if path.name.lower() == "readme.md":
        return False
    return parts[0] in ARTICLE_ROOTS


def all_article_files() -> list[Path]:
    files: list[Path] = []
    for root in ARTICLE_ROOTS:
        base = Path(root)
        if base.exists():
            files.extend(p for p in base.rglob("*.md") if is_article_path(p))
    return sorted(files)


def changed_files(base: str, head: str) -> list[Path]:
    if ZERO_SHA.fullmatch(base):
        return all_article_files()

    diff_expr = f"{base}...{head}"
    output = run_git(["diff", "--name-only", "--diff-filter=ACMRT", diff_expr], check=False)
    if not output.strip():
        output = run_git(["diff", "--name-only", "--diff-filter=ACMRT", f"{base}..{head}"])
    return sorted(Path(line) for line in output.splitlines() if line.strip())


def staged_files() -> list[Path]:
    output = run_git(["diff", "--cached", "--name-only", "--diff-filter=ACMRT"])
    return sorted(Path(line) for line in output.splitlines() if line.strip())


def strip_markdown(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n").lstrip("\ufeff")
    text = re.sub(r"\A---\n.*?\n---\n", "\n", text, flags=re.S)
    text = re.sub(r"```.*?```", "\n", text, flags=re.S)
    text = re.sub(r"<!--.*?-->", "\n", text, flags=re.S)

    lines: list[str] = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped:
            lines.append("")
            continue
        if stripped.startswith(("> 日期", "> Date", "> date")):
            continue
        if stripped.startswith("![") or stripped.lower().startswith("<img"):
            continue
        if re.fullmatch(r"\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?", stripped):
            continue
        lines.append(line)

    text = "\n".join(lines)
    text = re.sub(r"!\[[^\]]*]\([^)]*\)", " ", text)
    text = re.sub(r"\[([^\]]+)]\([^)]*\)", r"\1", text)
    text = re.sub(r"https?://\S+", " ", text)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"[`*_~>#-]+", " ", text)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def meaningful_chars(text: str) -> int:
    tokens = re.findall(r"[\u4e00-\u9fff]|[A-Za-z0-9]+", text)
    return sum(len(token) for token in tokens)


def measure(text: str) -> Metrics:
    clean = strip_markdown(text)
    paragraphs = [
        paragraph
        for paragraph in re.split(r"\n\s*\n+", clean)
        if meaningful_chars(paragraph) >= MIN_PARAGRAPH_CHARS
    ]
    sentences = [
        sentence
        for sentence in re.split(r"[。！？!?；;\n]+", clean)
        if meaningful_chars(sentence) >= 8
    ]
    return Metrics(
        chars=meaningful_chars(clean),
        paragraphs=len(paragraphs),
        sentences=len(sentences),
    )


def read_path(path: Path, *, staged: bool) -> str:
    if staged:
        return run_git(["show", f":{path.as_posix()}"])
    return path.read_text(encoding="utf-8")


def collect_paths(args: argparse.Namespace) -> tuple[list[Path], bool]:
    if args.paths:
        return [Path(path) for path in args.paths], False
    if args.all:
        return all_article_files(), False
    if args.staged:
        return staged_files(), True
    if args.base:
        return changed_files(args.base, args.head), False
    return staged_files(), True


def check_files(args: argparse.Namespace) -> list[Failure]:
    paths, use_staged_content = collect_paths(args)
    article_paths = sorted({path for path in paths if is_article_path(path)})
    failures: list[Failure] = []

    for path in article_paths:
        if not use_staged_content and not path.exists():
            continue

        metrics = measure(read_path(path, staged=use_staged_content))
        issues: list[str] = []
        if metrics.chars < args.min_chars:
            issues.append(f"body has {metrics.chars} meaningful chars; expected >= {args.min_chars}")
        if metrics.paragraphs < args.min_paragraphs:
            issues.append(f"has {metrics.paragraphs} developed paragraphs; expected >= {args.min_paragraphs}")
        if metrics.sentences < args.min_sentences:
            issues.append(f"has {metrics.sentences} developed sentences; expected >= {args.min_sentences}")

        if issues:
            failures.append(Failure(path=path, metrics=metrics, issues=tuple(issues)))

    return failures


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Check changed Markdown articles for minimum article structure.",
    )
    parser.add_argument("paths", nargs="*", help="Specific files to check.")
    parser.add_argument("--all", action="store_true", help="Check every article file.")
    parser.add_argument("--staged", action="store_true", help="Check staged article files.")
    parser.add_argument("--base", help="Base git revision for changed-file checks.")
    parser.add_argument("--head", default="HEAD", help="Head git revision for changed-file checks.")
    parser.add_argument("--min-chars", type=int, default=DEFAULT_MIN_CHARS)
    parser.add_argument("--min-paragraphs", type=int, default=DEFAULT_MIN_PARAGRAPHS)
    parser.add_argument("--min-sentences", type=int, default=DEFAULT_MIN_SENTENCES)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    failures = check_files(args)

    if not failures:
        print("Article quality check passed.")
        return 0

    print("Article quality check failed.")
    print(
        "Rules: "
        f">= {args.min_chars} meaningful chars, "
        f">= {args.min_paragraphs} developed paragraphs, "
        f">= {args.min_sentences} developed sentences."
    )
    for failure in failures:
        metrics = failure.metrics
        print(f"\n{failure.path}")
        print(
            f"  metrics: chars={metrics.chars}, "
            f"paragraphs={metrics.paragraphs}, sentences={metrics.sentences}"
        )
        for issue in failure.issues:
            print(f"  - {issue}")

    return 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except RuntimeError as error:
        print(f"article quality check error: {error}", file=sys.stderr)
        raise SystemExit(2)
