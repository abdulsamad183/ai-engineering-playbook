---
title: "3. Forward Propagation"
description: "Compute predictions by pushing inputs through layers left to right."
domain: deep-learning
tags: [dl-basics, forward]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 3. Forward Propagation

> Compute predictions by pushing inputs through layers left to right.

## Definition

**Forward propagation** evaluates the network: each layer transforms activations until the output (logits / probabilities).

## Flow

```mermaid
flowchart LR
  X --> Z1["z1 = W1x + b1"]
  Z1 --> A1["a1 = f(z1)"]
  A1 --> Z2["z2 = W2a1 + b2"]
  Z2 --> Yhat["ŷ"]
```

## Code

```python
import torch
import torch.nn.functional as F

x = torch.randn(4, 20)
W1, b1 = torch.randn(64, 20), torch.zeros(64)
W2, b2 = torch.randn(10, 64), torch.zeros(10)
a1 = F.relu(x @ W1.T + b1)
logits = a1 @ W2.T + b2
```

## Tips

- Keep shapes explicit (batch, features)  
- Autograd records this graph for backprop

---

## Continue

- **Section hub:** [Deep Learning Basics](README.md)
- **DL overview:** [Deep Learning](../README.md)
