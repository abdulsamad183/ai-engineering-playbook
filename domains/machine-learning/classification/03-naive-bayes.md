---
title: "3. Naive Bayes"
description: "Fast probabilistic classifiers assuming feature independence given the class."
domain: machine-learning
tags: [classification, naive-bayes]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 3. Naive Bayes

> Fast probabilistic classifiers assuming feature independence given the class.

## Definition

**Naive Bayes** applies Bayes' rule with a strong independence assumption. Variants: Gaussian, Multinomial, Bernoulli — common for text counts.

## Code

```python
from sklearn.naive_bayes import MultinomialNB

clf = MultinomialNB()
clf.fit(X_train_counts, y_train)
```

## Uses

- Text classification baselines  
- Very fast training  
- Solid when features are roughly conditionally independent  

## See also

- [Probability for ML](../../mathematics-statistics/ml-oriented/21-probability-for-ml.md)

---

## Continue

- **Section hub:** [Classification](README.md)
- **ML overview:** [Machine Learning](../README.md)
