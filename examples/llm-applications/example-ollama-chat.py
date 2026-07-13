"""Ollama local inference via OpenAI-compatible API.

Prerequisites: ollama serve && ollama pull llama3.2

Run: python example-ollama-chat.py
"""

from __future__ import annotations

from openai import AsyncOpenAI

client = AsyncOpenAI(
    api_key="ollama",  # required but unused locally
    base_url="http://localhost:11434/v1",
)


async def chat(message: str, model: str = "llama3.2") -> str:
    response = await client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": message}],
        max_tokens=500,
    )
    return response.choices[0].message.content or ""


async def main() -> None:
    print(await chat("Explain local LLM inference benefits."))


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
