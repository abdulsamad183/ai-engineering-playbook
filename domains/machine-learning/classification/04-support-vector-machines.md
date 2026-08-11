---
title: "4. Support Vector Machines"
description: "Max-margin classifiers — linear or kernelized for nonlinear boundaries."
domain: machine-learning
tags: [classification, svm]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 4. Support Vector Machines

> Max-margin classifiers — linear or kernelized for nonlinear boundaries.

## Definition

**SVMs** find a hyperplane maximizing the margin between classes. Kernels (RBF, poly) map features to enable nonlinear separation.

## Code

```python
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

clf = make_pipeline(StandardScaler(), SVC(kernel="rbf", C=1.0, probability=True))
clf.fit(X_train, y_train)
```

## Hyperparameters

| Param | Role |
|-------|------|
| `C` | Soft-margin penalty |
| `kernel` | linear / rbf / poly |
| `gamma` | RBF width |

## Notes

- Scale features  
- Can be slow on very large datasets vs trees / linear models

---

## Continue

- **Section hub:** [Classification](README.md)
- **ML overview:** [Machine Learning](../README.md)
