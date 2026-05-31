#!/usr/bin/env python3
"""Guard Markdown articles against thin content and broken image references."""

from __future__ import annotations

import argparse
import html
import os
import re
import subprocess
import sys
from dataclasses import dataclass, replace
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import unquote, urlsplit
from urllib.request import Request, urlopen


ARTICLE_ROOTS = ("ai-articles", "archive-bestjavaer")
DEFAULT_MIN_CHARS = int(os.getenv("ARTICLE_QUALITY_MIN_CHARS", "600"))
DEFAULT_MIN_PARAGRAPHS = int(os.getenv("ARTICLE_QUALITY_MIN_PARAGRAPHS", "5"))
DEFAULT_MIN_SENTENCES = int(os.getenv("ARTICLE_QUALITY_MIN_SENTENCES", "8"))
DEFAULT_MAX_BROKEN_IMAGES = int(os.getenv("ARTICLE_QUALITY_MAX_BROKEN_IMAGES", "0"))
DEFAULT_CHECK_REMOTE_IMAGES = os.getenv("ARTICLE_QUALITY_CHECK_REMOTE_IMAGES", "1").lower() not in {
    "0",
    "false",
    "no",
}
DEFAULT_REMOTE_IMAGE_TIMEOUT = float(os.getenv("ARTICLE_QUALITY_REMOTE_IMAGE_TIMEOUT", "5"))
DEFAULT_MAX_IMAGE_ERRORS = int(os.getenv("ARTICLE_QUALITY_MAX_IMAGE_ERRORS", "20"))
MIN_PARAGRAPH_CHARS = 20
ZERO_SHA = re.compile(r"^0{40}$")
MARKDOWN_IMAGE_RE = re.compile(r"!\[[^\]\n]*]\((?P<target>[^)\n]+)\)")
HTML_IMG_RE = re.compile(r"<img\b[^>]*>", re.I)
HTML_SRC_RE = re.compile(
    r"""\bsrc\s*=\s*(?:"(?P<double>[^"]*)"|'(?P<single>[^']*)'|(?P<bare>[^\s>]+))""",
    re.I,
)
REMOTE_IMAGE_CACHE: dict[str, str | None] = {}


@dataclass(frozen=True)
class Metrics:
    chars: int
    paragraphs: int
    sentences: int
    images: int = 0
    broken_images: int = 0


@dataclass(frozen=True)
class ImageRef:
    line: int
    target: str


@dataclass(frozen=True)
class ImageIssue:
    line: int
    target: str
    issue: str


@dataclass(frozen=True)
class Failure:
    path: Path
    metrics: Metrics
    issues: tuple[str, ...]
    image_issues: tuple[ImageIssue, ...] = ()


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


def repo_root() -> Path:
    return Path(run_git(["rev-parse", "--show-toplevel"]).strip()).resolve()


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


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def preserve_shape(match: re.Match[str]) -> str:
    return "".join("\n" if char == "\n" else " " for char in match.group(0))


def mask_ignored_markdown_blocks(text: str) -> str:
    text = re.sub(r"```.*?```", preserve_shape, text, flags=re.S)
    text = re.sub(r"<!--.*?-->", preserve_shape, text, flags=re.S)
    return text


def normalize_image_target(raw: str) -> str:
    target = html.unescape(raw).strip()
    if target.startswith("<") and ">" in target:
        return target[1 : target.index(">")].strip()

    for quote in ('"', "'"):
        marker = f" {quote}"
        if marker in target and target.endswith(quote):
            candidate = target[: target.rfind(marker)].strip()
            if candidate:
                return candidate
    return target


def find_image_refs(text: str) -> list[ImageRef]:
    search_text = mask_ignored_markdown_blocks(text)
    refs: list[tuple[int, ImageRef]] = []
    for match in MARKDOWN_IMAGE_RE.finditer(search_text):
        refs.append(
            (
                match.start(),
                ImageRef(
                    line=line_number(text, match.start()),
                    target=normalize_image_target(match.group("target")),
                ),
            )
        )

    for match in HTML_IMG_RE.finditer(search_text):
        src_match = HTML_SRC_RE.search(match.group(0))
        if not src_match:
            continue
        target = src_match.group("double") or src_match.group("single") or src_match.group("bare") or ""
        refs.append(
            (
                match.start(),
                ImageRef(
                    line=line_number(text, match.start()),
                    target=normalize_image_target(target),
                ),
            )
        )

    return [ref for _, ref in sorted(refs, key=lambda item: item[0])]


def index_has_file(path: Path) -> bool:
    result = subprocess.run(
        ["git", "cat-file", "-e", f":{path.as_posix()}"],
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return result.returncode == 0


def repo_relative(path: Path, root: Path) -> Path | None:
    try:
        return path.resolve(strict=False).relative_to(root)
    except ValueError:
        return None


def looks_like_local_absolute_path(path: str) -> bool:
    return path.startswith(("/Users/", "/home/", "/tmp/", "/var/", "/Volumes/", "/private/"))


def local_image_issue(article_path: Path, target: str, *, staged: bool, root: Path) -> str | None:
    split = urlsplit(target)
    if split.scheme == "file":
        return "uses a file:// image URL; use a repo-relative path or remote URL"
    if split.scheme:
        return f"uses unsupported image URL scheme: {split.scheme}"

    path_text = unquote(split.path)
    if not path_text:
        return "image target is empty"
    if "\0" in path_text:
        return "image target contains a null byte"
    if looks_like_local_absolute_path(path_text):
        return "uses an absolute local filesystem path; use a repo-relative image path"

    candidate = root / path_text.lstrip("/") if path_text.startswith("/") else article_path.parent / path_text
    relative = repo_relative(candidate, root)
    if relative is None:
        return "local image points outside the repository"

    if staged:
        if index_has_file(relative):
            return None
        if candidate.exists():
            return f"local image exists but is not staged: {relative.as_posix()}"
        return f"local image file not found: {relative.as_posix()}"

    if not candidate.is_file():
        return f"local image file not found: {relative.as_posix()}"
    return None


def remote_image_issue(url: str, timeout: float) -> str | None:
    url = url.split("#", 1)[0]
    if url in REMOTE_IMAGE_CACHE:
        return REMOTE_IMAGE_CACHE[url]

    issue = request_remote_image(url, timeout)
    REMOTE_IMAGE_CACHE[url] = issue
    return issue


def request_remote_image(url: str, timeout: float) -> str | None:
    fallback_codes = {403, 405, 501}
    try:
        return fetch_remote_image(url, timeout=timeout, method="HEAD")
    except HTTPError as error:
        if error.code not in fallback_codes:
            return f"remote image returned HTTP {error.code}"
    except (TimeoutError, URLError, OSError, ValueError) as error:
        return remote_error_message(error)

    try:
        return fetch_remote_image(url, timeout=timeout, method="GET")
    except HTTPError as error:
        return f"remote image returned HTTP {error.code}"
    except (TimeoutError, URLError, OSError, ValueError) as error:
        return remote_error_message(error)


def fetch_remote_image(url: str, *, timeout: float, method: str) -> str | None:
    headers = {
        "Accept": "image/*,*/*;q=0.8",
        "User-Agent": "bestjavaer-article-quality/1.0",
    }
    if method == "GET":
        headers["Range"] = "bytes=0-0"

    request = Request(url, headers=headers, method=method)
    with urlopen(request, timeout=timeout) as response:
        status = response.getcode()
        if not 200 <= status < 400:
            return f"remote image returned HTTP {status}"

        content_type = response.headers.get("Content-Type", "").split(";", 1)[0].lower()
        if content_type == "text/html":
            return "remote image returned HTML instead of an image"
    return None


def remote_error_message(error: BaseException) -> str:
    if isinstance(error, URLError):
        return f"remote image is unreachable: {error.reason}"
    return f"remote image is unreachable: {error}"


def image_issue(article_path: Path, ref: ImageRef, *, staged: bool, args: argparse.Namespace, root: Path) -> str | None:
    target = ref.target.strip()
    if not target:
        return "image target is empty"

    lower_target = target.lower()
    if lower_target.startswith("data:image/"):
        return None
    if lower_target.startswith("data:"):
        return "data URI is not an image"
    if target.startswith("//"):
        if not args.check_remote_images:
            return None
        return remote_image_issue(f"https:{target}", args.remote_image_timeout)

    split = urlsplit(target)
    if split.scheme in {"http", "https"}:
        if not args.check_remote_images:
            return None
        return remote_image_issue(target, args.remote_image_timeout)

    return local_image_issue(article_path, target, staged=staged, root=root)


def check_images(
    article_path: Path,
    text: str,
    *,
    staged: bool,
    args: argparse.Namespace,
    root: Path,
) -> tuple[int, tuple[ImageIssue, ...]]:
    refs = find_image_refs(text)
    issues = [
        ImageIssue(line=ref.line, target=ref.target, issue=issue)
        for ref in refs
        if (issue := image_issue(article_path, ref, staged=staged, args=args, root=root))
    ]
    return len(refs), tuple(issues)


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
    root = repo_root()

    for path in article_paths:
        if not use_staged_content and not path.exists():
            continue

        text = read_path(path, staged=use_staged_content)
        metrics = measure(text)
        image_count, image_issues = check_images(
            path,
            text,
            staged=use_staged_content,
            args=args,
            root=root,
        )
        metrics = replace(
            metrics,
            images=image_count,
            broken_images=len(image_issues),
        )
        issues: list[str] = []
        if metrics.chars < args.min_chars:
            issues.append(f"body has {metrics.chars} meaningful chars; expected >= {args.min_chars}")
        if metrics.paragraphs < args.min_paragraphs:
            issues.append(f"has {metrics.paragraphs} developed paragraphs; expected >= {args.min_paragraphs}")
        if metrics.sentences < args.min_sentences:
            issues.append(f"has {metrics.sentences} developed sentences; expected >= {args.min_sentences}")
        if metrics.broken_images > args.max_broken_images:
            issues.append(
                f"has {metrics.broken_images} broken image references; "
                f"expected <= {args.max_broken_images}"
            )

        if issues:
            failures.append(
                Failure(
                    path=path,
                    metrics=metrics,
                    issues=tuple(issues),
                    image_issues=image_issues,
                )
            )

    return failures


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Check changed Markdown articles for content depth and image health.",
    )
    parser.add_argument("paths", nargs="*", help="Specific files to check.")
    parser.add_argument("--all", action="store_true", help="Check every article file.")
    parser.add_argument("--staged", action="store_true", help="Check staged article files.")
    parser.add_argument("--base", help="Base git revision for changed-file checks.")
    parser.add_argument("--head", default="HEAD", help="Head git revision for changed-file checks.")
    parser.add_argument("--min-chars", type=int, default=DEFAULT_MIN_CHARS)
    parser.add_argument("--min-paragraphs", type=int, default=DEFAULT_MIN_PARAGRAPHS)
    parser.add_argument("--min-sentences", type=int, default=DEFAULT_MIN_SENTENCES)
    parser.add_argument("--max-broken-images", type=int, default=DEFAULT_MAX_BROKEN_IMAGES)
    parser.add_argument(
        "--check-remote-images",
        dest="check_remote_images",
        action="store_true",
        default=DEFAULT_CHECK_REMOTE_IMAGES,
        help="Validate remote image URLs with HTTP requests.",
    )
    parser.add_argument(
        "--skip-remote-images",
        dest="check_remote_images",
        action="store_false",
        help="Skip HTTP checks for remote image URLs.",
    )
    parser.add_argument("--remote-image-timeout", type=float, default=DEFAULT_REMOTE_IMAGE_TIMEOUT)
    parser.add_argument("--max-image-errors", type=int, default=DEFAULT_MAX_IMAGE_ERRORS)
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
        f">= {args.min_sentences} developed sentences, "
        f"<= {args.max_broken_images} broken image references."
    )
    for failure in failures:
        metrics = failure.metrics
        print(f"\n{failure.path}")
        print(
            f"  metrics: chars={metrics.chars}, "
            f"paragraphs={metrics.paragraphs}, sentences={metrics.sentences}, "
            f"images={metrics.images}, broken_images={metrics.broken_images}"
        )
        for issue in failure.issues:
            print(f"  - {issue}")
        for image_issue in failure.image_issues[: args.max_image_errors]:
            print(f"  image line {image_issue.line}: {image_issue.target}")
            print(f"    - {image_issue.issue}")
        remaining = len(failure.image_issues) - args.max_image_errors
        if remaining > 0:
            print(f"  ... {remaining} more broken image references not shown")

    return 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except RuntimeError as error:
        print(f"article quality check error: {error}", file=sys.stderr)
        raise SystemExit(2)
