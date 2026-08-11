---
title: "4. Features & Labels"
description: "Inputs (X) and targets (y) — what the model sees and predicts."
domain: machine-learning
tags: [ml-basics, features]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 4. Features & Labels

> Inputs (X) and targets (y) — what the model sees and predicts.

## Definition

**Features** are the input representation of each example. **Labels** (targets) are the values you want to predict in supervised learning.

## Types of features

| Kind | Examples |
|------|----------|
| Numeric | age, latency_ms |
| Categorical | country, plan_tier |
| Text / embeddings | bag-of-words, vectors |
| Derived | ratios, lags, aggregates |

## Code

```python
import pandas as pd

df = pd.DataFrame({
    "latency_ms": [120, 80, 200],
    "plan": ["pro", "free", "pro"],
    "churned": [0, 1, 0],  # label
})
X = df[["latency_ms", "plan"]]
y = df["churned"]
```

## Uses

- Feature quality often beats algorithm choice on tabular data  
- Labels define the task — wrong labels ⇒ wrong model  

## Common mistakes

- Using future information as a feature (leakage)  
- High-cardinality IDs as raw categories without care

---

## Continue

- **Section hub:** [ML Basics](README.md)
- **ML overview:** [Machine Learning](../README.md)
