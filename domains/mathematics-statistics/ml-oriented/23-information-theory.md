---
title: "23. Information Theory"
description: "Entropy, KL divergence, and mutual information — measuring uncertainty and difference."
domain: mathematics-statistics
tags: [ml-math, information-theory]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 23. Information Theory

> Entropy, KL divergence, and mutual information — measuring uncertainty and difference.

## Definition

**Information theory** quantifies uncertainty and difference between distributions. In ML it underpins cross-entropy, KL regularization, and compression views of learning.

## Key quantities

| Quantity | Meaning |
|----------|---------|
| Entropy H(p) | Uncertainty of p |
| Cross-entropy H(p,q) | Cost of coding p with q |
| KL(p ‖ q) | Extra bits using q instead of p |
| Mutual information | Shared information between variables |

## Code

```python
import numpy as np

def entropy(p):
    p = np.asarray(p, dtype=float)
    p = p[p > 0]
    return -np.sum(p * np.log(p))

def kl(p, q):
    p, q = np.asarray(p, float), np.asarray(q, float)
    mask = p > 0
    return np.sum(p[mask] * np.log(p[mask] / q[mask]))

p = np.array([0.7, 0.2, 0.1])
q = np.array([0.5, 0.3, 0.2])
print("H(p)", entropy(p))
print("KL(p||q)", kl(p, q))
# CE = H(p) + KL(p||q)
print("CE", entropy(p) + kl(p, q))
```

## Uses

- Cross-entropy loss  
- KL in VAEs / RLHF / distillation  
- Feature selection / MI views  

## Common mistakes

- Confusing KL(p‖q) with KL(q‖p) (asymmetric)

---

## Continue

- **Section hub:** [ML-Oriented Mathematics](README.md)
- **Math & Stats overview:** [Mathematics & Statistics](../README.md)
