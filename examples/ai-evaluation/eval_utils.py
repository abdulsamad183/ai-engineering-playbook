"""Shared evaluation helpers for playbook examples."""

from __future__ import annotations

import json
import statistics
import time
from dataclasses import dataclass, field
from typing import Callable


@dataclass
class EvalCase:
    id: str
    input: str
    expected: str | None = None
    context: list[str] = field(default_factory=list)
    metadata: dict = field(default_factory=dict)


@dataclass
class EvalResult:
    case_id: str
    output: str
    scores: dict[str, float]
    latency_ms: float


def exact_match(pred: str, gold: str) -> float:
    return 1.0 if pred.strip().lower() == gold.strip().lower() else 0.0


def contains_match(pred: str, gold: str) -> float:
    return 1.0 if gold.lower() in pred.lower() else 0.0


async def run_eval_suite(
    cases: list[EvalCase],
    system_fn: Callable,
    scorers: dict[str, Callable[[str, EvalCase], float]],
) -> list[EvalResult]:
    results: list[EvalResult] = []
    for case in cases:
        start = time.perf_counter()
        output = await system_fn(case.input)
        latency_ms = (time.perf_counter() - start) * 1000
        scores = {name: fn(output, case) for name, fn in scorers.items()}
        results.append(EvalResult(case.id, output, scores, latency_ms))
    return results


def aggregate_scores(results: list[EvalResult]) -> dict[str, float]:
    if not results:
        return {}
    keys = results[0].scores.keys()
    return {k: statistics.mean(r.scores[k] for r in results) for k in keys}


def load_jsonl(path: str) -> list[dict]:
    with open(path) as f:
        return [json.loads(line) for line in f if line.strip()]
