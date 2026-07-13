"""Regression testing gate for eval CI.

Run: python example-regression-testing.py
"""

from eval_utils import EvalCase, aggregate_scores, exact_match, run_eval_suite


async def current_system(q: str) -> str:
    q = q.lower()
    if "france" in q:
        return "Paris"
    if "japan" in q:
        return "Tokyo"
    return "unknown"


BASELINE_SCORES = {"exact": 1.0}
TOLERANCE = 0.05


async def main() -> None:
    cases = [
        EvalCase(id="1", input="Capital of France?", expected="Paris"),
        EvalCase(id="2", input="Capital of Japan?", expected="Tokyo"),
    ]
    results = await run_eval_suite(cases, current_system, {"exact": lambda o, c: exact_match(o, c.expected or "")})
    current = aggregate_scores(results)
    for metric, baseline in BASELINE_SCORES.items():
        if current[metric] < baseline - TOLERANCE:
            raise SystemExit(f"REGRESSION: {metric} {current[metric]:.2f} < {baseline - TOLERANCE:.2f}")
    print("PASS regression gate:", current)


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
