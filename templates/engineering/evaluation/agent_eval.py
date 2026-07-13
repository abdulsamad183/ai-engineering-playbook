"""Agent evaluation — task success and step efficiency."""

from dataclasses import dataclass


@dataclass
class AgentEvalCase:
    goal: str
    success_criteria: list[str]
    steps_taken: int
    max_steps: int


def agent_score(case: AgentEvalCase, output: str) -> dict[str, float]:
    success = sum(1 for c in case.success_criteria if c.lower() in output.lower()) / max(
        1, len(case.success_criteria)
    )
    efficiency = 1.0 - min(1.0, case.steps_taken / max(1, case.max_steps))
    return {"success": success, "efficiency": efficiency}
