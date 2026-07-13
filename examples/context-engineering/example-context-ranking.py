"""Context ranking — hybrid score fusion demo.

Run: python example-context-ranking.py
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class RankCandidate:
    doc_id: str
    vector_score: float
    bm25_rank: int
    recency: float


def rrf(rank: int, k: int = 60) -> float:
    return 1 / (k + rank + 1)


def rank_candidates(candidates: list[RankCandidate]) -> list[RankCandidate]:
    def final_score(c: RankCandidate) -> float:
        return 0.5 * c.vector_score + 0.2 * c.recency + 0.3 * rrf(c.bm25_rank)

    return sorted(candidates, key=final_score, reverse=True)


if __name__ == "__main__":
    items = [
        RankCandidate("a", 0.91, 0, 0.3),
        RankCandidate("b", 0.88, 2, 0.9),
        RankCandidate("c", 0.95, 5, 0.1),
    ]
    for c in rank_candidates(items):
        print(c.doc_id, c.vector_score)
