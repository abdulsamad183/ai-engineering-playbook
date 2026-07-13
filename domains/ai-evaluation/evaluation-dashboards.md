---
title: "Evaluation Dashboards"
description: "Quality, latency, cost, reliability dashboards — engineering and executive views."
domain: ai-evaluation
tags: [ai-evaluation, dashboards, monitoring, metrics, phase-10]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - continuous-evaluation.md
  - production-evaluation.md
keywords: [evaluation dashboard, quality metrics, trends]
author: hp
---

# Evaluation Dashboards

## Overview

Section **17** of Phase 10.

```mermaid
flowchart TB
    EVAL[Eval runs] --> TS[(Time-series DB)]
    TRACE[Traces] --> TS
    TS --> ENG[Engineering dashboard]
    TS --> EXEC[Executive dashboard]
    ENG --> ALERT[Alerts]
```

## Dashboard Layers

| Layer | Audience | Metrics |
|-------|----------|---------|
| **Quality** | ML/AI engineers | Faithfulness, task success, tool accuracy |
| **Latency** | Platform | P95 E2E, TTFT, retrieval |
| **Cost** | FinOps | $/request, $/task |
| **Reliability** | SRE | Error rate, timeouts |
| **Trends** | All | Week-over-week deltas |
| **Executive** | Leadership | Success rate, CSAT proxy, cost |

## Engineering Dashboard Panels

- Golden set scores by version
- Failure bucket pie chart
- Retrieval vs generation metric split
- Agent tool error rate

## Executive Dashboard Panels

- Task completion rate
- Cost per successful interaction
- Incident-linked quality drops

## Production Considerations

- Role-based access to raw outputs (PII)
- Link dashboard drill-down to traces

## Navigation

- [Production Evaluation](production-evaluation.md)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Phase 10 Section 17 |
