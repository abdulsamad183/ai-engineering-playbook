---
title: "Exception Handling"
description: "Errors as objects — try/except/else/finally, raising, custom exceptions, and robust failure handling."
domain: python-engineering
tags: [python, exceptions, error-handling, tutorial]
status: published
created: 2026-08-11
updated: 2026-08-12
version: "1.1"
---

# Exception Handling

> Errors as objects — try/except/else/finally, raising, custom exceptions, and robust failure handling.

## Definition

An **exception** signals that something abnormal occurred. Python uses an exception hierarchy rooted at `BaseException` (you almost always catch `Exception`, not `BaseException`).

**Exception handling** means catching, enriching, converting, or propagating those errors deliberately.

## Uses

- Validate inputs and fail with clear messages
- Retry transient network errors
- Ensure files/locks close via `finally` / context managers
- Translate low-level errors into domain errors

## Key forms

| Construct | Role |
|-----------|------|
| `try` | Protected block |
| `except` | Handle specific errors |
| `else` | Runs if no exception |
| `finally` | Always runs |
| `raise` | Throw / rethrow |
| `raise X from e` | Chain causes |

```mermaid
flowchart TD
  T[try] -->|error| X[except match?]
  X -->|yes| H[handler]
  X -->|no| P[propagate]
  T -->|ok| E[else]
  H --> F[finally]
  E --> F
  P --> F
```

## Code examples

```python
def parse_int(text: str) -> int:
    try:
        return int(text)
    except ValueError as e:
        raise ValueError(f"not an int: {text!r}") from e

print(parse_int("42"))
```

```python
# Multiple except + else + finally
values = ["10", "x", "20"]
total = 0
for v in values:
    try:
        n = int(v)
    except ValueError:
        print("skip", v)
    else:
        total += n            # only on success
    finally:
        pass                  # cleanup would go here
print(total)
```

```python
# Catch specific exceptions — never bare except:
try:
    d = {"a": 1}
    print(d["b"])
except KeyError as e:
    print("missing key", e)
```

```python
# Custom exception hierarchy
class AppError(Exception):
    """Base for application errors."""

class ConfigError(AppError):
    pass

def load_config(path: str) -> dict:
    if not path.endswith(".json"):
        raise ConfigError(f"unsupported config: {path}")
    return {"path": path}

try:
    load_config("settings.yaml")
except AppError as e:
    print("app failed:", e)
```

```python
# Don't swallow silently in libraries
def risky():
    try:
        1 / 0
    except ZeroDivisionError:
        # bad: pass
        # better: log + re-raise or return Result
        raise
```

## Common mistakes

| Mistake | Fix |
|---------|-----|
| Bare `except:` | Catch `Exception` or specific types |
| Swallowing errors | Log and decide: retry, convert, or raise |
| Using exceptions for normal control flow | Prefer returning values when expected |
| Catching `BaseException` | Avoid (includes `KeyboardInterrupt`) |

---

## Continue

- **Previous:** [`map()`, `filter()`, `reduce()`](17-map-filter-reduce.md)
- **Hub:** [Python topics](../README.md)
- **Next:** [File Handling](19-file-handling.md)
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

