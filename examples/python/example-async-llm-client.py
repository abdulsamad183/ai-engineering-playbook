"""Async LLM client with retry and timeout.

Production patterns: exponential backoff, timeout, structured errors.

Prerequisites:
    pip install httpx tenacity

Run:
    python example-async-llm-client.py
"""

from __future__ import annotations

import asyncio
import logging
from dataclasses import dataclass

import httpx
from tenacity import (
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential_jitter,
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@dataclass
class LLMResponse:
    content: str
    model: str
    input_tokens: int
    output_tokens: int


class LLMError(Exception):
    pass


class LLMTimeoutError(LLMError):
    pass


class MockLLMClient:
    """Simulates an LLM API with configurable failure rate."""

    def __init__(self, fail_count: int = 0) -> None:
        self._calls = 0
        self._fail_count = fail_count

    @retry(
        retry=retry_if_exception_type((httpx.TimeoutException, httpx.HTTPStatusError)),
        stop=stop_after_attempt(3),
        wait=wait_exponential_jitter(initial=1, max=10),
        reraise=True,
    )
    async def complete(self, prompt: str, timeout: float = 30.0) -> LLMResponse:
        self._calls += 1
        logger.info("LLM call attempt %d", self._calls)

        async with httpx.AsyncClient(timeout=timeout) as client:
            # Simulate API — replace with real OpenAI endpoint in production
            if self._calls <= self._fail_count:
                raise httpx.HTTPStatusError(
                    "Rate limited",
                    request=httpx.Request("POST", "https://api.openai.com/v1/chat/completions"),
                    response=httpx.Response(429),
                )

            return LLMResponse(
                content=f"Response to: {prompt}",
                model="gpt-4o-mini",
                input_tokens=len(prompt.split()),
                output_tokens=20,
            )


async def main() -> None:
    client = MockLLMClient(fail_count=2)  # fails twice, succeeds on third
    response = await client.complete("What is dependency injection?")
    print(f"Model: {response.model}")
    print(f"Content: {response.content}")
    print(f"Total calls: {client._calls}")


if __name__ == "__main__":
    asyncio.run(main())
