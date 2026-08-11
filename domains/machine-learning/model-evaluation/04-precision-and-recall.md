---
title: "4. Precision & Recall"
description: "Precision = trust positives; recall = catch positives."
domain: machine-learning
tags: [evaluation, precision-recall]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 4. Precision & Recall

> Precision = trust positives; recall = catch positives.

## Definition

- **Precision** = TP / (TP + FP) — of predicted positives, how many correct?  
- **Recall** = TP / (TP + FN) — of actual positives, how many found?

## Tradeoff

Raising the positive threshold usually ↑ precision and ↓ recall (task-dependent).

## Code

```python
from sklearn.metrics import precision_score, recall_score

precision_score(y_test, y_pred)
recall_score(y_test, y_pred)
```

## Uses in AI eng

- Safety filters: high precision  
- Fraud / defect finding: high recall

---

## Continue

- **Section hub:** [Model Evaluation](README.md)
- **ML overview:** [Machine Learning](../README.md)
