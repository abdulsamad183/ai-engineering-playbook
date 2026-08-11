---
title: "7. Gradient Descent"
description: "Step parameters opposite the gradient of the loss."
domain: deep-learning
tags: [dl-basics, gradient-descent]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 7. Gradient Descent

> Step parameters opposite the gradient of the loss.

## Definition

**Gradient descent** updates \(W \leftarrow W - \eta \nabla_W L\). Mini-batch SGD estimates the gradient on a subset for speed and noise that can help generalization.

## Variants

| Method | Idea |
|--------|------|
| Batch GD | Full dataset gradient |
| SGD | Mini-batches |
| Momentum / Adam | Adaptive / smoothed steps |

## Code

```python
eta = 0.01
for p in model.parameters():
    p.data -= eta * p.grad
```

## See also

- [Optimizers](10-optimizers.md) · [Learning Rate](08-learning-rate.md)

---

## Continue

- **Section hub:** [Deep Learning Basics](README.md)
- **DL overview:** [Deep Learning](../README.md)
