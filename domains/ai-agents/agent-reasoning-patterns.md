---
title: "Agent Reasoning Patterns"
description: "ReAct, reflection, planning, ToT, debate, self-consistency — architecture, workflows, production tradeoffs."
domain: ai-agents
tags: [ai-agents, ReAct, reflection, planning, reasoning]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - ../prompt-engineering/advanced-reasoning-strategies.md
  - agent-planning.md
keywords: [ReAct, reflection, tree of thoughts, self-consistency, debate]
author: hp
---

# Agent Reasoning Patterns

## Overview

Section **4**.

| Pattern | Flow | Production use |
|---------|------|----------------|
| **ReAct** | Thought → Action → Observation | Default tool loop |
| **Reflection** | Act → Critique → Revise | Quality-sensitive outputs |
| **Self-critique** | Generate → Score → Improve | Code, reports |
| **Planning** | Plan once → Execute steps | Multi-step tasks |
| **Replanning** | Observe failure → New plan | Robust ops |
| **Task decomposition** | Break goal into subtasks | Complex goals |
| **Tree of Thoughts** | Branch → Evaluate → Prune | Search problems |
| **Debate** | Multiple perspectives → Merge | High-stakes analysis |
| **Self-consistency** | Sample N → Majority vote | Reduce variance |

## ReAct Workflow

```mermaid
flowchart LR
    T[Thought] --> A[Action]
    A --> O[Observation]
    O --> T
```

## Reflection Loop

```mermaid
flowchart LR
    OUT[Output] --> CRIT[Critique]
    CRIT --> REV[Revise]
    REV --> OUT
```

## Tradeoffs

| Pattern | Cost | Latency | Reliability gain |
|---------|------|---------|------------------|
| ReAct | Medium | Medium | Baseline |
| Reflection | High | High | High for quality |
| ToT | Very high | Very high | Niche |

> **Production default:** ReAct + optional reflection on final artifact + explicit replan on tool failure.

## Python Example

```python
REACT_SYSTEM = """Think step by step. Format:
Thought: ...
Action: tool_name
Action Input: {...}
Stop with: Final Answer: ... when done."""
```

## Navigation

- [Agent Planning](agent-planning.md) · [Prompt Engineering Reasoning](../prompt-engineering/advanced-reasoning-strategies.md)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Initial publication |
