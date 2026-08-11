---
title: "2. ML Workflow"
description: "End-to-end loop from problem framing through deploy and monitor."
domain: machine-learning
tags: [ml-basics, workflow]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 2. ML Workflow

> End-to-end loop from problem framing through deploy and monitor.

## Definition

The **ML workflow** is the repeatable path from business question to a monitored model in production.

## Stages

| Stage | Goal |
|-------|------|
| Frame | Define task, metric, success |
| Data | Collect, clean, label |
| Features | Represent inputs |
| Split | Train / val / test |
| Train | Fit model |
| Tune | Hyperparameters on val |
| Evaluate | Final test / offline metrics |
| Ship | Deploy + monitor drift |

```mermaid
flowchart TB
  F[Frame] --> D[Data]
  D --> Fe[Features]
  Fe --> S[Split]
  S --> T[Train]
  T --> Tu[Tune]
  Tu --> E[Evaluate]
  E --> Dep[Deploy]
  Dep --> M[Monitor]
  M --> F
```

## Uses in AI eng

- Offline eval harnesses for LLM apps mirror this loop  
- Same discipline for ranking, classifiers, and regressors  

## Common mistakes

- Tuning on the test set  
- No clear metric before modeling

---

## Continue

- **Section hub:** [ML Basics](README.md)
- **ML overview:** [Machine Learning](../README.md)
