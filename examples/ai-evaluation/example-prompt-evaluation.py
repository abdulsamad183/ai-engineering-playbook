"""Prompt evaluation — consistency and regression.

Run: python example-prompt-evaluation.py
"""

import random

from eval_utils import EvalCase, exact_match, run_eval_suite


async def system_v1(q: str) -> str:
    return "Paris" if "france" in q.lower() else "unknown"


async def system_v2(q: str) -> str:
    return "Paris, France" if "france" in q.lower() else "unknown"


async def measure_consistency(fn, question: str, n: int = 5) -> float:
    random.seed(42)
    outputs = [await fn(question) for _ in range(n)]
    return len(set(outputs)) / len(outputs)  # lower = more consistent


async def main() -> None:
    cases = [EvalCase(id="1", input="Capital of France?", expected="Paris")]
    r1 = await run_eval_suite(cases, system_v1, {"exact": lambda o, c: exact_match(o, c.expected or "")})
    r2 = await run_eval_suite(cases, system_v2, {"exact": lambda o, c: exact_match(o, c.expected or "")})
    print("v1 exact:", r1[0].scores)
    print("v2 exact:", r2[0].scores)
    print("v1 consistency variance:", await measure_consistency(system_v1, cases[0].input))


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
