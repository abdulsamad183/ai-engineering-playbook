"""BM25 lexical retrieval example.

Run: python example-bm25-retrieval.py
Requires: rank-bm25
"""

from __future__ import annotations


def bm25_search(documents: list[str], query: str, top_k: int = 5) -> list[int]:
    from rank_bm25 import BM25Okapi

    tokenized = [doc.lower().split() for doc in documents]
    bm25 = BM25Okapi(tokenized)
    scores = bm25.get_scores(query.lower().split())
    return sorted(range(len(scores)), key=lambda i: -scores[i])[:top_k]


if __name__ == "__main__":
    docs = [
        "Refund policy allows 3 business days processing",
        "SSO login requires SAML metadata configuration",
        "API rate limit is 1000 requests per minute",
    ]
    print(bm25_search(docs, "refund processing time"))
