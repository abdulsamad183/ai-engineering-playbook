---
title: "2. Random Forest"
description: "Bagged trees with feature randomness — strong default for tabular ML."
domain: machine-learning
tags: [ensemble, random-forest]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 2. Random Forest

> Bagged trees with feature randomness — strong default for tabular ML.

## Definition

**Random Forest** = bagged decision trees where each split considers a random feature subset. Often excellent accuracy with little tuning.

## Code

```python
from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier(
    n_estimators=200,
    max_depth=None,
    min_samples_leaf=2,
    n_jobs=-1,
    random_state=42,
)
clf.fit(X_train, y_train)
print(clf.feature_importances_)
```

## Tips

- Scale usually unnecessary  
- Watch class imbalance (`class_weight`)  
- Importances are useful but correlated features share credit

---

## Continue

- **Section hub:** [Ensemble Learning](README.md)
- **ML overview:** [Machine Learning](../README.md)
