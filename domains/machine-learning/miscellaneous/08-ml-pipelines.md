---
title: "8. ML Pipelines"
description: "Chain preprocessing and models — fit once, transform consistently, avoid leakage."
domain: machine-learning
tags: [misc, pipelines]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 8. ML Pipelines

> Chain preprocessing and models — fit once, transform consistently, avoid leakage.

## Definition

An **ML pipeline** packages transforms + model so the same steps run in train and serve, with fit parameters learned only from training data.

## Code

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

pipe = Pipeline([
    ("scale", StandardScaler()),
    ("clf", LogisticRegression(max_iter=1000)),
])
pipe.fit(X_train, y_train)
pipe.predict(X_test)
```

## Why it matters

- Prevents preprocessing leakage  
- Cleaner CV and deployment  
- Reproducible training  

## See also

- [Scikit-Learn](09-scikit-learn.md) · [MLOps & LLMOps](../../mlops-llmops/README.md)

---

## Continue

- **Section hub:** [Miscellaneous ML](README.md)
- **ML overview:** [Machine Learning](../README.md)
