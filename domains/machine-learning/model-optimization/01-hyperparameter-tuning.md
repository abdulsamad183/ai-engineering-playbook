---
title: "1. Hyperparameter Tuning"
description: "Search model knobs on validation / CV — never on the final test set."
domain: machine-learning
tags: [optimization, tuning]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 1. Hyperparameter Tuning

> Search model knobs on validation / CV — never on the final test set.

## Definition

**Hyperparameter tuning** selects non-learned settings (depth, C, lr, …) using validation performance.

## Loop

```mermaid
flowchart LR
  Space[Search space] --> Trial[Train trial]
  Trial --> Score[Val / CV score]
  Score --> Best[Keep best]
  Best --> Final[Refit + test once]
```

## See also

- [Grid Search](02-grid-search.md) · [Random Search](03-random-search.md) · [Bayesian Optimization](04-bayesian-optimization.md)

---

## Continue

- **Section hub:** [Model Optimization](README.md)
- **ML overview:** [Machine Learning](../README.md)
