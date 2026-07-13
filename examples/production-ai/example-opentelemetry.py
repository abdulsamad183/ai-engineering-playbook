"""OpenTelemetry tracing pattern (minimal — install opentelemetry-api for full setup).

Run: python example-opentelemetry.py
"""

from contextlib import contextmanager
from dataclasses import dataclass, field
import time


@dataclass
class Span:
    name: str
    attributes: dict = field(default_factory=dict)
    children: list = field(default_factory=list)
    start: float = field(default_factory=time.perf_counter)
    end: float | None = None

    def finish(self) -> None:
        self.end = time.perf_counter()


@contextmanager
def trace_span(root: Span, name: str, **attrs):
    span = Span(name=name, attributes=attrs)
    root.children.append(span)
    try:
        yield span
    finally:
        span.finish()


async def fake_llm(prompt: str) -> str:
    return f"answer:{len(prompt)}"


async def rag_query(query: str) -> str:
    root = Span("rag.request", {"query_len": len(query)})
    with trace_span(root, "retrieval", top_k=5):
        await _sleep(0.05)
    with trace_span(root, "llm.completion", model="gpt-4"):
        result = await fake_llm(query)
    root.finish()
    return result


async def _sleep(s: float) -> None:
    import asyncio
    await asyncio.sleep(s)


if __name__ == "__main__":
    import asyncio
    asyncio.run(rag_query("refund policy"))
