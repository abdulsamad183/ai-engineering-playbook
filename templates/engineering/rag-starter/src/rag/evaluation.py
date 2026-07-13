"""Minimal RAG evaluation harness."""

from dataclasses import dataclass


@dataclass
class EvalCase:
    question: str
    expected_keywords: list[str]


def score_answer(answer: str, case: EvalCase) -> float:
    hits = sum(1 for kw in case.expected_keywords if kw.lower() in answer.lower())
    return hits / max(1, len(case.expected_keywords))
