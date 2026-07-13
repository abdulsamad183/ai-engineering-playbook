"""Hybrid search — BM25 + dense fusion with RRF.

Run: python example-hybrid-search.py
"""

from __future__ import annotations


def rrf_fuse(rankings: list[list[str]], k: int = 60) -> list[str]:
    scores: dict[str, float] = {}
    for ranking in rankings:
        for rank, doc_id in enumerate(ranking):
            scores[doc_id] = scores.get(doc_id, 0) + 1 / (k + rank + 1)
    return sorted(scores, key=scores.get, reverse=True)


if __name__ == "__main__":
    dense = ["doc-a", "doc-b", "doc-c"]
    sparse = ["doc-b", "doc-d", "doc-a"]
    print(rrf_fuse([dense, sparse]))
