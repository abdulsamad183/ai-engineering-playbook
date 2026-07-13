"""Anthropic Claude API example with tool use.

Environment: ANTHROPIC_API_KEY=sk-ant-...

Run: python example-anthropic-chat.py
"""

from __future__ import annotations

import os

from anthropic import AsyncAnthropic

client = AsyncAnthropic(api_key=os.environ["ANTHROPIC_API_KEY"])


async def chat(message: str, model: str = "claude-sonnet-4-20250514") -> str:
    response = await client.messages.create(
        model=model,
        max_tokens=1024,
        messages=[{"role": "user", "content": message}],
    )
    return response.content[0].text


async def main() -> None:
    answer = await chat("Explain tool use in Claude in two sentences.")
    print(answer)


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
