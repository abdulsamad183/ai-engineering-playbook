"""RAG evaluation — recall@K and golden case runner.

Run: python example-rag-evaluation.py
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class GoldenCase:
    question: str
    gold_doc_ids: set[str]


def recall_at_k(retrieved: list[str], gold: set[str], k: int) -> float:
    if not gold:
        return 1.0
    hit = len(set(retrieved[:k]) & gold)
    return hit / len(gold)


def evaluate_cases(cases: list[GoldenCase], retrieve_fn, k: int = 5) -> float:
    scores = []
    for case in cases:
        retrieved = retrieve_fn(case.question)
        scores.append(recall_at_k(retrieved, case.gold_doc_ids, k))
    return sum(scores) / len(scores) if scores else 0.0


if __name__ == "__main__":
    cases = [GoldenCase("refund SLA", {"policy-refund"})]

    def mock_retrieve(q: str) -> list[str]:
        return ["policy-refund", "policy-shipping"]

    print("Mean recall@5:", evaluate_cases(cases, mock_retrieve))
