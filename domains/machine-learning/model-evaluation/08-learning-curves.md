---
title: "8. Learning Curves"
description: "Plot train/val score vs data size or iterations — diagnose fit."
domain: machine-learning
tags: [evaluation, learning-curves]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 8. Learning Curves

> Plot train/val score vs data size or iterations — diagnose fit.

## Definition

**Learning curves** show how performance changes as you add data (or training rounds). Gaps diagnose bias vs variance.

## Code

```python
from sklearn.model_selection import learning_curve
import numpy as np

train_sizes, train_scores, val_scores = learning_curve(
    model, X, y, cv=5, train_sizes=np.linspace(0.2, 1.0, 5), scoring="f1"
)
```

## Reading

| Pattern | Likely issue |
|---------|--------------|
| Both low | Underfit |
| Train high, val low | Overfit |
| Gap closing with more data | Collect more data |

---

## Continue

- **Section hub:** [Model Evaluation](README.md)
- **ML overview:** [Machine Learning](../README.md)
