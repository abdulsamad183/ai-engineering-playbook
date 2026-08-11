---
title: "9. Stacking & Voting"
description: "Combine heterogeneous models — soft/hard vote or meta-learners."
domain: machine-learning
tags: [ensemble, stacking]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 9. Stacking & Voting

> Combine heterogeneous models — soft/hard vote or meta-learners.

## Definition

- **Voting** — average probabilities or majority vote  
- **Stacking** — train a meta-model on base-model predictions (out-of-fold)

## Code

```python
from sklearn.ensemble import VotingClassifier, StackingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

voting = VotingClassifier(
    estimators=[("rf", RandomForestClassifier(n_estimators=100)), ("knn", KNeighborsClassifier())],
    voting="soft",
)

stack = StackingClassifier(
    estimators=[("rf", RandomForestClassifier(n_estimators=100)), ("knn", KNeighborsClassifier())],
    final_estimator=LogisticRegression(max_iter=1000),
    passthrough=False,
)
```

## Common mistakes

- Stacking without out-of-fold preds → leakage / optimistic CV

---

## Continue

- **Section hub:** [Ensemble Learning](README.md)
- **ML overview:** [Machine Learning](../README.md)
