---
title: "Pydantic: BaseModel Basics"
description: "Define schemas, parse dicts/JSON, and catch validation errors."
domain: python-frameworks-libraries
tags: [pydantic, basemodel]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# Pydantic: BaseModel Basics

> Define schemas, parse dicts/JSON, and catch validation errors.

## Definition

**`BaseModel`** is Pydantic’s core class. Subclass it with typed fields; call the constructor or `model_validate` to parse/validate data.

## Key classes

| Class | Role |
|-------|------|
| `BaseModel` | Schema + validation |
| `ValidationError` | Raised on invalid input |

## Important methods

| Method | Use |
|--------|-----|
| `Model(**data)` | Parse kwargs |
| `model_validate(obj)` | Parse dict/object |
| `model_validate_json(s)` | Parse JSON string |
| `model_dump()` | To dict |
| `model_dump_json()` | To JSON string |

## Code

```python
from pydantic import BaseModel, ValidationError

class User(BaseModel):
    id: int
    email: str
    active: bool = True

u = User(id=1, email="a@b.com")
print(u, u.email)

try:
    User(id="x", email="a@b.com")
except ValidationError as e:
    print(e.errors())
```

## Uses

- Boundary validation for APIs and tools
- Document expected LLM JSON shapes

---

## Continue

- **Hub:** [Pydantic hub](README.md)
- **Frameworks overview:** [Python Frameworks & Libraries](../README.md)
