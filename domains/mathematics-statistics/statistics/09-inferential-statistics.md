---
title: "9. Inferential Statistics"
description: "From sample to population — estimation, uncertainty, and generalization."
domain: mathematics-statistics
tags: [statistics, inference]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 9. Inferential Statistics

> From sample to population — estimation, uncertainty, and generalization.

## Definition

**Inferential statistics** uses a sample to make statements about a population: estimates, confidence intervals, and hypothesis tests.

## Core ideas

| Idea | Meaning |
|------|---------|
| Population | Full set of interest |
| Sample | Observed subset |
| Estimator | Sample-based guess (e.g. mean) |
| Sampling distribution | Distribution of an estimator |
| Bias / variance | Estimator quality |
| Standard error | Spread of an estimator |

## Flow

```mermaid
flowchart LR
  Pop[Population] --> Sample[Sample]
  Sample --> Est[Estimate]
  Est --> Unc[Uncertainty]
  Unc --> Decision[Decision / CI / test]
```

## Code (bootstrap SE sketch)

```python
import numpy as np

rng = np.random.default_rng(0)
sample = rng.normal(0.7, 0.1, size=50)
boots = [rng.choice(sample, size=len(sample), replace=True).mean() for _ in range(1000)]
print("estimate", sample.mean())
print("bootstrap SE", np.std(boots, ddof=1))
```

## Uses

- Offline eval on a golden set → claim about production traffic  
- A/B test interpretation  
- Uncertainty on win rates  

## See also

- [11. Sampling](11-sampling.md) · [12. Hypothesis Testing](12-hypothesis-testing.md)

---

## Continue

- **Section hub:** [Statistics](README.md)
- **Math & Stats overview:** [Mathematics & Statistics](../README.md)
