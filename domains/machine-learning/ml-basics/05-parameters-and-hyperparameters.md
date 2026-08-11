---
title: "5. Model Parameters & Hyperparameters"
description: "Learned weights vs knobs you set — and who tunes what."
domain: machine-learning
tags: [ml-basics, hyperparameters]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 5. Model Parameters & Hyperparameters

> Learned weights vs knobs you set — and who tunes what.

## Definition

- **Parameters** — learned from data (weights, tree splits)  
- **Hyperparameters** — chosen by you / search (learning rate, depth, C)

## Examples

| Model | Parameters | Hyperparameters |
|-------|------------|-----------------|
| Linear regression | coefficients | (none / regularization strength) |
| Logistic / SVM | weights | C, kernel |
| Random Forest | tree structure | n_estimators, max_depth |
| Neural net | weights/biases | lr, layers, batch size |

## Code

```python
from sklearn.linear_model import LogisticRegression

# C is a hyperparameter; coef_ are parameters after fit
clf = LogisticRegression(C=1.0, max_iter=1000)
clf.fit(X_train, y_train)
print(clf.coef_.shape)
```

## Common mistakes

- Treating hyperparameters as free on the test set  
- Ignoring defaults that may be wrong for your scale  

## See also

- [Hyperparameter Tuning](../model-optimization/01-hyperparameter-tuning.md)

---

## Continue

- **Section hub:** [ML Basics](README.md)
- **ML overview:** [Machine Learning](../README.md)
