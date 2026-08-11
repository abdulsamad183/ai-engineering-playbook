---
title: "2. Dropout"
description: "Randomly zero activations in train — ensemble-like regularization."
domain: deep-learning
tags: [training, dropout]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 2. Dropout

> Randomly zero activations in train — ensemble-like regularization.

## Definition

**Dropout** drops units with probability \(p\) during training to reduce co-adaptation. Disabled (or scaled) at evaluation.

## Code

```python
import torch.nn as nn

nn.Sequential(nn.Linear(256, 256), nn.ReLU(), nn.Dropout(0.2), nn.Linear(256, 10))
```

---

## Continue

- **Section hub:** [Deep Learning Training](README.md)
- **DL overview:** [Deep Learning](../README.md)
