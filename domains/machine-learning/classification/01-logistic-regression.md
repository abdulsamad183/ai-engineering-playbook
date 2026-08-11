---
title: "1. Logistic Regression"
description: "Linear decision boundary with probabilistic outputs via the sigmoid / softmax."
domain: machine-learning
tags: [classification, logistic]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 1. Logistic Regression

> Linear decision boundary with probabilistic outputs via the sigmoid / softmax.

## Definition

**Logistic regression** models class probability with a linear score passed through a sigmoid (binary) or softmax (multiclass). Trained with log-loss.

## Code

```python
from sklearn.linear_model import LogisticRegression

clf = LogisticRegression(max_iter=1000)
clf.fit(X_train, y_train)
proba = clf.predict_proba(X_test)[:, 1]
```

## Uses

- Strong, calibrated-ish baseline for binary problems  
- Interpretable coefficients (log-odds)  

## Common mistakes

- Treating predict() threshold 0.5 as sacred — tune for precision/recall

---

## Continue

- **Section hub:** [Classification](README.md)
- **ML overview:** [Machine Learning](../README.md)
