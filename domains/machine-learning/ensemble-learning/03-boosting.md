---
title: "3. Boosting"
description: "Sequentially fix mistakes — turn weak learners into a strong model."
domain: machine-learning
tags: [ensemble, boosting]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 3. Boosting

> Sequentially fix mistakes — turn weak learners into a strong model.

## Definition

**Boosting** builds an additive ensemble: each new model focuses on errors of the current ensemble. Typically lower bias than bagging; can overfit if unconstrained.

## Family

| Method | Idea |
|--------|------|
| AdaBoost | Reweight hard examples |
| Gradient boosting | Fit residuals / gradients |
| XGBoost / LightGBM / CatBoost | Fast, regularized GBDT |

## See also

- [AdaBoost](04-adaboost.md) · [Gradient Boosting](05-gradient-boosting.md)

---

## Continue

- **Section hub:** [Ensemble Learning](README.md)
- **ML overview:** [Machine Learning](../README.md)
