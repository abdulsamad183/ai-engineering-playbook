"""Token budgeting — layer caps and enforcement.

Run: python example-token-budgeting.py
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class TokenBudget:
    total: int
    reserved_output: int
    system: int
    retrieval: int
    history: int
    user: int

    @property
    def input_available(self) -> int:
        return self.total - self.reserved_output


def enforce_layer_cap(items: list[tuple[str, int]], cap: int) -> list[tuple[str, int]]:
    """Keep items in order until cap reached."""
    out: list[tuple[str, int]] = []
    used = 0
    for item_id, tokens in items:
        if used + tokens > cap:
            break
        out.append((item_id, tokens))
        used += tokens
    return out


if __name__ == "__main__":
    budget = TokenBudget(total=8000, reserved_output=2000, system=600, retrieval=2500, history=1800, user=400)
    retrieval = [("doc-1", 900), ("doc-2", 800), ("doc-3", 1200)]
    kept = enforce_layer_cap(retrieval, budget.retrieval)
    print("Input available:", budget.input_available)
    print("Retrieval kept:", kept)
