---
title: "8. Imbalanced Data"
description: "Rare positives — resampling, class weights, and the right metrics."
domain: machine-learning
tags: [feature-engineering, imbalance]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 8. Imbalanced Data

> Rare positives — resampling, class weights, and the right metrics.

## Definition

**Imbalanced data** means one class dominates. Accuracy can look great while the minority class is ignored.

## Tactics

| Tactic | Notes |
|--------|-------|
| class_weight | Cheap first try |
| Threshold tuning | On validation |
| Resampling | SMOTE / undersample (careful) |
| Metrics | F1, PR-AUC, recall@k |

## Code

```python
from sklearn.linear_model import LogisticRegression

clf = LogisticRegression(class_weight="balanced", max_iter=1000)
clf.fit(X_train, y_train)
```

---

## Continue

- **Section hub:** [Feature Engineering](README.md)
- **ML overview:** [Machine Learning](../README.md)
