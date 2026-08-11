---
title: "3. Confusion Matrix"
description: "TP, FP, TN, FN — the raw counts behind most classification metrics."
domain: machine-learning
tags: [evaluation, confusion-matrix]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 3. Confusion Matrix

> TP, FP, TN, FN — the raw counts behind most classification metrics.

## Definition

A **confusion matrix** counts actual vs predicted classes.

```text
                Pred Pos   Pred Neg
Actual Pos        TP         FN
Actual Neg        FP         TN
```

## Code

```python
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

cm = confusion_matrix(y_test, y_pred)
print(cm)
```

## Uses

- Debug which classes confuse the model  
- Derive precision/recall

---

## Continue

- **Section hub:** [Model Evaluation](README.md)
- **ML overview:** [Machine Learning](../README.md)
