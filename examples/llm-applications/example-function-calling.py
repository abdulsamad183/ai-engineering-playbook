"""OpenAI function calling / tool use example.

Run: python example-function-calling.py
"""

from __future__ import annotations

import json
import os
from typing import Any

from openai import AsyncOpenAI

client = AsyncOpenAI(api_key=os.environ["OPENAI_API_KEY"])

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get current weather for a city",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {"type": "string"},
                    "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
                },
                "required": ["city"],
            },
        },
    }
]


def get_weather(city: str, unit: str = "celsius") -> dict[str, Any]:
    return {"city": city, "temperature": 22, "unit": unit, "condition": "sunny"}


TOOL_HANDLERS = {"get_weather": get_weather}


async def run_agent(user_message: str) -> str:
    messages = [{"role": "user", "content": user_message}]

    response = await client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        tools=TOOLS,
        tool_choice="auto",
    )
    msg = response.choices[0].message
    messages.append(msg.model_dump(exclude_none=True))

    if msg.tool_calls:
        for call in msg.tool_calls:
            args = json.loads(call.function.arguments)
            handler = TOOL_HANDLERS[call.function.name]
            result = handler(**args)
            messages.append({
                "role": "tool",
                "tool_call_id": call.id,
                "content": json.dumps(result),
            })

        final = await client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
        )
        return final.choices[0].message.content or ""

    return msg.content or ""


async def main() -> None:
    print(await run_agent("What's the weather in Tokyo?"))


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
