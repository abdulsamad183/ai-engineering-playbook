"""High-level prompt evaluation framework.

Run: python example-prompt-evaluation.py
"""

from __future__ import annotations

import json
from dataclasses import dataclass


@dataclass
class EvalCase:
    id: str
    input: str
    expected_category: str
    expected_contains: list[str] | None = None


@dataclass
class EvalResult:
    case_id: str
    passed: bool
    actual: str
    failures: list[str]


GOLDEN_SET = [
    EvalCase("001", "Double charged on invoice", "billing"),
    EvalCase("002", "500 error on login", "technical"),
    EvalCase("003", "Reset my password", "account"),
]


def evaluate_classification(actual_json: str, case: EvalCase) -> EvalResult:
    failures = []
    try:
        data = json.loads(actual_json)
        category = data.get("category", "")
        if category != case.expected_category:
            failures.append(f"Expected category {case.expected_category}, got {category}")
    except json.JSONDecodeError:
        failures.append("Invalid JSON output")

    return EvalResult(
        case_id=case.id,
        passed=len(failures) == 0,
        actual=actual_json,
        failures=failures,
    )


def run_eval_suite(predict_fn, cases: list[EvalCase]) -> dict:
    results = [evaluate_classification(predict_fn(c.input), c) for c in cases]
    passed = sum(1 for r in results if r.passed)
    return {
        "total": len(results),
        "passed": passed,
        "accuracy": passed / len(results) if results else 0,
        "failures": [r for r in results if not r.passed],
    }


def mock_predict(text: str) -> str:
    if "charged" in text or "invoice" in text:
        return '{"category": "billing", "confidence": 0.9}'
    if "error" in text or "500" in text:
        return '{"category": "technical", "confidence": 0.9}'
    return '{"category": "account", "confidence": 0.8}'


if __name__ == "__main__":
    report = run_eval_suite(mock_predict, GOLDEN_SET)
    print(json.dumps({k: v for k, v in report.items() if k != "failures"}, indent=2))
    print(f"Accuracy: {report['accuracy']:.0%}")
