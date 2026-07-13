---
title: "Event-Driven Agents"
description: "Event bus, triggers, pub/sub, async execution, reactive agent architectures."
domain: ai-agents
tags: [ai-agents, events, pub-sub, async, phase-8]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - agent-state-management.md
  - ../backend-engineering/background-processing-for-ai.md
keywords: [event-driven, event bus, triggers, reactive agents]
author: hp
---

# Event-Driven Agents

## Overview

Section **10** of Phase 8.

```mermaid
flowchart LR
    TRIG[Triggers] --> BUS[Event Bus]
    BUS --> ROUTE[Router]
    ROUTE --> A1[Agent Worker]
    ROUTE --> A2[Agent Worker]
    A1 --> BUS
```

## Patterns

| Pattern | Use case |
|---------|----------|
| **Webhook trigger** | Ticket created → support agent |
| **Queue consumer** | SQS/Kafka → agent job |
| **Pub/Sub** | Fan-out notifications |
| **Scheduled** | Cron maintenance agent |

## Production Architecture

- Durable queues (not in-memory only)
- At-least-once delivery + idempotent handlers
- Dead-letter queue for failed runs
- Correlation ID across events

## Navigation

- [Multi-Agent Systems](multi-agent-systems.md)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Phase 8 Section 10 |
