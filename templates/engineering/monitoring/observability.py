"""OpenTelemetry, LangFuse, and Phoenix hooks."""

from contextlib import contextmanager
from typing import Iterator


@contextmanager
def trace_span(name: str) -> Iterator[None]:
    # Wire opentelemetry.trace.get_tracer(__name__).start_as_current_span(name)
    yield


def init_langfuse() -> None:
  pass  # from langfuse import Langfuse; Langfuse()


def init_phoenix() -> None:
  pass  # import phoenix as px; px.launch_app()


def health_payload() -> dict[str, str]:
    return {"status": "ok", "otel": "disabled", "langfuse": "disabled", "phoenix": "disabled"}
