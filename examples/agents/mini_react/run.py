"""
Mini ReAct-style agent loop with mock tools (no API keys).

Run:
  python examples/agents/mini_react/run.py
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Step:
    thought: str
    action: str | None
    action_input: str | None
    observation: str | None = None


def calculator(expr: str) -> str:
    allowed = set("0123456789+-*/(). ")
    if not set(expr) <= allowed:
        return "error: invalid expression"
    try:
        return str(eval(expr, {"__builtins__": {}}, {}))  # noqa: S307 - sandbox limited
    except Exception as e:  # noqa: BLE001
        return f"error: {e}"


TOOLS = {
    "calculator": calculator,
}


def plan(question: str) -> list[Step]:
    # Deterministic toy planner for the demo
    if "2+2" in question.replace(" ", "") or "2 + 2" in question:
        return [
            Step("Need arithmetic", "calculator", "2+2"),
            Step("Have result; answer user", None, None),
        ]
    return [Step("No tool needed", None, None)]


def run_agent(question: str) -> str:
    steps = plan(question)
    last_obs = None
    for step in steps:
        if step.action and step.action in TOOLS:
            step.observation = TOOLS[step.action](step.action_input or "")
            last_obs = step.observation
            print(f"thought={step.thought} action={step.action}({step.action_input}) -> {step.observation}")
        else:
            print(f"thought={step.thought} (final)")
    if last_obs is not None:
        return f"Answer: {last_obs}"
    return f"Answer: I can only demo calculator tooling. You asked: {question}"


def main() -> None:
    for q in ["What is 2 + 2?", "Tell me a joke"]:
        print("Q:", q)
        print(run_agent(q))
        print("---")


if __name__ == "__main__":
    main()
