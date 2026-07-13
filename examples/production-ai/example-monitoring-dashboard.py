"""Monitoring metrics aggregation for dashboards.

Run: python example-monitoring-dashboard.py
"""

from collections import defaultdict
from statistics import mean


def aggregate_metrics(events: list[dict]) -> dict:
    by_route: dict[str, list[float]] = defaultdict(list)
    errors = 0
    for e in events:
        by_route[e["route"]].append(e["latency_ms"])
        if e.get("status", 200) >= 500:
            errors += 1
    return {
        "routes": {r: {"p50": mean(v), "count": len(v)} for r, v in by_route.items()},
        "error_rate": errors / max(len(events), 1),
    }


if __name__ == "__main__":
    sample = [
        {"route": "/chat", "latency_ms": 400, "status": 200},
        {"route": "/chat", "latency_ms": 1200, "status": 200},
        {"route": "/rag", "latency_ms": 800, "status": 500},
    ]
    print(aggregate_metrics(sample))
