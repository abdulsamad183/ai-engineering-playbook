---
title: "1. Training & Validation"
description: "Split discipline for deep nets — train for learning, val for selection."
domain: deep-learning
tags: [eval, train-val]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 1. Training & Validation

> Split discipline for deep nets — train for learning, val for selection.

## Definition

Use **train** for gradient updates, **validation** for early stopping / LR / checkpoints, and **test** once for final claims.

## Loop

```mermaid
flowchart LR
  Train --> Val
  Val -->|improve| Checkpoint
  Val -->|stop| Done[Stop / LR change]
```

## See also

- [ML splits](../../machine-learning/ml-basics/03-training-validation-testing.md)

---

## Continue

- **Section hub:** [Model Evaluation & Debugging](README.md)
- **DL overview:** [Deep Learning](../README.md)
