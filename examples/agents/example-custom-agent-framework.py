"""Custom minimal agent framework — see build-your-own-agent-framework.md.

Run: python example-custom-agent-framework.py
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class RunContext:
    goal: str
    observations: list[str] = field(default_factory=list)
    step: int = 0


class SimplePlanner:
    async def next_action(self, ctx: RunContext) -> dict:
        if ctx.observations:
            return {"type": "finish", "result": ctx.observations[-1]}
        return {"type": "act", "tool": "echo", "args": {"msg": ctx.goal}}


class ToolRegistry:
    async def echo(self, msg: str) -> str:
        return f"echo: {msg}"


class MiniFramework:
    def __init__(self, planner, tools: ToolRegistry, max_steps: int = 5):
        self.planner = planner
        self.tools = tools
        self.max_steps = max_steps

    async def run(self, goal: str) -> str:
        ctx = RunContext(goal=goal)
        while ctx.step < self.max_steps:
            action = await self.planner.next_action(ctx)
            if action["type"] == "finish":
                return action["result"]
            fn = getattr(self.tools, action["tool"])
            ctx.observations.append(await fn(**action["args"]))
            ctx.step += 1
        raise TimeoutError("max steps")


if __name__ == "__main__":
    import asyncio
    fw = MiniFramework(SimplePlanner(), ToolRegistry())
    print(asyncio.run(fw.run("hello agent")))
