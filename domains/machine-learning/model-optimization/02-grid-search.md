---
title: "2. Grid Search"
description: "Exhaustive Cartesian product of hyperparameter values."
domain: machine-learning
tags: [optimization, grid-search]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 2. Grid Search

> Exhaustive Cartesian product of hyperparameter values.

## Definition

**Grid search** evaluates every combination in a parameter grid (usually with CV).

## Code

```python
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier

grid = GridSearchCV(
    RandomForestClassifier(random_state=42),
    param_grid={"n_estimators": [100, 200], "max_depth": [4, 8, None]},
    cv=5,
    scoring="f1",
    n_jobs=-1,
)
grid.fit(X_train, y_train)
print(grid.best_params_, grid.best_score_)
```

## Tradeoff

- Thorough but expensive as dimensions grow

---

## Continue

- **Section hub:** [Model Optimization](README.md)
- **ML overview:** [Machine Learning](../README.md)
