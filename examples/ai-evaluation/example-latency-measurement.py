"""Latency measurement for AI pipelines.

Run: python example-latency-measurement.py
"""

import asyncio
import statistics
import time


async def fake_retrieval() -> None:
    await asyncio.sleep(0.05)


async def fake_llm() -> str:
    await asyncio.sleep(0.2)
    return "answer"


async def measure_pipeline(n: int = 10) -> dict:
    e2e_samples: list[float] = []
    for _ in range(n):
        start = time.perf_counter()
        await fake_retrieval()
        await fake_llm()
        e2e_samples.append((time.perf_counter() - start) * 1000)
    e2e_samples.sort()
    p95_idx = int(0.95 * len(e2e_samples)) - 1
    return {"p50_ms": statistics.median(e2e_samples), "p95_ms": e2e_samples[p95_idx]}


async def main() -> None:
    print(await measure_pipeline())


if __name__ == "__main__":
    asyncio.run(main())
