"""Tool-using agent with registry and validation.

Run: python example-tool-agent.py
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Any


@dataclass
class ToolSpec:
    name: str
    fn: Callable
    schema: dict


class ToolRegistry:
    def __init__(self) -> None:
        self._tools: dict[str, ToolSpec] = {}

    def register(self, name: str, fn: Callable, schema: dict) -> None:
        self._tools[name] = ToolSpec(name, fn, schema)

    async def call(self, name: str, args: dict) -> Any:
        if name not in self._tools:
            raise ValueError(f"Unknown tool: {name}")
        return await self._tools[name].fn(**args)


async def get_weather(city: str) -> str:
    return f"Weather in {city}: 72F sunny"


if __name__ == "__main__":
    import asyncio
    reg = ToolRegistry()
    reg.register("get_weather", get_weather, {"city": "string"})
    print(asyncio.run(reg.call("get_weather", {"city": "NYC"})))
