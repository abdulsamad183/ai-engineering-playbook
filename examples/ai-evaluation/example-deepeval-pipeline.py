"""DeepEval-style pytest pipeline (simplified).

Run: python example-deepeval-pipeline.py
"""

from eval_utils import EvalCase, exact_match


def evaluate_case(case: EvalCase, actual: str, metrics: list) -> dict:
    scores = {}
    for name, fn, threshold in metrics:
        score = fn(actual, case)
        scores[name] = {"score": score, "pass": score >= threshold}
    return scores


def main() -> None:
    case = EvalCase(id="t1", input="Capital of France?", expected="Paris")
    actual = "Paris"
    metrics = [("exact_match", lambda a, c: exact_match(a, c.expected or ""), 1.0)]
    result = evaluate_case(case, actual, metrics)
    assert result["exact_match"]["pass"], "DeepEval-style assert failed"
    print("PASS:", result)


if __name__ == "__main__":
    main()
