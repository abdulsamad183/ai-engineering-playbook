---
title: "Multi-Agent Context Sharing"
description: "High-level overview of shared context across agents — blackboard architecture, synchronization, coordination, and shared knowledge."
domain: context-engineering
tags: [context-engineering, multi-agent, blackboard, coordination]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - memory-systems.md
  - context-architecture.md
  - ../ai-agents/README.md
  - ../agent-architectures/README.md
keywords: [multi-agent, shared memory, blackboard, context synchronization]
author: hp
---

# Multi-Agent Context Sharing

> How multiple agents share, read, and write context — introductory patterns for the [AI Agents](../ai-agents/README.md) handbook..

## Table of Contents

- [Overview](#overview)
- [Shared Memory](#shared-memory)
- [Blackboard Architecture](#blackboard-architecture)
- [Context Synchronization](#context-synchronization)
- [Agent Communication](#agent-communication)
- [Shared Knowledge](#shared-knowledge)
- [Coordination](#coordination)
- [Architecture Diagram](#architecture-diagram)
- [Production Considerations](#production-considerations)
- [Interview Preparation](#interview-preparation)
- [Navigation](#navigation)

---

## Overview

Multi-agent systems require **shared context stores** beyond individual session memory — coordinated facts, task state, and observations visible to authorized agents.

Section **16** — expanded in [AI Agents](../ai-agents/README.md).

```mermaid
flowchart TB
    A1[Research Agent] --> BB[Shared Blackboard]
    A2[Writer Agent] --> BB
    A3[Reviewer Agent] --> BB
    BB --> MEM[(Shared Memory Store)]
```

---

## Shared Memory

Central store keyed by `task_id` or `workflow_id`:

| Entry type | Writers | Readers |
|------------|---------|---------|
| Facts | Research agent | All |
| Draft | Writer agent | Reviewer |
| Decisions | Orchestrator | All |

ACL per entry type — not all agents see everything.

---

## Blackboard Architecture

Classic pattern: agents post structured artifacts to a shared board; orchestrator or event bus notifies subscribers.

```python
@dataclass
class BlackboardEntry:
    task_id: str
    agent_id: str
    entry_type: str
    content: dict
    version: int
```

Optimistic concurrency with version checks.

---

## Context Synchronization

- **Event-driven:** agent completes → publish → others refresh context
- **Polling:** orchestrator pulls board state each step
- **Lease-based:** agent locks section while editing

Avoid two agents writing conflicting global state without coordination.

---

## Agent Communication

Messages are context for receiving agents — format as structured blocks, not free-form chat when possible.

---

## Shared Knowledge

Org-wide knowledge (retrieval index) vs task-specific blackboard — separate namespaces.

---

## Coordination

Orchestrator assigns budgets per agent:

- Research agent: high retrieval budget
- Writer agent: high output budget, blackboard facts as input
- Reviewer: draft + rubric only

---

## Architecture Diagram

```mermaid
sequenceDiagram
    participant O as Orchestrator
    participant R as Research Agent
    participant W as Writer Agent
    participant B as Blackboard

    O->>R: task + budget
    R->>B: post facts
    O->>W: task + read facts
    W->>B: post draft
    O->>O: assemble final context
```

---

## Production Considerations

- Trace agent ID on every blackboard write
- TTL and cleanup for completed tasks
- Tenant isolation on shared stores

---

## Interview Preparation

**Q: How do agents share context without chaos?**

> Structured blackboard, typed entries, orchestrator coordination, ACLs, versioning, separate task-scoped vs global knowledge.

---

## Navigation

### Prerequisites

- [Memory Systems](memory-systems.md)
- [Context Architecture](context-architecture.md)

### Related Topics

- [AI Agents](../ai-agents/README.md)
- [Agent Architectures](../agent-architectures/README.md)

### Next

- [Context Quality](context-quality.md)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Initial publication |
