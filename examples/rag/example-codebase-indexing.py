"""Codebase indexing — walk repo and chunk by file.

Run: python example-codebase-indexing.py
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass
class CodeChunk:
    chunk_id: str
    path: str
    language: str
    content: str


EXTENSION_LANG = {".py": "python", ".ts": "typescript", ".go": "go", ".md": "markdown"}


def index_repository(root: Path, max_file_bytes: int = 50_000) -> list[CodeChunk]:
    chunks: list[CodeChunk] = []
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix not in EXTENSION_LANG:
            continue
        if path.stat().st_size > max_file_bytes:
            continue
        if "node_modules" in path.parts or ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        rel = str(path.relative_to(root))
        chunks.append(CodeChunk(
            chunk_id=f"{rel}#0",
            path=rel,
            language=EXTENSION_LANG[path.suffix],
            content=text,
        ))
    return chunks


if __name__ == "__main__":
    root = Path(".")
    found = index_repository(root)
    print(f"Indexed {len(found)} files")
