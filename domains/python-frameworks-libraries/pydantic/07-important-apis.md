---
title: "Pydantic: Important APIs Cheat Sheet"
description: "High-frequency Pydantic v2 APIs for AI apps."
domain: python-frameworks-libraries
tags: [pydantic, cheatsheet]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# Pydantic: Important APIs Cheat Sheet

> High-frequency Pydantic v2 APIs for AI apps.

## Classes

`BaseModel`, `ValidationError`, `Field`, `BaseSettings` (pydantic-settings)

## Parse / dump

`model_validate`, `model_validate_json`, `model_dump`, `model_dump_json`

## Validation

`@field_validator`, `@model_validator`, constraints on `Field`

## Structured output sketch

```python
from pydantic import BaseModel, Field

class Extracted(BaseModel):
    intent: str
    confidence: float = Field(ge=0, le=1)

data = {"intent": "refund", "confidence": 0.82}
print(Extracted.model_validate(data))
```

---

## Continue

- **Hub:** [Pydantic hub](README.md)
- **Frameworks overview:** [Python Frameworks & Libraries](../README.md)
