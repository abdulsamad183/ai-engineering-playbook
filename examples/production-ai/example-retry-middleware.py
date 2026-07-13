"""Retry middleware pattern for transient LLM errors.

Run: python example-retry-middleware.py
"""

import asyncio
import random


class TransientError(Exception):
    pass


async def with_retry(fn, max_attempts: int = 3, base_delay: float = 0.5):
    last_exc = None
    for attempt in range(max_attempts):
        try:
            return await fn()
        except TransientError as e:
            last_exc = e
            await asyncio.sleep(base_delay * (2 ** attempt))
    raise last_exc


async def flaky_llm() -> str:
    if random.random() < 0.6:
        raise TransientError("503 upstream")
    return "ok"


async def main() -> None:
    random.seed(1)
    result = await with_retry(flaky_llm)
    print("result:", result)


if __name__ == "__main__":
    asyncio.run(main())
