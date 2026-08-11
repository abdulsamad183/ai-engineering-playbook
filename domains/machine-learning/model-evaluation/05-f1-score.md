---
title: "5. F1 Score"
description: "Harmonic mean of precision and recall — one number for imbalance."
domain: machine-learning
tags: [evaluation, f1]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 5. F1 Score

> Harmonic mean of precision and recall — one number for imbalance.

## Definition

**F1** = 2 · precision · recall / (precision + recall). Balances the two; extends to macro/micro/weighted averages for multiclass.

## Code

```python
from sklearn.metrics import f1_score

f1_score(y_test, y_pred)
f1_score(y_test, y_pred, average="macro")  # multiclass
```

## Notes

- F1 ignores true negatives — OK for many detection tasks  
- Prefer PR-AUC when threshold will be swept

---

## Continue

- **Section hub:** [Model Evaluation](README.md)
- **ML overview:** [Machine Learning](../README.md)
