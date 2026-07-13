"""Few-shot classification with structured prompt.

Run: python example-few-shot-classification.py
"""

from __future__ import annotations

FEW_SHOT_CLASSIFICATION = {
    "system": """You classify support tickets into categories.
Categories: billing, technical, account, other
Respond with JSON only: {"category": "...", "confidence": 0.0-1.0}""",
    "examples": [
        {"input": "I was charged twice this month", "output": '{"category": "billing", "confidence": 0.95}'},
        {"input": "API returns 500 on /v1/chat", "output": '{"category": "technical", "confidence": 0.98}'},
        {"input": "How do I change my email?", "output": '{"category": "account", "confidence": 0.92}'},
    ],
}


def build_messages(ticket: str) -> list[dict]:
    messages = [{"role": "system", "content": FEW_SHOT_CLASSIFICATION["system"]}]

    for ex in FEW_SHOT_CLASSIFICATION["examples"]:
        messages.append({"role": "user", "content": ex["input"]})
        messages.append({"role": "assistant", "content": ex["output"]})

    messages.append({"role": "user", "content": ticket})
    return messages


def main() -> None:
    ticket = "The streaming endpoint disconnects after 30 seconds"
    messages = build_messages(ticket)
    print(f"Message count: {len(messages)}")
    for m in messages:
        print(f"  [{m['role']}] {m['content'][:60]}...")


if __name__ == "__main__":
    main()
