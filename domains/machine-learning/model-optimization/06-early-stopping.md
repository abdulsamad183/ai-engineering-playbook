---
title: "6. Early Stopping"
description: "Stop training when validation stops improving — cheap regularization."
domain: machine-learning
tags: [optimization, early-stopping]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 6. Early Stopping

> Stop training when validation stops improving — cheap regularization.

## Definition

**Early stopping** monitors a validation metric during iterative training (boosting rounds, epochs) and keeps the best checkpoint.

## Code (sklearn GBDT)

```python
from sklearn.ensemble import HistGradientBoostingClassifier

clf = HistGradientBoostingClassifier(
    max_iter=500,
    learning_rate=0.05,
    early_stopping=True,
    validation_fraction=0.1,
    n_iter_no_change=20,
    random_state=42,
)
clf.fit(X_train, y_train)
```

## Tips

- Need a real validation stream  
- Pair with a lower learning rate + more estimators

---

## Continue

- **Section hub:** [Model Optimization](README.md)
- **ML overview:** [Machine Learning](../README.md)
