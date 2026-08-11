---
title: "16. Bayesian Statistics"
description: "Prior, likelihood, posterior — updating beliefs with data."
domain: mathematics-statistics
tags: [statistics, bayesian]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 16. Bayesian Statistics

> Prior, likelihood, posterior — updating beliefs with data.

## Definition

**Bayesian statistics** treats parameters as uncertain and updates a **prior** with data via the **likelihood** to get a **posterior**.

```text
posterior ∝ likelihood × prior
```

## Core vocabulary

| Term | Meaning |
|------|---------|
| Prior | Belief before data |
| Likelihood | P(data \| params) |
| Posterior | Belief after data |
| MAP | Maximum a posteriori |
| Predictive | Distribution of new data |

## Code (Beta-Binomial conjugacy sketch)

```python
# Prior Beta(a,b); observe s successes in n trials
# Posterior Beta(a+s, b+n-s)
a, b = 2, 2
s, n = 7, 10
post_a, post_b = a + s, b + n - s
post_mean = post_a / (post_a + post_b)
print("posterior mean", post_mean)
```

## Uses

- Small-data inference with priors  
- A/B with sequential updates  
- Uncertainty in calibration / bandits  

## See also

- [4. Probability Theory](../mathematics/04-probability-theory.md)

---

## Continue

- **Section hub:** [Statistics](README.md)
- **Math & Stats overview:** [Mathematics & Statistics](../README.md)
