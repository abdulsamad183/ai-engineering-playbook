---
title: "AI Agents Interviews"
description: "Agent interviews — ReAct, planning, tools, multi-agent, LangGraph, frameworks, HITL."
domain: interview-preparation
tags: [interview, agents, react, langgraph]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - ../ai-agents/README.md
  - mcp-interviews.md
keywords: [agent interview, ReAct, supervisor, tool calling]
author: hp
---

# AI Agents Interviews

## Overview

Section **12**.

## Core Patterns

| Pattern | Interview prompt |
|---------|------------------|
| **ReAct** | Explain loop | Think → tool → observe |
| **Planning** | Decompose task | Subgoals with replanning |
| **Reflection** | Improve answer | Critique + revise |
| **Supervisor** | Multi-agent | Router delegates to workers |
| **Swarm** | vs supervisor | Peer handoff vs central |
| **HITL** | When? | Destructive tools, low confidence |

## Framework Comparison (interview)

| Framework | Say in interview |
|-----------|------------------|
| **LangGraph** | Stateful graph, cycles, checkpointing |
| **CrewAI** | Role-based agents |
| **AutoGen** | Conversable agents |
| **PydanticAI** | Type-safe tools |
| **OpenAI Agents SDK** | Lightweight orchestration |

## FAQ

**Q: How prevent infinite agent loops?**

> Max steps; duplicate action detection; timeout; cost budget.

**Q: How evaluate agents?**

> Task completion, tool accuracy, trajectory match — [Agent eval](../ai-evaluation/agent-evaluation.md).

**Architecture:** Supervisor vs single agent?

> Supervisor when specialized tools/domains; single agent for simple workflows — ops cost tradeoff.

## Coding Exercise

Implement 3-step ReAct loop with mock tools (search, calculator).

## Further Reading

- [AI Agents](../ai-agents/README.md)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Section 12 |
