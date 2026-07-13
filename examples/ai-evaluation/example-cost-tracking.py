"""Cost tracking per request.

Run: python example-cost-tracking.py
"""

from dataclasses import dataclass


@dataclass
class Usage:
    input_tokens: int
    output_tokens: int
    embed_calls: int = 0
    tool_calls: int = 0


def compute_cost(u: Usage, price_in: float = 3.0, price_out: float = 15.0, embed: float = 0.02) -> dict:
    llm = (u.input_tokens * price_in + u.output_tokens * price_out) / 1_000_000
    embedding = u.embed_calls * embed / 1000
    tools = u.tool_calls * 0.001
    total = llm + embedding + tools
    return {"llm_usd": llm, "embed_usd": embedding, "tools_usd": tools, "total_usd": total}


def main() -> None:
    u = Usage(input_tokens=1200, output_tokens=400, embed_calls=2, tool_calls=1)
    print(compute_cost(u))


if __name__ == "__main__":
    main()
