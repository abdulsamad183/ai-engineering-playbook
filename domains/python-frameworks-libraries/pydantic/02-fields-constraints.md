---
title: "Pydantic: Fields & Constraints"
description: "Field(), constraints, defaults, and aliases."
domain: python-frameworks-libraries
tags: [pydantic, fields]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# Pydantic: Fields & Constraints

> Field(), constraints, defaults, and aliases.

## Definition

**`Field`** attaches constraints, defaults, descriptions, and aliases to model fields — surfaced in OpenAPI and error messages.

## Important APIs

| API | Use |
|-----|-----|
| `Field(...)` | Required field metadata |
| `ge`, `le`, `gt`, `lt` | Numeric bounds |
| `min_length`, `max_length` | String/collection size |
| `pattern` | Regex constraint |
| `default` / `default_factory` | Defaults |
| `alias` | External name |

## Code

```python
from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    message: str = Field(min_length=1, max_length=8000, description="User text")
    temperature: float = Field(default=0.2, ge=0, le=2)
    max_tokens: int = Field(default=512, ge=1, le=4096)
    tags: list[str] = Field(default_factory=list)

print(ChatRequest(message="hello"))
```

---

## Continue

- **Hub:** [Pydantic hub](README.md)
- **Frameworks overview:** [Python Frameworks & Libraries](../README.md)
