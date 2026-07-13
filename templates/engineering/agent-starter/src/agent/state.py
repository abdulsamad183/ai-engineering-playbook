"""Agent state and checkpointing."""

from dataclasses import dataclass, field
from typing import Any


@dataclass
class AgentState:
    goal: str
    plan: list[str] = field(default_factory=list)
    observations: list[str] = field(default_factory=list)
    messages: list[dict[str, Any]] = field(default_factory=list)
    step: int = 0

    def checkpoint(self) -> dict[str, Any]:
        return {
            "goal": self.goal,
            "plan": self.plan,
            "observations": self.observations,
            "messages": self.messages,
            "step": self.step,
        }

    @classmethod
    def restore(cls, data: dict[str, Any]) -> "AgentState":
        return cls(**data)
