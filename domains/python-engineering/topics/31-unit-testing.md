---
title: "Unit Testing"
description: "Verify code with pytest — tests, fixtures, assertions, parametrization, and testing AI boundaries."
domain: python-engineering
tags: [python, testing, pytest, tutorial]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
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
