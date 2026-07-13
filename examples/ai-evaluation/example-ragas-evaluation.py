"""RAGAS-style RAG evaluation (simplified without ragas dependency).

Run: python example-ragas-evaluation.py
"""

from eval_utils import EvalCase, aggregate_scores, contains_match, run_eval_suite


def faithfulness(answer: str, case: EvalCase) -> float:
    if not case.context:
        return 1.0
    tokens = set(answer.lower().split())
    ctx_tokens = set(" ".join(case.context).lower().split())
    overlap = len(tokens & ctx_tokens) / max(len(tokens), 1)
    return min(1.0, overlap * 2)


def answer_relevancy(answer: str, case: EvalCase) -> float:
    return contains_match(answer, case.expected or "")


async def mock_rag(question: str) -> str:
    if "refund" in question.lower():
        return "Refunds are accepted within 30 days with receipt."
    return "I don't know."


async def main() -> None:
    cases = [
        EvalCase(
            id="1",
            input="What is the refund policy?",
            expected="30 days",
            context=["Refunds accepted within 30 days with receipt."],
        )
    ]
    results = await run_eval_suite(
        cases,
        mock_rag,
        {"faithfulness": faithfulness, "answer_relevancy": answer_relevancy},
    )
    print("Scores:", aggregate_scores(results))


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
