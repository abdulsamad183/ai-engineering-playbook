---
title: "Task Graphs for Agents"
description: "DAG execution, dependency graphs, scheduling, parallel execution, conditional branches, loops."
domain: ai-agents
tags: [ai-agents, DAG, task-graph, scheduling]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - agent-planning.md
  - ../ai-workflows/README.md
keywords: [DAG, execution graph, parallel execution, conditional]
author: hp
---

# Task Graphs for Agents

## Overview

Section **9**.

```mermaid
flowchart TD
    A[Step A] --> C[Step C]
    B[Step B] --> C
    C --> D{Condition}
    D -->|yes| E[Step E]
    D -->|no| F[Step F]
```

## Concepts

| Concept | Description |
|---------|-------------|
| **DAG** | Directed acyclic graph of tasks |
| **Dependency** | B waits for A |
| **Parallel** | A and B concurrent |
| **Conditional** | Branch on observation |
| **Loop** | Repeat until condition (max iterations) |

## Scheduling

Topological sort → execute ready nodes in parallel pools. LangGraph models this as graph nodes/edges.

## Production

- Max parallelism limits
- Per-node timeouts
- Deadlock detection on cyclic graphs (forbid cycles in DAG mode)

## Navigation

- [Event-Driven Agents](event-driven-agents.md)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Initial publication |
