# Monitoring Template

> OpenTelemetry, LangFuse, and Phoenix integration hooks.

---

## Purpose

Observability scaffolding: trace spans, LLM tracing backends, unified health payload.

---

## Usage

```python
from observability import trace_span, init_langfuse, health_payload

with trace_span("rag_query"):
    ...
print(health_payload())
```

Wire real SDKs by uncommenting imports in `observability.py`.

---

## Related

- [AI Evaluation Observability](../../../domains/ai-evaluation/continuous-evaluation.md)
- [LangSmith / Phoenix guides](../../../domains/ai-evaluation/)
