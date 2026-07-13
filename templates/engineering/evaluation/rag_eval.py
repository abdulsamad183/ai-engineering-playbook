"""RAG evaluation — faithfulness and recall proxies."""

from dataclasses import dataclass


@dataclass
class RAGEvalCase:
    question: str
    context: str
    answer: str
    expected_facts: list[str]


def faithfulness_score(case: RAGEvalCase) -> float:
    return sum(1 for f in case.expected_facts if f.lower() in case.answer.lower()) / max(
        1, len(case.expected_facts)
    )
