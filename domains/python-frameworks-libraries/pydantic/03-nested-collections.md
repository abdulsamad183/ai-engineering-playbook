---
title: "Pydantic: Nested Models & Collections"
description: "Compose models — lists, dicts, optional nested objects."
domain: python-frameworks-libraries
tags: [pydantic, nested]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# Pydantic: Nested Models & Collections

> Compose models — lists, dicts, optional nested objects.

## Definition

Models can nest other models and use collection types (`list[T]`, `dict[K,V]`, `set[T]`) with full validation.

## Patterns

| Pattern | Example |
|---------|---------|
| Nested model | `address: Address` |
| List of models | `messages: list[Message]` |
| Optional | `user: User | None = None` |
| Union / literal | `Literal["user","assistant"]` |

## Code

```python
from typing import Literal
from pydantic import BaseModel

class Message(BaseModel):
    role: Literal["user", "assistant", "system"]
    content: str

class ChatThread(BaseModel):
    id: str
    messages: list[Message]

thread = ChatThread(
    id="t1",
    messages=[Message(role="user", content="hi")],
)
print(thread.model_dump())
```

---

## Continue

- **Hub:** [Pydantic hub](README.md)
- **Frameworks overview:** [Python Frameworks & Libraries](../README.md)
