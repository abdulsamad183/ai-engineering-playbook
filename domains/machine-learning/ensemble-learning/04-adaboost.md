---
title: "4. AdaBoost"
description: "Classic boosting — reweight misclassified points each round."
domain: machine-learning
tags: [ensemble, adaboost]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 4. AdaBoost

> Classic boosting — reweight misclassified points each round.

## Definition

**AdaBoost** trains weak learners (often stumps) sequentially, increasing weights of misclassified examples and combining them with learned votes.

## Code

```python
from sklearn.ensemble import AdaBoostClassifier

clf = AdaBoostClassifier(n_estimators=50, learning_rate=1.0, random_state=42)
clf.fit(X_train, y_train)
```

## Notes

- Sensitive to noisy labels / outliers  
- Often outperformed by modern GBDT on tabular data

---

## Continue

- **Section hub:** [Ensemble Learning](README.md)
- **ML overview:** [Machine Learning](../README.md)
