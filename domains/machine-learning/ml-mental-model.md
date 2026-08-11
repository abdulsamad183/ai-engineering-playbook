---
title: "Machine Learning Mental Model"
description: "A practical map of ML problem types and the engineering loop."
domain: machine-learning
tags: [machine-learning]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# Machine Learning Mental Model

> A practical map of ML problem types and the engineering loop.

## Definition

ML systems map inputs to outputs by optimizing a loss on data. The engineering loop is: frame the task → collect/label data → train → evaluate → deploy → monitor → iterate.

## Why it matters

LLMs did not remove ML fundamentals. Intent classifiers, ranking models, anomaly detectors, and eval harnesses still use classical ML thinking.

## How it works

```mermaid
flowchart LR
  X[Features X] --> F[Model f]
  F --> Y[Prediction Y]
  Y --> L[Loss vs label]
  L --> U[Update parameters]
```

## Key principles

1. **Start with the decision** — What action changes if the model is wrong?
2. **Baselines first** — Rules and linear models reveal data issues early.
3. **Split before peeking** — Test set leakage invents fake progress.

## Common applications

| Application | Description |
|-------------|-------------|
| Routing | Classify queries to tools/models |
| Quality filters | Detect toxic/PII before generation |
| Ranking | Order retrieved chunks |

## Common mistakes

- Training on test data accidentally
- Ignoring class imbalance
- Shipping without a monitoring plan

## Further reading

- [Supervised learning essentials](supervised-learning-essentials.md)
- [MLOps & LLMOps](../mlops-llmops/README.md)
