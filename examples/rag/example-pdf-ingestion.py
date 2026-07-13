"""PDF ingestion for RAG — parse, hash, metadata.

Run: python example-pdf-ingestion.py
Requires: pymupdf (pip install pymupdf)
"""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
from pathlib import Path


@dataclass
class ParsedPDF:
    doc_id: str
    text: str
    page_count: int
    content_hash: str
    metadata: dict


def parse_pdf(path: Path, doc_id: str) -> ParsedPDF:
    import fitz  # PyMuPDF

    doc = fitz.open(path)
    pages = [page.get_text() for page in doc]
    text = "\n\n".join(pages)
    content_hash = hashlib.sha256(text.encode()).hexdigest()
    return ParsedPDF(
        doc_id=doc_id,
        text=text,
        page_count=len(pages),
        content_hash=content_hash,
        metadata={"source_uri": str(path), "format": "pdf"},
    )


if __name__ == "__main__":
    print("PDF ingestion ready — provide a path to parse_pdf(Path('doc.pdf'), 'doc-1')")
