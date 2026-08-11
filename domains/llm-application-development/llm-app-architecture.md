---
title: "LLM App Architecture"
description: "A reference architecture for LLM-backed services."
domain: llm-application-development
tags: [llm-application-development]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# LLM App Architecture

> A reference architecture for LLM-backed services.

## Definition

A typical LLM app has: an API edge, an orchestration layer (prompt + tools + retrieval), model provider adapters, persistence (threads/memory), and observability/eval hooks.

## Why it matters

Clear layering lets you swap models, add RAG, or introduce agents without rewriting the product.

## How it works

```mermaid
flowchart TB
  Edge[API Edge] --> Svc[Application services]
  Svc --> Orch[Orchestrator]
  Orch --> Provider[Model adapter]
  Orch --> Retriever[Retriever]
  Orch --> ToolRuntime[Tool runtime]
  Svc --> Store[(Threads / users / files)]
```

## Key principles

1. **Provider adapters** — Isolate vendor SDKs behind interfaces.
2. **Pure prompt builders** — Testable functions, not buried strings.
3. **Explicit state** — Don't hide critical state only inside the model.

## Common applications

| Application | Description |
|-------------|-------------|
| Chat API | Threaded conversations |
| Doc QA | RAG orchestration |
| Workflow apps | Structured multi-step jobs |

## Common mistakes

- God-object 'agent' with no boundaries
- Business rules only inside prompts

## Further reading

- [Orchestration patterns](orchestration-patterns.md)
- [AI System Design](../ai-system-design/README.md)
