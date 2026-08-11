# Pydantic

> Data validation and settings powered by type hints — the schema layer for FastAPI and AI app boundaries.

**Prerequisites:** [Python type hints](../../python-engineering/topics/27-type-hints.md)  
**Part of:** [Python Frameworks & Libraries](../README.md)

---

## Definition

**Pydantic** validates and parses data into typed Python objects using annotations. `BaseModel` defines schemas; invalid input raises clear errors. FastAPI uses Pydantic for request/response models. v2 is the current major line (`pydantic` 2.x).

---

## When to use Pydantic

| Use | Example |
|-----|---------|
| API schemas | ChatRequest / ChatResponse |
| Config | env-based Settings |
| Tool args | agent tool payloads |
| Structured LLM output | parse JSON → model |

---

## Topics

| # | Topic | Document |
|---|-------|----------|
| 1 | BaseModel basics | [01-basemodel-basics.md](01-basemodel-basics.md) |
| 2 | Fields & constraints | [02-fields-constraints.md](02-fields-constraints.md) |
| 3 | Nested models & collections | [03-nested-collections.md](03-nested-collections.md) |
| 4 | Validators | [04-validators.md](04-validators.md) |
| 5 | Serialization | [05-serialization.md](05-serialization.md) |
| 6 | Settings management | [06-settings.md](06-settings.md) |
| 7 | Important APIs cheat sheet | [07-important-apis.md](07-important-apis.md) |

---

## Related

- [FastAPI](../fastapi/README.md) · [Type Hints](../../python-engineering/topics/27-type-hints.md)
