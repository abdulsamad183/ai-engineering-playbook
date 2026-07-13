"""LangFuse-style trace record (conceptual — use langfuse SDK in production).

Run: python example-langfuse-integration.py
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass
class Trace:
    name: str
    user_id: str
    metadata: dict = field(default_factory=dict)
    observations: list = field(default_factory=list)

    def generation(self, name: str, model: str, input_tokens: int, output_tokens: int, latency_ms: float):
        self.observations.append({
            "type": "generation",
            "name": name,
            "model": model,
            "input_tokens": input_tokens,
            "output_tokens": output_tokens,
            "latency_ms": latency_ms,
            "ts": datetime.now(timezone.utc).isoformat(),
        })

    def flush(self) -> dict:
        return {"trace": self.name, "observations": self.observations}


def main() -> None:
    trace = Trace(name="chat-turn", user_id="u-1", metadata={"prompt_version": "v3"})
    trace.generation("answer", "gpt-4", 800, 120, 950)
    print(trace.flush())


if __name__ == "__main__":
    main()
