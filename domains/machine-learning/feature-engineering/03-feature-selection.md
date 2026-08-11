---
title: "3. Feature Selection"
description: "Keep informative features — filter, wrapper, and embedded methods."
domain: machine-learning
tags: [feature-engineering, selection]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 3. Feature Selection

> Keep informative features — filter, wrapper, and embedded methods.

## Definition

**Feature selection** drops unhelpful or redundant inputs to improve generalization, speed, and interpretability.

## Approaches

| Type | Examples |
|------|----------|
| Filter | Correlation, mutual information, χ² |
| Wrapper | RFE, forward selection |
| Embedded | Lasso, tree importances |

## Code

```python
from sklearn.feature_selection import SelectKBest, mutual_info_classif

sel = SelectKBest(mutual_info_classif, k=20)
X_sel = sel.fit_transform(X_train, y_train)
```

---

## Continue

- **Section hub:** [Feature Engineering](README.md)
- **ML overview:** [Machine Learning](../README.md)
