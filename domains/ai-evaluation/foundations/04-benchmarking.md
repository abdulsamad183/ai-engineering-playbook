---
title: "AI Benchmarking"
description: "Public, internal, custom, regression, and performance benchmarks — strengths and limitations."
domain: ai-evaluation
tags: [ai-evaluation, benchmarking, regression]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - evaluation-datasets.md
  - frameworks/openai-evals.md
keywords: [benchmark, MMLU, regression benchmark]
author: hp
---

# AI Benchmarking

## Overview

Section **14**.

## Benchmark Types

| Type | Purpose |
|------|---------|
| **Public** | Model capability (MMLU, HumanEval) |
| **Internal** | Your product tasks |
| **Custom** | Domain-specific suites |
| **Regression** | Block deploy on drop |
| **Performance** | Latency/cost under load |

## Strengths and Limitations

| Strength | Limitation |
|----------|------------|
| Comparable across models | May not reflect your users |
| Good for model selection | Contamination / overfitting |
| Automated | Gaming via prompt tuning |

## Benchmark Automation

```mermaid
flowchart LR
    SCHED[Scheduler] --> RUN[Run benchmark]
    RUN --> STORE[Results DB]
    STORE --> COMPARE[Compare to baseline]
    COMPARE --> ALERT[Alert on regression]
```

## Best Practices

- Internal benchmarks > public alone for ship decisions
- Version benchmark datasets
- Report slice metrics

## Navigation

- [A/B Testing](ab-testing.md)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Initial publication |
