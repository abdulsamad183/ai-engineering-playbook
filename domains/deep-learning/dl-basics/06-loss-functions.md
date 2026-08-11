---
title: "6. Loss Functions"
description: "Training objectives — cross-entropy, MSE, and task-specific losses."
domain: deep-learning
tags: [dl-basics, loss]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 6. Loss Functions

> Training objectives — cross-entropy, MSE, and task-specific losses.

## Definition

The **loss** scores predictions vs targets. Optimizers minimize average loss over batches.

## Common losses

| Loss | Use |
|------|-----|
| Cross-entropy | Classification |
| MSE / L1 | Regression |
| CTC / seq losses | Alignment-heavy sequences |
| Contrastive / InfoNCE | Representation learning |

## Code

```python
import torch.nn.functional as F
import torch

logits = torch.randn(8, 10)
y = torch.randint(0, 10, (8,))
loss = F.cross_entropy(logits, y)
```

## See also

- [ML Loss Functions](../../machine-learning/ml-basics/06-loss-functions.md)

---

## Continue

- **Section hub:** [Deep Learning Basics](README.md)
- **DL overview:** [Deep Learning](../README.md)
