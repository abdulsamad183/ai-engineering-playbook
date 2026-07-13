"""Planner — decompose goals into steps."""

from agent.state import AgentState


class Planner:
    def plan(self, state: AgentState) -> list[str]:
        return [f"Research: {state.goal}", f"Execute: {state.goal}", "Verify result"]
