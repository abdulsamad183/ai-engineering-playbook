# Shared Utilities

> Copy-paste modules for retry, config, logging, tokens, and cost tracking.

---

## Purpose

Cross-cutting helpers used by FastAPI, RAG, and agent starters. Copy `playbook_utils/` into your project or install as a local package.

---

## Modules

| Module | Function |
|--------|----------|
| `config.py` | Pydantic `BaseSettings` pattern |
| `retry.py` | Async exponential backoff |
| `logging.py` | JSON structured events |
| `tokens.py` | Rough token estimation |
| `cost.py` | Per-request cost tracker |
| `prompts.py` | Load parameterized prompt files |

---

## Usage

```python
from playbook_utils import with_retry, CostTracker, estimate_tokens

tracker = CostTracker()
tracker.record(estimate_tokens(prompt), estimate_tokens(response))
```

---

## Extension Points

Add `caching.py`, `streaming.py`, and `api_wrappers.py` following the same patterns.

---

## Related Templates

- [Logging](../logging/README.md)
- [Evaluation](../evaluation/README.md)
