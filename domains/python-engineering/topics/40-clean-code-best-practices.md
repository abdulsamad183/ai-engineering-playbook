---
title: "Clean Code & Python Best Practices"
description: "Write Python that teams can trust — naming, structure, errors, typing, tooling, and production habits."
domain: python-engineering
tags: [python, clean-code, best-practices, tutorial]
status: published
created: 2026-08-11
updated: 2026-08-12
version: "1.1"
---

# Clean Code & Python Best Practices

> Write Python that teams can trust — naming, structure, errors, typing, tooling, and production habits.

## Definition

**Clean code** is software that is easy to read, change, test, and operate. In Python, that means idiomatic style (PEP 8), clear boundaries, intentional dependencies, and automation (format/lint/type/test).

## Uses

- Keep AI codebases maintainable as prompts/tools grow
- Onboard teammates quickly
- Reduce production incidents from “clever” code

## Principles

| Principle | Practice |
|-----------|----------|
| Clarity over cleverness | Obvious > cute |
| Small units | Functions/classes with one job |
| Explicit boundaries | Validate at I/O edges |
| Fail fast | Clear exceptions |
| Consistency | Formatter + linter |
| Testability | Pure cores, thin adapters |
| Observability | Structured logs/traces |

## Style & tooling

```bash
ruff check .
ruff format .
pyright
pytest -q
```

```python
user_id = "u1"                 # snake_case
MAX_TOKENS = 512                # constants
class RetrievalService:
    pass                        # CapWords
```

## Project habits

```text
src/myapp/...           # package code
tests/...               # tests mirror packages
pyproject.toml          # deps + tool config
README.md               # how to run
```

## Code examples (before → after)

```python
# Before: vague + side effects
def process(d):
    d["s"] = d.get("s") or 0
    print(d)
    return d

# After: explicit
from dataclasses import dataclass

@dataclass
class Row:
    score: float

def normalize_row(row: Row) -> Row:
    score = 0.0 if row.score is None else row.score
    return Row(score=score)
```

```python
from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    message: str = Field(min_length=1, max_length=8000)
    temperature: float = Field(default=0.2, ge=0, le=2)
```

## Production checklist

- [ ] Venv + locked deps
- [ ] Typecheck public APIs
- [ ] Tests for core logic + CI
- [ ] Logging with request IDs; secrets redacted
- [ ] Timeouts/retries with budgets
- [ ] No unbounded caches
- [ ] Clear module boundaries (api / domain / adapters)

## Pythonic tips

1. Prefer `with` for resources
2. Prefer comprehensions for simple maps/filters
3. Use `pathlib` for paths
4. EAFP with specific exceptions when idiomatic
5. Don’t fight the stdlib — know it first

## Anti-patterns

- Catch-all `except:` swallowing bugs
- Global mutable config mutated everywhere
- Copy-pasted prompt strings with no versioning
- Mega-functions doing orchestration + I/O + parsing

## Related deep dive

For AI-service oriented patterns (async, uv, Pydantic, project layouts), continue with [Python for AI Engineering](../python-for-ai-engineering.md).

---

## Continue

- **Previous:** [Performance Optimization](39-performance-optimization.md)
- **Hub:** [Python topics](../README.md)
- **AI production guide:** [Python for AI Engineering](../python-for-ai-engineering.md)

---

## AI engineering angle

This topic shows up constantly in AI codebases: training scripts, eval runners, FastAPI services, agent tools, and data cleanup jobs. Prefer clear `main()` entrypoints, typed interfaces, and small testable functions over notebook-only workflows.

## Production checklist

- [ ] Errors are explicit (no bare `except:`)
- [ ] Logging instead of leftover `print` in services
- [ ] Deterministic seeds where experiments need reproduction
- [ ] Resource cleanup via `with` / context managers
- [ ] Unit tests for pure helpers

## Practice exercises

1. Rewrite one snippet from this page as a function with type hints and a docstring.
2. Add a failing unit test, then make it pass.
3. Note one way this concept appears in RAG, agents, or LLM API clients.

## Interview prompts

**Q: When would you choose a different approach than the default shown here?**

A: Tie the answer to performance, readability, concurrency, or API boundaries — and give a concrete AI-engineering example (streaming responses, batch embedding, tool sandboxing).

## See also

- [Python hub](../README.md)
- [Python Frameworks](../../python-frameworks-libraries/README.md)
- [LLM Application Development](../../llm-application-development/README.md)

