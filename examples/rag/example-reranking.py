"""Cross-encoder reranking pattern for RAG.

Run: python example-reranking.py
Requires: sentence-transformers
"""

from __future__ import annotations


def rerank(query: str, passages: list[str], top_n: int = 5) -> list[tuple[str, float]]:
    from sentence_transformers import CrossEncoder

    model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")
    pairs = [[query, p] for p in passages]
    scores = model.predict(pairs)
    ranked = sorted(zip(passages, scores), key=lambda x: -float(x[1]))
    return ranked[:top_n]


if __name__ == "__main__":
    passages = [
        "Refunds process in 3 business days.",
        "SSO uses SAML metadata.",
        "Office hours are 9am-5pm.",
    ]
    try:
        print(rerank("refund timeline", passages))
    except ImportError:
        print("pip install sentence-transformers")
