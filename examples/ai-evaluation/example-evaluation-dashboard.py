"""Evaluation dashboard data aggregation.

Run: python example-evaluation-dashboard.py
"""

from collections import defaultdict
from datetime import datetime


def build_dashboard_rows(runs: list[dict]) -> dict:
    by_day: dict[str, list[float]] = defaultdict(list)
    for run in runs:
        day = run["timestamp"][:10]
        by_day[day].append(run["faithfulness"])
    return {
        "daily_avg_faithfulness": {d: sum(v) / len(v) for d, v in sorted(by_day.items())},
        "latest": runs[-1] if runs else {},
    }


def main() -> None:
    runs = [
        {"timestamp": "2026-07-10T12:00:00", "faithfulness": 0.82, "latency_p95_ms": 2100},
        {"timestamp": "2026-07-11T12:00:00", "faithfulness": 0.79, "latency_p95_ms": 2300},
        {"timestamp": "2026-07-12T12:00:00", "faithfulness": 0.85, "latency_p95_ms": 1900},
    ]
    print(build_dashboard_rows(runs))


if __name__ == "__main__":
    main()
