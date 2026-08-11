---
title: "8. CatBoost"
description: "GBDT with strong categorical encoding and ordered boosting tricks."
domain: machine-learning
tags: [ensemble, catboost]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 8. CatBoost

> GBDT with strong categorical encoding and ordered boosting tricks.

## Definition

**CatBoost** focuses on categorical features and reducing prediction shift via ordered target statistics / ordered boosting.

## Code

```python
# pip install catboost
from catboost import CatBoostClassifier

clf = CatBoostClassifier(
    iterations=300,
    depth=6,
    learning_rate=0.05,
    cat_features=cat_idx,  # column indices
    verbose=False,
    random_seed=42,
)
clf.fit(X_train, y_train, eval_set=(X_val, y_val))
```

## When to prefer

- Many categorical columns  
- Want solid results with less manual encoding

---

## Continue

- **Section hub:** [Ensemble Learning](README.md)
- **ML overview:** [Machine Learning](../README.md)
