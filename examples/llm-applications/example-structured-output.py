"""Structured JSON output with OpenAI and Pydantic validation.

Run: python example-structured-output.py
"""

from __future__ import annotations

import json
import os

from openai import AsyncOpenAI
from pydantic import BaseModel, Field

client = AsyncOpenAI(api_key=os.environ["OPENAI_API_KEY"])


class SentimentResult(BaseModel):
    sentiment: str = Field(description="positive, negative, or neutral")
    confidence: float = Field(ge=0.0, le=1.0)
    summary: str


async def analyze_sentiment(text: str) -> SentimentResult:
    response = await client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "Analyze sentiment. Respond with JSON matching the schema.",
            },
            {"role": "user", "content": text},
        ],
        response_format={"type": "json_object"},
        temperature=0.0,
    )
    raw = response.choices[0].message.content or "{}"
    return SentimentResult.model_validate(json.loads(raw))


async def main() -> None:
    result = await analyze_sentiment("The deployment went smoothly despite one minor rollback.")
    print(result.model_dump_json(indent=2))


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
