---
title: "5. Gaussian Mixture Models"
description: "Soft clusters as a weighted sum of Gaussians — EM fitting."
domain: machine-learning
tags: [unsupervised, gmm]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 5. Gaussian Mixture Models

> Soft clusters as a weighted sum of Gaussians — EM fitting.

## Definition

A **GMM** models data as a mixture of multivariate Gaussians. EM estimates means, covariances, and mixture weights; assignments can be soft (responsibilities).

## Code

```python
from sklearn.mixture import GaussianMixture

gmm = GaussianMixture(n_components=3, covariance_type="full", random_state=42)
labels = gmm.fit_predict(X_scaled)
proba = gmm.predict_proba(X_scaled)
```

## Uses

- Soft clustering  
- Simple generative density / anomaly scores (`score_samples`)

---

## Continue

- **Section hub:** [Unsupervised Learning](README.md)
- **ML overview:** [Machine Learning](../README.md)
