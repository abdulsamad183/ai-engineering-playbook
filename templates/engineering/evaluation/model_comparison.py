"""Model comparison and cost analysis."""

import time
from dataclasses import dataclass


@dataclass
class ModelResult:
    model: str
    latency_ms: float
    input_tokens: int
    output_tokens: int
    cost_usd: float


def benchmark(fn, *, model: str, price_in: float, price_out: float) -> ModelResult:
    start = time.perf_counter()
    input_tokens, output_tokens = fn()
    latency_ms = (time.perf_counter() - start) * 1000
    cost = (input_tokens * price_in + output_tokens * price_out) / 1_000_000
    return ModelResult(model, latency_ms, input_tokens, output_tokens, cost)
