"""A/B testing assignment and metric aggregation.

Run: python example-ab-testing.py
"""

import hashlib
import random
from collections import defaultdict


def assign_variant(user_id: str, experiment: str, treatment_pct: int = 50) -> str:
    h = int(hashlib.sha256(f"{experiment}:{user_id}".encode()).hexdigest(), 16)
    return "treatment" if h % 100 < treatment_pct else "control"


def aggregate_ab(results: list[dict]) -> dict:
    buckets: dict[str, list[float]] = defaultdict(list)
    for r in results:
        buckets[r["variant"]].append(r["success"])
    return {v: sum(s) / len(s) for v, s in buckets.items()}


def main() -> None:
    random.seed(0)
    results = []
    for i in range(1000):
        v = assign_variant(f"user-{i}", "prompt-v2")
        success = random.random() < (0.62 if v == "treatment" else 0.55)
        results.append({"variant": v, "success": float(success)})
    print("conversion rates:", aggregate_ab(results))


if __name__ == "__main__":
    main()
