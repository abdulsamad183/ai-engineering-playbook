"""Conversation memory — short-term session facts + long-term semantic recall.

Run: python example-conversation-memory.py
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass
class SessionMemory:
    session_id: str
    facts: list[str] = field(default_factory=list)

    def add(self, fact: str) -> None:
        if fact not in self.facts:
            self.facts.append(fact)

    def to_context(self) -> str:
        if not self.facts:
            return ""
        lines = "\n".join(f"- {f}" for f in self.facts)
        return f"<session_memory>\n{lines}\n</session_memory>"


@dataclass
class SemanticMemory:
    user_id: str
    records: list[tuple[str, float]] = field(default_factory=list)

    def recall(self, query: str, top_k: int = 3) -> list[str]:
        # Production: vector similarity. Demo: keyword overlap.
        scored = [
            (text, conf)
            for text, conf in self.records
            if any(word in text.lower() for word in query.lower().split())
        ]
        scored.sort(key=lambda x: -x[1])
        return [t for t, _ in scored[:top_k]]

    def write(self, text: str, confidence: float = 0.8) -> None:
        self.records.append((text, confidence))


if __name__ == "__main__":
    session = SessionMemory("sess-1")
    session.add("User invoice number is 8842")
    long_term = SemanticMemory("user-42")
    long_term.write("User prefers concise answers", 0.9)

    query = "concise refund for invoice"
    print(session.to_context())
    print("Recalled:", long_term.recall(query))
