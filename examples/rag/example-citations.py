"""Citations — format sources and validate cited IDs.

Run: python example-citations.py
"""

from __future__ import annotations

import re
from dataclasses import dataclass


@dataclass
class Source:
    chunk_id: str
    title: str
    uri: str


def format_sources_block(sources: list[Source]) -> str:
    lines = ["<sources>"]
    for s in sources:
        lines.append(f'<source id="{s.chunk_id}" title="{s.title}" uri="{s.uri}" />')
    lines.append("</sources>")
    return "\n".join(lines)


def extract_cited_ids(answer: str) -> set[str]:
    return set(re.findall(r"\[(chunk-[^\]]+)\]", answer))


def validate_citations(answer: str, allowed_ids: set[str]) -> list[str]:
    cited = extract_cited_ids(answer)
    return sorted(cited - allowed_ids)


if __name__ == "__main__":
    sources = [Source("chunk-1", "Refund Policy", "s3://kb/refund.pdf")]
    print(format_sources_block(sources))
    print(validate_citations("Refunds take 3 days [chunk-1] [chunk-99]", {"chunk-1"}))
