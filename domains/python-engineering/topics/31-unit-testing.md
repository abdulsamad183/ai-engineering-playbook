---
title: "Unit Testing"
description: "Verify code with pytest — tests, fixtures, assertions, parametrization, and testing AI boundaries."
domain: python-engineering
tags: [python, testing, pytest, tutorial]
status: published
created: 2026-08-11
updated: 2026-08-12
version: "1.1"
---

# Unit Testing

> Verify code with pytest — tests, fixtures, assertions, parametrization, and testing AI boundaries.

## Definition

**Unit testing** checks small pieces of code (functions/classes) in isolation to catch regressions early. In Python, **pytest** is the de facto standard.

## Uses

- Lock parsing/normalization logic
- Prevent prompt-builder regressions
- CI gates before deploy
- Fast feedback while refactoring

## Types of tests (pyramid)

| Type | Scope | Speed |
|------|-------|-------|
| Unit | One function/module | Fast |
| Integration | DB/API together | Medium |
| E2E / eval | Full system / LLM quality | Slower |

## Code examples

```python
# test_normalize.py
def normalize(text: str) -> str:
    return " ".join(text.strip().lower().split())

def test_normalize_collapses_space():
    assert normalize("  Hello   World ") == "hello world"

def test_normalize_empty():
    assert normalize("   ") == ""
```

```python
import pytest

@pytest.fixture
def sample_docs():
    return [{"id": "1", "text": "rag"}, {"id": "2", "text": "agent"}]

def test_count(sample_docs):
    assert len(sample_docs) == 2
```

```python
import pytest

@pytest.mark.parametrize("raw,expected", [
    ("42", 42),
    ("0", 0),
])
def test_parse(raw, expected):
    assert int(raw) == expected
```

```python
import pytest

def test_rejects_negative():
    with pytest.raises(ValueError):
        raise ValueError("nope")
```

```python
from unittest.mock import Mock

llm = Mock(return_value="ok")
assert llm("hi") == "ok"
llm.assert_called_once_with("hi")
```

## Testing AI systems

- Unit-test **deterministic** parts (chunking, routing, schema validation)
- Put LLM quality in **eval suites**, not only unit tests
- Use golden files for prompt assembly snapshots

## Common mistakes

- Tests that hit real paid APIs by default
- Brittle tests coupled to exact log wording
- No tests for failure paths

---

## Continue

- **Previous:** [Logging](30-logging.md)
- **Hub:** [Python topics](../README.md)
- **Next:** [Debugging](32-debugging.md)
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

