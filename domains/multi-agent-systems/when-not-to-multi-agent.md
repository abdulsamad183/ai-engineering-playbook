---
title: "When Not to Use Multi-Agent"
description: "Complexity traps and simpler alternatives."
domain: multi-agent-systems
tags: [multi-agent-systems]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# When Not to Use Multi-Agent

> Complexity traps and simpler alternatives.

## Definition

Avoid multi-agent when a single agent with tools, a deterministic workflow, or RAG chain meets the bar. Multi-agent adds latency, cost, and failure modes that need their own eval.

## Why it matters

Hype-driven agent swarms are a leading cause of unmaintainable demos.

## How it works

```mermaid
flowchart TB
  Task[Task] --> Q{Need specialized roles?}
  Q -->|no| Single[Single agent / chain]
  Q -->|yes| Q2{Need parallel specialists?}
  Q2 -->|no| Pipeline[Simple pipeline]
  Q2 -->|yes| MAS[Multi-agent]
```

## Key principles

1. **Workflows before swarms** — If steps are known, code them.
2. **Measure incremental gain** — Quality per extra $.
3. **Debugability is a feature** — Prefer inspectable graphs.

## Common applications

| Application | Description |
|-------------|-------------|
| FAQ | RAG only |
| Form filling | Structured extraction |
| Fixed ETL | Orchestrator without LLMs per stage |

## Common mistakes

- Five agents for a two-step task
- No cost dashboard on agent fan-out

## Further reading

- [LLM Application Development — orchestration](../llm-application-development/orchestration-patterns.md)
- [AI Agents](../ai-agents/README.md)
