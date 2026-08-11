---
title: "Pydantic: Serialization"
description: "model_dump, JSON mode, aliases, and excluding fields."
domain: python-frameworks-libraries
tags: [pydantic, serialization]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# Pydantic: Serialization

> model_dump, JSON mode, aliases, and excluding fields.

## Definition

**Serialization** turns models into dicts/JSON for APIs, logs, and queues.

## Important methods / options

| API | Use |
|-----|-----|
| `model_dump()` | dict |
| `model_dump_json()` | JSON string |
| `exclude`, `include` | Field filters |
| `exclude_none` | Drop nulls |
| `by_alias` | Use aliases |
| `mode="json"` | JSON-friendly types |

## Code

```python
from pydantic import BaseModel, Field

class Hit(BaseModel):
    doc_id: str = Field(serialization_alias="id")
    score: float
    raw: str | None = None

h = Hit(doc_id="d1", score=0.9)
print(h.model_dump(by_alias=True, exclude_none=True))
print(h.model_dump_json(by_alias=True, exclude_none=True))
```

---

## Continue

- **Hub:** [Pydantic hub](README.md)
- **Frameworks overview:** [Python Frameworks & Libraries](../README.md)
