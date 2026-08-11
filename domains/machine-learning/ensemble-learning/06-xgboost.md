---
title: "6. XGBoost"
description: "Regularized gradient boosting library — speed, sparsity, and strong defaults."
domain: machine-learning
tags: [ensemble, xgboost]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 6. XGBoost

> Regularized gradient boosting library — speed, sparsity, and strong defaults.

## Definition

**XGBoost** is a scalable GBDT library with regularization, missing-value handling, and efficient histogram/approx split finding.

## Code

```python
# pip install xgboost
from xgboost import XGBClassifier

clf = XGBClassifier(
    n_estimators=200,
    max_depth=6,
    learning_rate=0.05,
    subsample=0.8,
    colsample_bytree=0.8,
    eval_metric="logloss",
    random_state=42,
)
clf.fit(X_train, y_train, eval_set=[(X_val, y_val)], verbose=False)
```

## Uses

- Kaggle-style tabular competitions  
- Production ranking / risk models  

## Common mistakes

- No early stopping → overfit  
- Leaky target encoding without CV

---

## Continue

- **Section hub:** [Ensemble Learning](README.md)
- **ML overview:** [Machine Learning](../README.md)
