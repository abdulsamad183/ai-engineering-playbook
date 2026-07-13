# Memory Types Cheat Sheet

> Quick reference for AI memory layers. See [Memory Systems](../domains/context-engineering/memory-systems.md).

## Types

| Type | Scope | Storage | TTL |
|------|-------|---------|-----|
| **Working** | Agent step | In-process | Request |
| **Short-term** | Session | Redis | Hours |
| **Long-term** | User | DB + vector | Months+ |
| **Episodic** | Events | Event store | Configurable |
| **Semantic** | Facts | Vector DB | Until deleted |
| **Procedural** | How-to | Versioned docs | Release cycle |

## Recall Triggers

| Type | Trigger |
|------|---------|
| Short-term | `session_id` |
| Semantic | `user_id` + query embedding |
| Episodic | Time + topic similarity |
| Procedural | Intent / task classifier |

## Write Rules

- ✅ Explicit user request
- ✅ Validated extraction (confidence threshold)
- ❌ Unverified model output
- ❌ Tool output without validation

## See Also

- [Context Personalization Checklist](context-personalization-checklist.md)
