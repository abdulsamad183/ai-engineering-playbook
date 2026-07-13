---
title: "Production Agent Engineering"
description: "Production agents — observability, tracing, cost optimization, scaling, queues, multi-tenant, checkpointing."
domain: ai-agents
tags: [ai-agents, production, observability, scaling, phase-8]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - ../logging/logging-for-ai-applications.md
  - human-in-the-loop.md
keywords: [production agents, tracing, scaling, checkpointing]
author: hp
---

# Production Agent Engineering

## Overview

Section **17** of Phase 8.

```mermaid
flowchart LR
    AGENT[Agent Workers] --> Q[Queue]
    Q --> SCALE[Auto-scale]
    AGENT --> TRACE[Traces]
    TRACE --> DASH[Dashboards]
```

## Operations Checklist

| Area | Practice |
|------|----------|
| **Observability** | Span per step; log tool I/O redacted |
| **Tracing** | OpenTelemetry / LangSmith |
| **Cost** | Per-run budget; model routing |
| **Rate limits** | Per user/tenant |
| **Retries** | Exponential backoff; idempotent tools |
| **Checkpointing** | Resume long runs |
| **Queues** | Celery/SQS for async agents |
| **Multi-tenant** | Isolated state + tool credentials |

## Reliability SLOs

- p95 latency per task type
- Success rate ≥ target (e.g. 95%)
- Max cost per run enforced

## Navigation

- [Agent Security](agent-security.md)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Phase 8 Section 17 |
