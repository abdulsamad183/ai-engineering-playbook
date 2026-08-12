"""
Mini RAG — fully offline (no API keys).

Run from repo root:
  python examples/rag/mini_rag/run.py
"""
from __future__ import annotations

import math
import re
from collections import Counter
from dataclasses import dataclass


DOCS = {
    "refund.md": "Refunds are available within 30 days with a receipt. Digital goods are non-refundable after download.",
    "shipping.md": "Standard shipping takes 5-7 business days. Express shipping takes 2 business days.",
    "password.md": "Reset your password from Settings > Security. Use a unique password for this account.",
}


def tokenize(text: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", text.lower())


@dataclass
class Chunk:
    doc_id: str
    text: str
    tf: Counter


def build_index(docs: dict[str, str]) -> list[Chunk]:
    chunks: list[Chunk] = []
    for doc_id, text in docs.items():
        for para in text.split(". "):
            para = para.strip()
            if not para:
                continue
            toks = tokenize(para)
            chunks.append(Chunk(doc_id=doc_id, text=para, tf=Counter(toks)))
    return chunks


def score(query_tf: Counter, chunk: Chunk) -> float:
    # Prefer token overlap weighted by rarity in the chunk
    if not query_tf:
        return 0.0
    overlap = sum(min(query_tf[t], chunk.tf[t]) for t in query_tf)
    return overlap / max(1, sum(query_tf.values()))


def retrieve(chunks: list[Chunk], query: str, k: int = 2) -> list[Chunk]:
    q = Counter(tokenize(query))
    ranked = sorted(chunks, key=lambda c: score(q, c), reverse=True)
    return ranked[:k]


def answer(query: str, hits: list[Chunk]) -> str:
    q = Counter(tokenize(query))
    if not hits or score(q, hits[0]) <= 0:
        return "I don't know based on the docs."
    cites = ", ".join(f"[{h.doc_id}]" for h in hits)
    joined = " ".join(h.text for h in hits)
    return f"{joined} Sources: {cites}"


def main() -> None:
    index = build_index(DOCS)
    for q in ["How long for refunds?", "express shipping time", "quantum physics"]:
        hits = retrieve(index, q, k=2)
        print("Q:", q)
        print("A:", answer(q, hits))
        print("---")


if __name__ == "__main__":
    main()
