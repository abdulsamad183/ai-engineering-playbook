---
title: "1. Introduction to Machine Learning"
description: "What ML is, problem types, and when classical ML beats rules or deep learning."
domain: machine-learning
tags: [ml-basics, introduction]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 1. Introduction to Machine Learning

> What ML is, problem types, and when classical ML beats rules or deep learning.

## Definition

**Machine learning** builds systems that improve on a task from data instead of only hard-coded rules. You choose a model class, fit it on examples, and evaluate on held-out data.

## Learning paradigms

| Type | Signal | Examples |
|------|--------|----------|
| Supervised | Labels | Regression, classification |
| Unsupervised | No labels | Clustering, PCA |
| Semi-supervised | Few labels | Pseudo-labeling |
| Reinforcement | Rewards | Bandits, agents |

## When to use classical ML

- Tabular data with clear features  
- Strong baselines before deep learning  
- Interpretability and fast iteration matter  

## How it works

```mermaid
flowchart LR
  Data[Data] --> Features[Features]
  Features --> Model[Model]
  Model --> Pred[Predictions]
  Pred --> Eval[Evaluate]
```

## Code sketch

```python
# Supervised pattern (sklearn-style)
# model.fit(X_train, y_train)
# preds = model.predict(X_test)
```

## Common mistakes

- Jumping to deep learning without a linear/tree baseline  
- Ignoring data leakage and split discipline

---

## Continue

- **Section hub:** [ML Basics](README.md)
- **ML overview:** [Machine Learning](../README.md)
