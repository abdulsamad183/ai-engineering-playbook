"""
Tiny generative demo: sample tokens from a toy categorical distribution.

Run:
  python examples/generative-ai/mini_sample.py
"""
from __future__ import annotations

import random


def sample_next(probs: dict[str, float], temperature: float = 1.0) -> str:
    items = list(probs.items())
    tokens, weights = zip(*items)
    if temperature <= 0:
        return max(items, key=lambda kv: kv[1])[0]
    scaled = [w ** (1.0 / temperature) for w in weights]
    total = sum(scaled) or 1.0
    scaled = [w / total for w in scaled]
    return random.choices(list(tokens), weights=scaled, k=1)[0]


def main() -> None:
    probs = {"hello": 0.5, "hi": 0.3, "hey": 0.2}
    random.seed(0)
    print([sample_next(probs, temperature=0.8) for _ in range(8)])


if __name__ == "__main__":
    main()
