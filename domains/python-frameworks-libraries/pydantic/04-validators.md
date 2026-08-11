---
title: "Pydantic: Validators"
description: "Custom field and model validation with field_validator / model_validator."
domain: python-frameworks-libraries
tags: [pydantic, validators]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# Pydantic: Validators

> Custom field and model validation with field_validator / model_validator.

## Definition

**Validators** run custom logic during parsing — normalize strings, cross-check fields, or reject unsafe values.

## Important APIs (v2)

| API | Use |
|-----|-----|
| `@field_validator` | Per-field |
| `@model_validator` | Whole-model |
| `mode="before"/"after"` | When it runs |

## Code

```python
from pydantic import BaseModel, field_validator, model_validator

class Query(BaseModel):
    text: str
    k: int = 5

    @field_validator("text")
    @classmethod
    def strip_text(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError("text must not be empty")
        return v

    @model_validator(mode="after")
    def check_k(self):
        if self.k < 1:
            raise ValueError("k must be >= 1")
        return self

print(Query(text="  hello  ", k=3))
```

---

## Continue

- **Hub:** [Pydantic hub](README.md)
- **Frameworks overview:** [Python Frameworks & Libraries](../README.md)
