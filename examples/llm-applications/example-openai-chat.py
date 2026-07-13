"""OpenAI Chat Completions API example.

Prerequisites: pip install openai
Environment: OPENAI_API_KEY=sk-...

Run: python example-openai-chat.py
"""

from __future__ import annotations

import os

from openai import AsyncOpenAI

client = AsyncOpenAI(api_key=os.environ["OPENAI_API_KEY"])


async def chat(message: str, model: str = "gpt-4o-mini") -> str:
    response = await client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": message}],
        max_tokens=500,
        temperature=0.3,
        timeout=30.0,
    )
    usage = response.usage
    print(f"Tokens: in={usage.prompt_tokens} out={usage.completion_tokens}")
    return response.choices[0].message.content or ""


async def main() -> None:
    answer = await chat("Explain KV cache in one paragraph.")
    print(answer)


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
