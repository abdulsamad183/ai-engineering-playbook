"""Token counting and cost estimation.

Prerequisites: pip install tiktoken

Run: python example-token-counting.py
"""

from __future__ import annotations

import tiktoken

# Pricing per 1M tokens (example — verify current rates)
PRICING = {
    "gpt-4o-mini": {"input": 0.15, "output": 0.60},
    "gpt-4o": {"input": 2.50, "output": 10.00},
}


def count_tokens(text: str, model: str = "gpt-4o-mini") -> int:
    try:
        encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        encoding = tiktoken.get_encoding("cl100k_base")
    return len(encoding.encode(text))


def estimate_cost(
    prompt: str,
    expected_output_tokens: int = 200,
    model: str = "gpt-4o-mini",
) -> dict:
    input_tokens = count_tokens(prompt, model)
    rates = PRICING.get(model, PRICING["gpt-4o-mini"])
    input_cost = (input_tokens / 1_000_000) * rates["input"]
    output_cost = (expected_output_tokens / 1_000_000) * rates["output"]
    return {
        "model": model,
        "input_tokens": input_tokens,
        "expected_output_tokens": expected_output_tokens,
        "estimated_cost_usd": round(input_cost + output_cost, 6),
    }


def main() -> None:
    prompt = "You are a helpful assistant. " * 50 + "Summarize this document."
    result = estimate_cost(prompt, expected_output_tokens=500, model="gpt-4o")
    print(f"Input tokens: {result['input_tokens']}")
    print(f"Estimated cost: ${result['estimated_cost_usd']}")


if __name__ == "__main__":
    main()
