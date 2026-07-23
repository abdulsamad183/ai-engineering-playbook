import asyncio

from agent.main import run_agent
from agent.planner import Planner
from agent.state import AgentState
from agent.tools import ToolRegistry


def test_planner_produces_plan():
    planner = Planner()
    state = AgentState(goal="Summarize metrics")
    plan = planner.plan(state)
    assert isinstance(plan, list)
    assert len(plan) > 0
    assert all(isinstance(step, str) and step for step in plan)


def test_tool_registry_register_and_run():
    registry = ToolRegistry()
    registry.register("echo", lambda message: f"echo:{message}")
    assert registry.run("echo", message="hello") == "echo:hello"


def test_run_agent_completes():
    state = asyncio.run(run_agent("Summarize quarterly metrics"))
    assert state.goal == "Summarize quarterly metrics"
    assert len(state.plan) > 0
    assert state.step == len(state.plan)
    assert len(state.observations) == len(state.plan)
