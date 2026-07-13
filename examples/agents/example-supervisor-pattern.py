"""Supervisor multi-agent pattern — delegate to workers.

Run: python example-supervisor-pattern.py
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class WorkerResult:
    agent: str
    output: str


async def supervisor_run(task: str, workers: dict[str, callable]) -> str:
    plan = ["researcher", "writer"]  # from LLM planner in production
    results: list[WorkerResult] = []
    context = task
    for name in plan:
        out = await workers[name](context, results)
        results.append(WorkerResult(name, out))
        context = f"{context}\n\n{name} said:\n{out}"
    return results[-1].output


async def researcher(ctx: str, _: list) -> str:
    return "Found: refund SLA is 3 business days."


async def writer(ctx: str, prior: list) -> str:
    return f"Draft reply based on research: {prior[0].output if prior else ctx}"


if __name__ == "__main__":
    import asyncio
    print(asyncio.run(supervisor_run("Answer refund question", {"researcher": researcher, "writer": writer})))
