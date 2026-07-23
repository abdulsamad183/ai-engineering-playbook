---
title: "Monitoring AI Systems"
description: "Metrics, health checks, dashboards, alerting, SLA, SLO, error budgets."
domain: ai-deployment
tags: [monitoring, slo, alerting]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - observability-for-ai.md
  - ../ai-evaluation/evaluation-dashboards.md
keywords: [monitoring, SLO, health checks, alerting]
author: hp
---

# Monitoring AI Systems

## Overview

Section **6**.

```mermaid
flowchart TB
    APP[AI Service] --> MET[Metrics]
    APP --> HC[Health checks]
    MET --> PROM[Prometheus/Grafana]
    PROM --> ALERT[PagerDuty]
```

## Key Metrics

| Category | Examples |
|----------|----------|
| **Quality** | Faithfulness score, error rate |
| **Latency** | p95 E2E, TTFT |
| **Cost** | $/hour, tokens/min |
| **Reliability** | 5xx rate, timeout rate |

## Health Checks

- `/health` — process up
- `/ready` — DB, Redis, model API reachable

## SLO Example

99.5% requests < 5s over 30 days; error budget → freeze features.

## Navigation

- [Logging](logging-for-ai.md)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Initial publication |
