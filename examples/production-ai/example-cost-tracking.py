"""Production cost tracking per request.

Run: python example-cost-tracking.py
"""

from dataclasses import dataclass, field


@dataclass
class CostTracker:
    price_in_per_m: float = 3.0
    price_out_per_m: float = 15.0
    totals: dict = field(default_factory=lambda: {"input_tokens": 0, "output_tokens": 0, "usd": 0.0})

    def record(self, input_tokens: int, output_tokens: int) -> float:
        usd = (input_tokens * self.price_in_per_m + output_tokens * self.price_out_per_m) / 1_000_000
        self.totals["input_tokens"] += input_tokens
        self.totals["output_tokens"] += output_tokens
        self.totals["usd"] += usd
        return usd


if __name__ == "__main__":
    t = CostTracker()
    t.record(1200, 300)
    t.record(800, 150)
    print(t.totals)
