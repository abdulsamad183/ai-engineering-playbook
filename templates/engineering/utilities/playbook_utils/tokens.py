"""Rough token estimation (4 chars ≈ 1 token for English)."""


def estimate_tokens(text: str) -> int:
    return max(1, len(text) // 4)
