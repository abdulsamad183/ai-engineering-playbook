# Agent Lifecycle Cheat Sheet

> Init → Plan → Execute → Observe → Reflect → Complete

| Stage | Check |
|-------|-------|
| Init | Goal, budgets, permissions loaded |
| Plan | Steps valid against tool registry |
| Execute | Timeout + retry policy |
| Observe | Truncate large tool output |
| Reflect | Optional quality gate |
| Complete | Success criteria verified |

**Guards:** `max_steps`, `max_cost`, `max_duration`

See [Introduction](../domains/ai-agents/introduction-to-agent-engineering.md).
