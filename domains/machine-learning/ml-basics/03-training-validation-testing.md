---
title: "3. Training, Validation & Testing"
description: "Why splits exist — train fits, val tunes, test judges once."
domain: machine-learning
tags: [ml-basics, splits]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 3. Training, Validation & Testing

> Why splits exist — train fits, val tunes, test judges once.

## Definition

- **Train set** — fit parameters  
- **Validation set** — choose hyperparameters / early stop  
- **Test set** — unbiased final estimate (use once for claims)

## Rules of thumb

| Split | Typical share | Purpose |
|-------|---------------|---------|
| Train | 60–80% | Learn |
| Val | 10–20% | Tune |
| Test | 10–20% | Report |

## Code

```python
from sklearn.model_selection import train_test_split

X_train, X_temp, y_train, y_temp = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)
X_val, X_test, y_val, y_test = train_test_split(
    X_temp, y_temp, test_size=0.5, random_state=42, stratify=y_temp
)
```

## Common mistakes

- Peeking at test during feature selection  
- Random split when time order matters (use time-based split)  
- Leakage via scaling fit on full data  

## See also

- [Cross-Validation](../model-evaluation/07-cross-validation.md)

---

## Continue

- **Section hub:** [ML Basics](README.md)
- **ML overview:** [Machine Learning](../README.md)
