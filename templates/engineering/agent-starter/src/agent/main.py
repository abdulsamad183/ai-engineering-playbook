import asyncio

from agent.executor import Executor
from agent.memory import Memory
from agent.planner import Planner
from agent.state import AgentState
from agent.tools import ToolRegistry


async def run_agent(goal: str) -> AgentState:
    state = AgentState(goal=goal)
    planner = Planner()
    tools = ToolRegistry()
    tools.register("echo", lambda message: f"echo:{message}")
    executor = Executor(tools)
    memory = Memory()

    state.plan = planner.plan(state)
    while state.step < len(state.plan):
        result = await executor.run_step(state)
        memory.add(result)
    return state


if __name__ == "__main__":
    final = asyncio.run(run_agent("Summarize quarterly metrics"))
    print(final.checkpoint())
