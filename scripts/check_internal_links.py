#!/usr/bin/env python3
"""Fail when a Markdown link points to a missing local path."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
SKIPPED_TREES = (ROOT / "docs", ROOT / "meta" / "templates")


def markdown_files() -> list[Path]:
    return [
        path
        for path in ROOT.rglob("*.md")
        if ".git" not in path.parts
        and not any(path.is_relative_to(tree) for tree in SKIPPED_TREES)
    ]


def destination(raw: str) -> str:
    value = raw.strip()
    if value.startswith("<") and ">" in value:
        return value[1 : value.index(">")]
    return value.split(maxsplit=1)[0]


def failures(path: Path) -> list[tuple[int, str]]:
    problems: list[tuple[int, str]] = []
    in_fence = False
    fence = ""

    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        marker = line.lstrip()[:3]
        if marker in {"```", "~~~"}:
            if not in_fence:
                in_fence, fence = True, marker
            elif marker == fence:
                in_fence, fence = False, ""
            continue
        if in_fence:
            continue

        prose = re.sub(r"`[^`\n]+`", "", line)
        for match in LINK.finditer(prose):
            target = destination(match.group(1))
            if not target or target.startswith(("#", "http://", "https://", "mailto:")):
                continue
            if "{{" in target or "}}" in target:
                continue
            local_path = unquote(target.split("#", 1)[0])
            if local_path and not (path.parent / local_path).resolve().exists():
                problems.append((line_number, target))
    return problems


def main() -> int:
    files = markdown_files()
    broken = [
        (path.relative_to(ROOT), line, target)
        for path in files
        for line, target in failures(path)
    ]
    if broken:
        print(f"Found {len(broken)} broken internal Markdown link(s):", file=sys.stderr)
        for path, line, target in broken:
            print(f"  {path}:{line}: {target}", file=sys.stderr)
        return 1
    print(f"Checked internal links in {len(files)} Markdown files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
