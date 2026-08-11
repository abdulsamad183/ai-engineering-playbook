---
title: "2. Feature Transformation"
description: "Logs, powers, Binning — reshape distributions for better linear fit."
domain: machine-learning
tags: [feature-engineering, transform]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 2. Feature Transformation

> Logs, powers, Binning — reshape distributions for better linear fit.

## Definition

**Feature transforms** change the representation of a column: log1p, Box-Cox/Yeo-Johnson, quantile maps, binning.

## Code

```python
import numpy as np
from sklearn.preprocessing import PowerTransformer

X_log = np.log1p(X_positive)
pt = PowerTransformer(method="yeo-johnson")
X_t = pt.fit_transform(X_train)
```

## Uses

- Heavy-tailed spends / latencies  
- Stabilize variance for linear models

---

## Continue

- **Section hub:** [Feature Engineering](README.md)
- **ML overview:** [Machine Learning](../README.md)
