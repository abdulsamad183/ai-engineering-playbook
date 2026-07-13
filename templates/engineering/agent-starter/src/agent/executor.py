"""Executor with retries and tracing hooks."""

import logging

from agent.state import AgentState
from agent.tools import ToolRegistry
import asyncio
from collections.abc import Awaitable, Callable
from typing import TypeVar

T = TypeVar("T")


async def with_retry(fn: Callable[[], Awaitable[T]], *, max_attempts: int = 3) -> T:
    last: Exception | None = None
    for attempt in range(max_attempts):
        try:
            return await fn()
        except Exception as exc:
            last = exc
            if attempt == max_attempts - 1:
                break
            await asyncio.sleep(0.5 * (2**attempt))
    raise last  # type: ignore[misc]

logger = logging.getLogger(__name__)


class Executor:
    def __init__(self, tools: ToolRegistry) -> None:
        self.tools = tools

    async def run_step(self, state: AgentState) -> str:
        if state.step >= len(state.plan):
            return "done"

        step = state.plan[state.step]

        async def _act() -> str:
            if step.startswith("Execute"):
                return str(self.tools.run("echo", message=state.goal))
            return f"completed: {step}"

        result = await with_retry(_act, max_attempts=3)
        state.observations.append(result)
        state.step += 1
        logger.info("agent_step", extra={"step": state.step, "result": result})
        return result
