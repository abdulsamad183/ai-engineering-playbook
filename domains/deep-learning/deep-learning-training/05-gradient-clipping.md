---
title: "5. Gradient Clipping"
description: "Cap gradient norms — stop exploding updates in RNNs and deep nets."
domain: deep-learning
tags: [training, grad-clip]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 5. Gradient Clipping

> Cap gradient norms — stop exploding updates in RNNs and deep nets.

## Definition

**Gradient clipping** rescales gradients when their norm exceeds a threshold, improving stability.

## Code

```python
import torch.nn.utils as utils

loss.backward()
utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
optimizer.step()
```

---

## Continue

- **Section hub:** [Deep Learning Training](README.md)
- **DL overview:** [Deep Learning](../README.md)
