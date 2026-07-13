"""Single-agent ReAct loop — minimal production pattern.

Run: python example-single-agent-react.py
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class ReActState:
    goal: str
    thoughts: list[str] = field(default_factory=list)
    observations: list[str] = field(default_factory=list)
    finished: bool = False
    answer: str = ""


async def react_loop(goal: str, llm, tools: dict, max_steps: int = 10) -> ReActState:
    state = ReActState(goal=goal)
    for _ in range(max_steps):
        decision = await llm.decide(state, tools)
        if decision["type"] == "finish":
            state.finished = True
            state.answer = decision["answer"]
            break
        tool = tools[decision["tool"]]
        obs = await tool(**decision.get("args", {}))
        state.thoughts.append(decision.get("thought", ""))
        state.observations.append(str(obs))
    return state


class MockLLM:
    async def decide(self, state: ReActState, tools: dict) -> dict:
        if not state.observations:
            return {"type": "act", "tool": "search_kb", "args": {"q": state.goal}, "thought": "Need policy"}
        return {"type": "finish", "answer": "Refunds in 3 business days per KB."}


async def search_kb(q: str) -> str:
    return "Refund policy: 3 business days."


if __name__ == "__main__":
    import asyncio
    result = asyncio.run(react_loop("refund time?", MockLLM(), {"search_kb": search_kb}))
    print(result.answer)
