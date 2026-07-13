"""Retry helper with exponential backoff."""

import asyncio
from collections.abc import Awaitable, Callable
from typing import TypeVar

T = TypeVar("T")


async def with_retry(
    fn: Callable[[], Awaitable[T]],
    *,
    max_attempts: int = 3,
    base_delay: float = 0.5,
    retry_on: tuple[type[Exception], ...] = (Exception,),
) -> T:
    last: Exception | None = None
    for attempt in range(max_attempts):
        try:
            return await fn()
        except retry_on as exc:
            last = exc
            if attempt == max_attempts - 1:
                break
            await asyncio.sleep(base_delay * (2**attempt))
    raise last  # type: ignore[misc]
