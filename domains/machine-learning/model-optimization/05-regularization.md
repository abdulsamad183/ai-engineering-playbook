---
title: "5. Regularization"
description: "Penalize complexity — L1/L2, dropout (DL), tree constraints."
domain: machine-learning
tags: [optimization, regularization]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 5. Regularization

> Penalize complexity — L1/L2, dropout (DL), tree constraints.

## Definition

**Regularization** constrains model capacity to improve generalization: weight penalties, max depth, min leaf size, dropout, early stopping.

## Examples

| Model | Regularizers |
|-------|----------------|
| Linear / logistic | L1 / L2 / Elastic Net (`C` / `alpha`) |
| Trees | max_depth, min_samples_leaf |
| GBDT | learning_rate, subsample, lambda |
| Neural nets | weight decay, dropout |

## See also

- [Ridge](../regression/04-ridge-regression.md) · [Overfitting](../ml-basics/08-overfitting-and-underfitting.md)

---

## Continue

- **Section hub:** [Model Optimization](README.md)
- **ML overview:** [Machine Learning](../README.md)
