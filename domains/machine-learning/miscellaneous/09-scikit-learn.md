---
title: "9. Scikit-Learn"
description: "The standard classical ML toolkit — estimators, transformers, CV, and metrics."
domain: machine-learning
tags: [misc, sklearn]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 9. Scikit-Learn

> The standard classical ML toolkit — estimators, transformers, CV, and metrics.

## Definition

**scikit-learn** is the default Python library for classical ML: consistent `fit` / `predict` / `transform` APIs, model selection, and metrics.

## Core API

| Object | Methods |
|--------|---------|
| Estimator | `fit`, `predict` (and often `predict_proba`) |
| Transformer | `fit`, `transform` |
| Pipeline | Chains both |
| CV tools | `GridSearchCV`, `cross_val_score` |

## Code

```python
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

X, y = load_breast_cancer(return_X_y=True)
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
clf = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))
clf.fit(X_tr, y_tr)
print(classification_report(y_te, clf.predict(X_te)))
```

## Docs

- https://scikit-learn.org/

---

## Continue

- **Section hub:** [Miscellaneous ML](README.md)
- **ML overview:** [Machine Learning](../README.md)
