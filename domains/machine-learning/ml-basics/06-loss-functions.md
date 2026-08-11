---
title: "6. Loss Functions"
description: "What training minimizes — MSE, log-loss, hinge, and custom objectives."
domain: machine-learning
tags: [ml-basics, loss]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 6. Loss Functions

> What training minimizes — MSE, log-loss, hinge, and custom objectives.

## Definition

A **loss function** measures how wrong a prediction is. Training searches for parameters that make average loss small on the training data (plus regularization).

## Common losses

| Loss | Task | Notes |
|------|------|-------|
| MSE / MAE | Regression | MSE penalizes large errors more |
| Binary cross-entropy | Binary class | Log-loss |
| Multiclass CE | Multi-class | Softmax + NLL |
| Hinge | SVM-style | Margin |
| Huber | Regression | Robust to outliers |

## Code

```python
import numpy as np

def mse(y, y_hat):
    return np.mean((y - y_hat) ** 2)

def log_loss_binary(y, p, eps=1e-12):
    p = np.clip(p, eps, 1 - eps)
    return -np.mean(y * np.log(p) + (1 - y) * np.log(1 - p))
```

## Common mistakes

- Optimizing accuracy while the product needs recall  
- Mismatched loss vs metric (train CE, report F1 — OK if intentional)

---

## Continue

- **Section hub:** [ML Basics](README.md)
- **ML overview:** [Machine Learning](../README.md)
