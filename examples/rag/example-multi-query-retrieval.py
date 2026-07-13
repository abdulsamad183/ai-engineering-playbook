"""Multi-query retrieval — generate variants and fuse results.

Run: python example-multi-query-retrieval.py
"""

from __future__ import annotations


def generate_query_variants(question: str) -> list[str]:
    return [
        question,
        question + " official policy",
        question.replace("?", ""),
    ]


def fuse_doc_lists(lists: list[list[str]], k: int = 60) -> list[str]:
    scores: dict[str, float] = {}
    for docs in lists:
        for rank, doc_id in enumerate(docs):
            scores[doc_id] = scores.get(doc_id, 0) + 1 / (k + rank + 1)
    return sorted(scores, key=scores.get, reverse=True)


if __name__ == "__main__":
    variants = generate_query_variants("What is the refund timeline?")
    results = [["doc-1", "doc-2"], ["doc-2", "doc-3"], ["doc-1", "doc-4"]]
    print(fuse_doc_lists(results))
