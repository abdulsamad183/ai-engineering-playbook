---
title: "Debugging"
description: "Find and fix bugs systematically — prints, logging, pdb/breakpoint, bisecting, and AI-era failure modes."
domain: python-engineering
tags: [python, debugging, tutorial]
status: published
created: 2026-08-11
updated: 2026-08-12
version: "1.1"
---

# Debugging

> Find and fix bugs systematically — prints, logging, pdb/breakpoint, bisecting, and AI-era failure modes.

## Definition

**Debugging** is the disciplined process of forming hypotheses about incorrect behavior, gathering evidence, and applying a minimal fix. Tools help, but process matters more.

## Uses

- Fix crashes and wrong outputs
- Diagnose flaky tests
- Understand production incidents from logs/traces

## Techniques

| Technique | When |
|-----------|------|
| Reproduce minimally | Always first |
| `print` / log values | Quick checks |
| `breakpoint()` / pdb | Interactive |
| Bisect / binary search | Regressions |
| Git bisect | When introduced? |
| Divide & conquer | Isolate layer |

```mermaid
flowchart TB
  R[Reproduce] --> H[Hypothesis]
  H --> E[Evidence]
  E --> F[Fix]
  F --> V[Verify + regression test]
```

## Code examples

```python
def score(xs: list[float]) -> float:
    print("DEBUG xs=", xs)          # temporary
    return sum(xs) / len(xs)
```

```python
def normalize(scores):
    breakpoint()                    # drops into debugger
    total = sum(scores)
    return [s / total for s in scores]

# pdb commands: n (next), s (step), c (continue), p expr, l, q
```

```python
def chunk(text: str, size: int) -> list[str]:
    assert size > 0, "size must be positive"
    return [text[i:i+size] for i in range(0, len(text), size)]
```

```python
import traceback
try:
    1 / 0
except Exception:
    traceback.print_exc()
```

## AI-specific debugging

| Symptom | Likely layer |
|---------|--------------|
| Wrong facts | Retrieval / grounding |
| Weird format | Prompt / schema validation |
| Timeouts | Provider / async blocking |
| Flaky answers | Temperature / non-determinism |
| Tool failures | Authz / args validation |

## Common mistakes

- Changing many things at once
- Fixing without a regression test
- Ignoring the first exception in a chain

---

## Continue

- **Previous:** [Unit Testing](31-unit-testing.md)
- **Hub:** [Python topics](../README.md)
- **Next:** [Concurrency](33-concurrency.md)
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

