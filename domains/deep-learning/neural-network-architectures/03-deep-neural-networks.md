---
title: "3. Deep Neural Networks"
description: "Many layers — hierarchical features, and the challenges of depth."
domain: deep-learning
tags: [architectures, dnn]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 3. Deep Neural Networks

> Many layers — hierarchical features, and the challenges of depth.

## Definition

**Deep neural networks** use many layers to compose features. Depth helps representation power but needs good init, normalization, residual paths, and careful optimization.

## Challenges at depth

| Issue | Mitigations |
|-------|-------------|
| Vanishing/exploding grads | Residual links, norm, good init |
| Optimization hardness | Adam, LR schedules, warmup |
| Overfitting | Regularization, more data |

## See also

- [Residual Networks](04-residual-networks.md) · [Batch Normalization](../deep-learning-training/01-batch-normalization.md)

---

## Continue

- **Section hub:** [Neural Network Architectures](README.md)
- **DL overview:** [Deep Learning](../README.md)
