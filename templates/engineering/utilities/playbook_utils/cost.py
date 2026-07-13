"""Per-request LLM cost tracking."""

from dataclasses import dataclass, field


@dataclass
class CostTracker:
    price_in_per_m: float = 3.0
    price_out_per_m: float = 15.0
    input_tokens: int = 0
    output_tokens: int = 0

    def record(self, input_tokens: int, output_tokens: int) -> float:
        self.input_tokens += input_tokens
        self.output_tokens += output_tokens
        return (
            input_tokens * self.price_in_per_m + output_tokens * self.price_out_per_m
        ) / 1_000_000

    @property
    def total_usd(self) -> float:
        return (
            self.input_tokens * self.price_in_per_m
            + self.output_tokens * self.price_out_per_m
        ) / 1_000_000
