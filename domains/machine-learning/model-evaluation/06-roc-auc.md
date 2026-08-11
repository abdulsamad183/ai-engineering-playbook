---
title: "6. ROC-AUC"
description: "Ranking quality across thresholds — ROC curve and area under it."
domain: machine-learning
tags: [evaluation, roc-auc]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 6. ROC-AUC

> Ranking quality across thresholds — ROC curve and area under it.

## Definition

**ROC** plots TPR vs FPR across score thresholds. **AUC** summarizes ranking quality (0.5 ≈ random, 1.0 ≈ perfect).

## Code

```python
from sklearn.metrics import roc_auc_score, RocCurveDisplay

roc_auc_score(y_test, y_scores)
```

## Caveats

- Misleading under heavy imbalance — also check PR-AUC  
- Needs scores/probabilities, not only hard labels

---

## Continue

- **Section hub:** [Model Evaluation](README.md)
- **ML overview:** [Machine Learning](../README.md)
