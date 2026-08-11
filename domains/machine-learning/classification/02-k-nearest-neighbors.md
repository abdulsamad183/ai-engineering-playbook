---
title: "2. K-Nearest Neighbors"
description: "Lazy learner — classify by majority vote of nearby training points."
domain: machine-learning
tags: [classification, knn]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 2. K-Nearest Neighbors

> Lazy learner — classify by majority vote of nearby training points.

## Definition

**k-NN** predicts from the k closest training examples (distance usually Euclidean after scaling).

## Code

```python
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

clf = make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=5))
clf.fit(X_train, y_train)
```

## Tradeoffs

| Pros | Cons |
|------|------|
| Simple, nonlinear | Slow at predict time |
| Few assumptions | Curse of dimensionality |
| Good baseline | Needs scaling |

## Hyperparameters

- `n_neighbors`, distance metric, weights (`uniform` / `distance`)

---

## Continue

- **Section hub:** [Classification](README.md)
- **ML overview:** [Machine Learning](../README.md)
