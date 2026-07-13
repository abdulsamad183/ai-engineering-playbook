"""Conversation pruning — importance-aware history trimming.

Run: python example-conversation-pruning.py
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Turn:
    role: str
    content: str
    tokens: int
    importance: float


def prune_history(turns: list[Turn], token_budget: int, min_recent: int = 4) -> list[Turn]:
    if sum(t.tokens for t in turns) <= token_budget:
        return turns

    recent = turns[-min_recent:]
    older = turns[:-min_recent]
    older_sorted = sorted(older, key=lambda t: -t.importance)

    selected_old: list[Turn] = []
    used = sum(t.tokens for t in recent)
    for t in older_sorted:
        if used + t.tokens <= token_budget:
            selected_old.append(t)
            used += t.tokens

    return sorted(selected_old + recent, key=lambda t: turns.index(t))


if __name__ == "__main__":
    turns = [
        Turn("user", "hi", 5, 0.1),
        Turn("assistant", "hello", 5, 0.1),
        Turn("user", "billing issue invoice 8842", 12, 0.95),
        Turn("assistant", "checking", 8, 0.3),
        Turn("user", "need refund", 6, 0.9),
    ]
    pruned = prune_history(turns, token_budget=25, min_recent=2)
    print([t.content for t in pruned])
