"""Prompt evaluation template."""

from dataclasses import dataclass


@dataclass
class PromptEvalCase:
    input: str
    must_include: list[str]


def evaluate_output(output: str, case: PromptEvalCase) -> float:
    return sum(1 for s in case.must_include if s in output) / max(1, len(case.must_include))
