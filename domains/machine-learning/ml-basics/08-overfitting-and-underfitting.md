---
title: "8. Overfitting & Underfitting"
description: "Too complex vs too simple — reading train/val gaps."
domain: machine-learning
tags: [ml-basics, overfitting]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 8. Overfitting & Underfitting

> Too complex vs too simple — reading train/val gaps.

## Definition

- **Overfitting** — memorizes train, fails on new data (high variance)  
- **Underfitting** — too simple for the pattern (high bias)

## Signals

| Pattern | Train | Val |
|---------|-------|-----|
| Underfit | High error | High error |
| Overfit | Low error | High error |
| Good fit | Low-ish | Similar low-ish |

```mermaid
flowchart LR
  U[Underfit] --> Add[More capacity / features]
  O[Overfit] --> Reg[Regularize / more data / simpler]
```

## Fixes

- Overfit: more data, regularization, early stop, fewer features  
- Underfit: richer features, deeper trees, less regularization  

## See also

- [Bias-Variance Tradeoff](09-bias-variance-tradeoff.md)

---

## Continue

- **Section hub:** [ML Basics](README.md)
- **ML overview:** [Machine Learning](../README.md)
