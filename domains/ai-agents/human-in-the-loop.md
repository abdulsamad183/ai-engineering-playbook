---
title: "Human-in-the-Loop for Agents"
description: "Approval workflows, escalation, human feedback, review queues, safe execution, override."
domain: ai-agents
tags: [ai-agents, HITL, approval, safety]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - agent-security.md
  - production-agent-engineering.md
keywords: [human in the loop, approval, escalation, override]
author: hp
---

# Human-in-the-Loop for Agents

## Overview

Section **12**.

```mermaid
sequenceDiagram
    participant A as Agent
    participant Q as Review Queue
    participant H as Human
    A->>Q: destructive action request
    Q->>H: notify
    H->>Q: approve / reject
    Q->>A: resume or abort
```

## Patterns

| Pattern | When |
|---------|------|
| **Pre-approval** | Before send email, payment, deploy |
| **Post-review** | Sample outputs for QA |
| **Escalation** | Low confidence or policy edge |
| **Correction** | Human edits agent plan |
| **Kill switch** | Immediate abort |

## Safe Execution

- Classify tools: read / write / destructive
- Auto-approve reads; queue writes
- Timeout approvals → fail closed

## Navigation

- [Agent Security](agent-security.md)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Initial publication |
