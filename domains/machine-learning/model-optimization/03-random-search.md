---
title: "3. Random Search"
description: "Sample hyperparameter combinations — often better budget use than grids."
domain: machine-learning
tags: [optimization, random-search]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 3. Random Search

> Sample hyperparameter combinations — often better budget use than grids.

## Definition

**Random search** draws hyperparameter sets from distributions. With the same budget, often finds better configs than coarse grids (especially with unimportant dims).

## Code

```python
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import randint

search = RandomizedSearchCV(
    RandomForestClassifier(random_state=42),
    param_distributions={"n_estimators": randint(50, 400), "max_depth": randint(2, 20)},
    n_iter=30,
    cv=5,
    scoring="f1",
    random_state=42,
    n_jobs=-1,
)
search.fit(X_train, y_train)
```

---

## Continue

- **Section hub:** [Model Optimization](README.md)
- **ML overview:** [Machine Learning](../README.md)
