---
title: "Dataclasses"
description: "Boilerplate-free data containers with @dataclass — fields, defaults, frozen records, and vs Pydantic."
domain: python-engineering
tags: [python, dataclasses, tutorial]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# Dataclasses

> Boilerplate-free data containers with @dataclass — fields, defaults, frozen records, and vs Pydantic.

## Definition

A **dataclass** (via `@dataclass`) is a class auto-generated with `__init__`, `__repr__`, comparisons, etc., from annotated fields. Ideal for plain data records.

## Uses

- Request/response internal models
- Config objects
- Intermediate pipeline structures (Chunk, Hit, Message)

## Types / options

| Option | Effect |
|--------|--------|
| `frozen=True` | Immutable instances |
| `slots=True` | Lower memory (3.10+) |
| `order=True` | Ordering methods |
| `kw_only=True` | Keyword-only fields (3.10+) |

## Code examples

```python
from dataclasses import dataclass, field, asdict

@dataclass
class Chunk:
    doc_id: str
    text: str
    score: float = 0.0
    tags: list[str] = field(default_factory=list)

c = Chunk("d1", "hello", 0.9, tags=["rag"])
print(c)
print(asdict(c))
```

```python
@dataclass(frozen=True)
class ModelRef:
    provider: str
    name: str

m = ModelRef("openai", "gpt-4.1")
# m.name = "x"  # FrozenInstanceError
```

```python
from dataclasses import dataclass

@dataclass
class Message:
    role: str
    content: str

    def tokens_heuristic(self) -> int:
        return max(1, len(self.content) // 4)

print(Message("user", "hello world").tokens_heuristic())
```

```python
@dataclass
class BaseEvent:
    type: str

@dataclass
class LoginEvent(BaseEvent):
    user: str

print(LoginEvent(type="login", user="samad"))
```

## Dataclass vs Pydantic vs TypedDict

| Tool | Validation | Best for |
|------|------------|----------|
| dataclass | Minimal | Internal trusted data |
| Pydantic | Rich runtime | API boundaries |
| TypedDict | Type checker only | Dict-shaped JSON |

## Common mistakes

- Mutable default `tags: list = []` → use `field(default_factory=list)`
- Expecting validation like Pydantic

---

## Continue

- **Previous:** [Object-Oriented Programming](23-oop.md)
- **Hub:** [Python topics](../README.md)
- **Next:** [Decorators](25-decorators.md)
- **AI production guide:** [Python for AI Engineering](../python-for-ai-engineering.md)
