---
title: "10. Probability Distributions"
description: "Named distributions — Bernoulli, Binomial, Normal, Poisson, Categorical, and more."
domain: mathematics-statistics
tags: [statistics, distributions]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 10. Probability Distributions

> Named distributions — Bernoulli, Binomial, Normal, Poisson, Categorical, and more.

## Definition

A **probability distribution** specifies how probability mass/density is assigned to values of a random variable.

## Common distributions

| Distribution | Support | Typical use |
|--------------|---------|-------------|
| Bernoulli | {0,1} | Binary outcome |
| Binomial | counts | # successes |
| Categorical | classes | Softmax outputs |
| Normal | real line | Noise, scores |
| Log-normal | positive | Latencies |
| Poisson | counts | Event rates |
| Exponential | positive | Waiting times |
| Beta | (0,1) | Probabilities |
| Dirichlet | simplex | Categorical priors |

## Code

```python
import numpy as np

rng = np.random.default_rng(0)
print(rng.binomial(n=10, p=0.3))
print(rng.normal(0, 1, size=3))
# Categorical via multinomial / choice
print(rng.choice(["a", "b", "c"], p=[0.5, 0.2, 0.3]))
```

## Uses in AI

- Softmax ≈ categorical  
- Gaussian noise assumptions  
- Modeling click/conversion rates  

## See also

- [4. Probability Theory](../mathematics/04-probability-theory.md)

---

## Continue

- **Section hub:** [Statistics](README.md)
- **Math & Stats overview:** [Mathematics & Statistics](../README.md)
