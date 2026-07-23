---
title: "AI Architecture Patterns"
description: "Request-response, event-driven, pipeline, agentic, pub/sub, microservices, modular monolith."
domain: ai-system-design
tags: [system-design, patterns, architecture]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - scaling-ai-systems.md
  - ../software-architecture/architecture-patterns-foundation.md
keywords: [agentic architecture, event-driven AI, microservices]
author: hp
---

# AI Architecture Patterns

## Overview

Section **16**.

| Pattern | AI use case |
|---------|-------------|
| **Request-response** | Sync chat, completions |
| **Event-driven** | Index on upload; async eval |
| **Pipeline** | Ingest → chunk → embed → index |
| **Agentic** | Tool loop with state machine |
| **Pub/Sub** | Fan-out notifications; multi-agent |
| **Microservices** | Separate retrieval, inference, agents |
| **Modular monolith** | FastAPI modules; start here |
| **CQRS** | Write indexing vs read query paths |

```mermaid
flowchart LR
    subgraph Agentic
        PLAN[Plan] --> ACT[Act]
        ACT --> OBS[Observe]
        OBS --> PLAN
    end
```

## Selection Guide

- **MVP** → modular monolith + queue
- **Team scale** → extract retrieval service
- **High throughput ingest** → event-driven pipeline

## Tradeoffs

Microservices add network latency — avoid premature split.

## Navigation

- [System Design Interviews](ai-system-design-interviews.md)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Initial publication |
