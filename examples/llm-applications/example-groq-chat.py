"""Groq API — OpenAI-compatible fast inference.

Environment: GROQ_API_KEY=gsk_...

Run: python example-groq-chat.py
"""

from __future__ import annotations

import os

from openai import AsyncOpenAI

client = AsyncOpenAI(
    api_key=os.environ["GROQ_API_KEY"],
    base_url="https://api.groq.com/openai/v1",
)


async def chat(message: str, model: str = "llama-3.3-70b-versatile") -> str:
    response = await client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": message}],
        max_tokens=500,
        temperature=0.2,
    )
    return response.choices[0].message.content or ""


async def main() -> None:
    print(await chat("Why is Groq fast for inference?"))


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
