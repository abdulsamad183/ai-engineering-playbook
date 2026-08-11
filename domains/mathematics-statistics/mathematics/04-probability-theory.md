---
title: "4. Probability Theory"
description: "Random variables, distributions, expectation, and conditional probability."
domain: mathematics-statistics
tags: [mathematics, probability]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 4. Probability Theory

> Random variables, distributions, expectation, and conditional probability.

## Definition

**Probability theory** formalizes uncertainty. A **random variable** maps outcomes to numbers; a **distribution** describes how likely values are.

## Core concepts

| Concept | Meaning |
|---------|---------|
| Sample space Ω | Possible outcomes |
| Event | Subset of Ω |
| P(A) | Probability of event A |
| Random variable X | Numeric outcome |
| PDF / PMF | Density / mass function |
| CDF | F(x) = P(X ≤ x) |
| Expectation E[X] | Mean |
| Variance Var(X) | Spread |
| Conditional P(A\|B) | Update given evidence |
| Independence | P(A∩B)=P(A)P(B) |

## Bayes' rule

```text
P(H|D) = P(D|H) P(H) / P(D)
```

## Code

```python
import numpy as np

rng = np.random.default_rng(0)
samples = rng.normal(loc=0.0, scale=1.0, size=10000)
print(samples.mean(), samples.var())

# Monte Carlo estimate of P(X > 1) for X ~ N(0,1)
print(np.mean(samples > 1))
```

## Uses in AI

- Softmax outputs as categorical distributions  
- Sampling / decoding  
- Uncertainty and calibration  
- Generative modeling  

## Common mistakes

- Treating model scores as calibrated probabilities without checking  
- Confusing independence with conditional independence  

## See also

- [10. Probability Distributions](../statistics/10-probability-distributions.md)  
- [21. Probability for ML](../ml-oriented/21-probability-for-ml.md)

---

## Continue

- **Section hub:** [Mathematics](README.md)
- **Math & Stats overview:** [Mathematics & Statistics](../README.md)
- Next topic: use the numbered list on the hub
