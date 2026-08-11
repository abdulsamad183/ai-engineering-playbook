---
title: "9. Bias-Variance Tradeoff"
description: "Error decomposition — why ensembles and regularization help."
domain: machine-learning
tags: [ml-basics, bias-variance]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 9. Bias-Variance Tradeoff

> Error decomposition — why ensembles and regularization help.

## Definition

Expected prediction error decomposes (informally) into **bias² + variance + noise**. Simpler models → higher bias, lower variance; flexible models → opposite.

## Intuition

| Choice | Bias | Variance |
|--------|------|----------|
| Linear on nonlinear data | High | Low |
| Deep tree on small data | Low | High |
| Regularized / bagged | Balanced | Balanced |

## Practical takeaways

- Cross-validation estimates generalization, not just train fit  
- Ensembles (bagging) cut variance; boosting cuts bias (carefully)  
- Always plot learning curves when unsure  

## See also

- [Statistical Learning Theory](../../mathematics-statistics/ml-oriented/24-statistical-learning-theory.md)
- [Learning Curves](../model-evaluation/08-learning-curves.md)

---

## Continue

- **Section hub:** [ML Basics](README.md)
- **ML overview:** [Machine Learning](../README.md)
