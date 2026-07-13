"""OpenRouter unified multi-provider API.

Environment: OPENROUTER_API_KEY=sk-or-...

Run: python example-openrouter-chat.py
"""

from __future__ import annotations

import os

from openai import AsyncOpenAI

client = AsyncOpenAI(
    api_key=os.environ["OPENROUTER_API_KEY"],
    base_url="https://openrouter.ai/api/v1",
)


async def chat(message: str, model: str = "anthropic/claude-sonnet-4") -> str:
    response = await client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": message}],
        extra_headers={
            "HTTP-Referer": "https://your-app.example.com",
            "X-Title": "AI Engineering Playbook",
        },
    )
    return response.choices[0].message.content or ""


async def main() -> None:
    # Switch models without changing client code
    for model in ["openai/gpt-4o-mini", "anthropic/claude-sonnet-4"]:
        print(f"--- {model} ---")
        print(await chat("Say hello in one word.", model=model))


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
