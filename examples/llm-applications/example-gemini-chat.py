"""Google Gemini API example.

Environment: GOOGLE_API_KEY=...

Run: pip install google-genai && python example-gemini-chat.py
"""

from __future__ import annotations

import os

from google import genai

client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])


async def chat(message: str, model: str = "gemini-2.0-flash") -> str:
    response = await client.aio.models.generate_content(
        model=model,
        contents=message,
    )
    return response.text or ""


async def main() -> None:
    answer = await chat("What is a context window?")
    print(answer)


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
