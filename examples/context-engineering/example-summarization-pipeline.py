"""Summarization pipeline — rolling history compression.

Run: python example-summarization-pipeline.py
"""

from __future__ import annotations


def summarize_turns(turns: list[dict[str, str]], max_chars: int = 500) -> str:
    """Demo: extractive join. Production: LLM with faithfulness prompt."""
    lines = []
    for t in turns:
        prefix = "User" if t["role"] == "user" else "Assistant"
        lines.append(f"{prefix}: {t['content'][:120]}")
    text = "\n".join(lines)
    return text[:max_chars]


def build_history(turns: list[dict], keep_recent: int = 4) -> tuple[str, list[dict]]:
    if len(turns) <= keep_recent:
        return "", turns
    older = turns[:-keep_recent]
    recent = turns[-keep_recent:]
    summary = summarize_turns(older)
    return summary, recent


if __name__ == "__main__":
    turns = [{"role": "user", "content": f"Message {i}"} for i in range(10)]
    summary, recent = build_history(turns)
    print("Summary chars:", len(summary), "Recent turns:", len(recent))
