---
title: "1. Anomaly Detection"
description: "Find rare or weird points — isolation forests, density, and reconstruction errors."
domain: machine-learning
tags: [misc, anomaly]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 1. Anomaly Detection

> Find rare or weird points — isolation forests, density, and reconstruction errors.

## Definition

**Anomaly detection** flags observations that differ from normal patterns (fraud, outages, bad sensors).

## Approaches

| Approach | Examples |
|----------|----------|
| Unsupervised | IsolationForest, LOF, One-Class SVM |
| Density / GMM | Low log-likelihood |
| Supervised | Rare-class classifier if labels exist |
| Deep | Autoencoder reconstruction error |

## Code

```python
from sklearn.ensemble import IsolationForest

clf = IsolationForest(contamination=0.02, random_state=42)
scores = clf.fit_predict(X)  # -1 anomaly, 1 normal
```

## Tips

- Contamination rate is a business choice  
- Evaluate with precision@k when positives are rare

---

## Continue

- **Section hub:** [Miscellaneous ML](README.md)
- **ML overview:** [Machine Learning](../README.md)
