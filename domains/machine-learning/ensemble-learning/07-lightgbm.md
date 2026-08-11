---
title: "7. LightGBM"
description: "Fast GBDT with leaf-wise growth and native categorical support options."
domain: machine-learning
tags: [ensemble, lightgbm]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 7. LightGBM

> Fast GBDT with leaf-wise growth and native categorical support options.

## Definition

**LightGBM** grows trees leaf-wise and uses histogram binning for speed on large data. Popular for high-cardinality tabular problems.

## Code

```python
# pip install lightgbm
from lightgbm import LGBMClassifier

clf = LGBMClassifier(
    n_estimators=300,
    learning_rate=0.05,
    num_leaves=31,
    random_state=42,
)
clf.fit(X_train, y_train, eval_set=[(X_val, y_val)])
```

## Tips

- Control `num_leaves` to limit overfit  
- Prefer native categorical handling when available

---

## Continue

- **Section hub:** [Ensemble Learning](README.md)
- **ML overview:** [Machine Learning](../README.md)
