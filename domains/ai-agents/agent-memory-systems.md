---
title: "Agent Memory Systems"
description: "Agent memory — working, episodic, semantic, vector, structured, external, shared memory for autonomous systems."
domain: ai-agents
tags: [ai-agents, memory, episodic, semantic]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - ../context-engineering/memory-systems.md
  - agent-state-management.md
keywords: [agent memory, working memory, vector memory, shared memory]
author: hp
---

# Agent Memory Systems

## Overview

Section **6**. Agents need layered memory beyond conversation history.

| Type | Scope | Agent use |
|------|-------|-----------|
| **Working** | Current run scratchpad | Plan, observations |
| **Short-term** | Session | Recent tool results |
| **Episodic** | Past runs | "Last time we..." |
| **Semantic** | Facts | User prefs, domain facts |
| **Vector** | RAG recall | Knowledge retrieval tool |
| **Structured** | DB/JSON | Tickets, CRM records |
| **External** | Files, git | Codebase state |
| **Shared** | Multi-agent | Blackboard |

```mermaid
flowchart TB
    WM[Working Memory] --> AGENT[Agent Loop]
    STM[Short-term] --> AGENT
    LTM[Long-term / Semantic] --> AGENT
    EXT[External / RAG] --> AGENT
```

## Updates and Expiration

- Write episodic memory after successful task completion
- Compress working memory each N steps
- Never persist unvalidated LLM hallucinations

See [Context Engineering Memory](../context-engineering/memory-systems.md) for storage patterns.

## Navigation

- [Tool Use](tool-use.md)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Initial publication |
