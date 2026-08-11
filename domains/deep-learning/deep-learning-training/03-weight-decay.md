---
title: "3. Weight Decay"
description: "L2-style parameter penalty — keep weights small via the optimizer."
domain: deep-learning
tags: [training, weight-decay]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 3. Weight Decay

> L2-style parameter penalty — keep weights small via the optimizer.

## Definition

**Weight decay** shrinks parameters each step (coupled with Adam as AdamW). Reduces overfitting and implicit complexity.

## Code

```python
import torch.optim as optim

optim.AdamW(model.parameters(), lr=1e-3, weight_decay=0.01)
```

---

## Continue

- **Section hub:** [Deep Learning Training](README.md)
- **DL overview:** [Deep Learning](../README.md)
