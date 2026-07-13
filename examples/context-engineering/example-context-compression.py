"""Context compression — trim ranked blocks to token budget.

Run: python example-context-compression.py
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Block:
    doc_id: str
    text: str
    tokens: int
    rank: float


def compress_to_budget(blocks: list[Block], budget: int) -> list[Block]:
    ordered = sorted(blocks, key=lambda b: -b.rank)
    selected: list[Block] = []
    used = 0
    for b in ordered:
        if used + b.tokens <= budget:
            selected.append(b)
            used += b.tokens
    if not selected and ordered:
        # Keep top block truncated conceptually
        top = ordered[0]
        selected = [Block(top.doc_id, top.text[: budget * 4], budget, top.rank)]
    return selected


if __name__ == "__main__":
    blocks = [
        Block("1", "policy text", 400, 0.95),
        Block("2", "faq text", 300, 0.80),
        Block("3", "noise", 200, 0.40),
    ]
    result = compress_to_budget(blocks, budget=500)
    print([(b.doc_id, b.tokens) for b in result])
