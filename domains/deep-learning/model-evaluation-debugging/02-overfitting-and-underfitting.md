---
title: "2. Overfitting & Underfitting"
description: "Diagnose capacity vs data — train/val curves tell the story."
domain: deep-learning
tags: [eval, overfit]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 2. Overfitting & Underfitting

> Diagnose capacity vs data — train/val curves tell the story.

## Definition

Deep nets overfit easily. Watch train vs val loss/metrics and apply regularization, augmentation, or more data.

| Pattern | Action |
|---------|--------|
| Both high | Underfit — bigger model / longer train / less reg |
| Train low, val high | Overfit — dropout, decay, aug, early stop |

## See also

- [ML Overfitting](../../machine-learning/ml-basics/08-overfitting-and-underfitting.md)

---

## Continue

- **Section hub:** [Model Evaluation & Debugging](README.md)
- **DL overview:** [Deep Learning](../README.md)
