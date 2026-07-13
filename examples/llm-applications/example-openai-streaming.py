"""Streaming LLM response via OpenAI API.

Run: python example-openai-streaming.py
"""

from __future__ import annotations

import os
import sys

from openai import AsyncOpenAI

client = AsyncOpenAI(api_key=os.environ["OPENAI_API_KEY"])


async def stream_chat(message: str, model: str = "gpt-4o-mini") -> None:
    stream = await client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": message}],
        stream=True,
        timeout=60.0,
    )
    async for chunk in stream:
        delta = chunk.choices[0].delta.content
        if delta:
            sys.stdout.write(delta)
            sys.stdout.flush()
    print()


async def main() -> None:
    await stream_chat("Write a haiku about async Python.")


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
