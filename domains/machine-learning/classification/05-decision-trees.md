---
title: "5. Decision Trees"
description: "Axis-aligned splits — interpretable, nonlinear, foundation for forests and boosting."
domain: machine-learning
tags: [classification, decision-trees]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 5. Decision Trees

> Axis-aligned splits — interpretable, nonlinear, foundation for forests and boosting.

## Definition

A **decision tree** recursively splits feature space to purify labels (classification) or reduce variance (regression).

## Code

```python
from sklearn.tree import DecisionTreeClassifier

clf = DecisionTreeClassifier(max_depth=4, min_samples_leaf=10, random_state=42)
clf.fit(X_train, y_train)
```

## Pros / cons

| Pros | Cons |
|------|------|
| Interpretable | Overfits easily |
| Nonlinear | Unstable to small data changes |
| No scaling needed | Axis-aligned only |

## See also

- [Random Forest](../ensemble-learning/02-random-forest.md) · [Gradient Boosting](../ensemble-learning/05-gradient-boosting.md)

---

## Continue

- **Section hub:** [Classification](README.md)
- **ML overview:** [Machine Learning](../README.md)
