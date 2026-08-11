---
title: "7. Model Interpretability"
description: "Prefer transparent models or add post-hoc tools when you need auditability."
domain: machine-learning
tags: [misc, interpretability]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 7. Model Interpretability

> Prefer transparent models or add post-hoc tools when you need auditability.

## Definition

**Interpretability** is how easily a human can understand the mapping from inputs to outputs. Sometimes choose a simpler model; sometimes explain a complex one.

## Spectrum

| More interpretable | Less |
|--------------------|------|
| Linear, shallow trees | Deep ensembles, neural nets |
| Sparse features | Huge feature spaces |

## Code (permutation importance)

```python
from sklearn.inspection import permutation_importance

r = permutation_importance(model, X_val, y_val, n_repeats=10, random_state=42)
```

## Tip

- Interpretability ≠ causality

---

## Continue

- **Section hub:** [Miscellaneous ML](README.md)
- **ML overview:** [Machine Learning](../README.md)
