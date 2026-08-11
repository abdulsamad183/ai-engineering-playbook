---
title: "7. Handling Outliers"
description: "Detect and treat extreme values without deleting real rare events blindly."
domain: machine-learning
tags: [feature-engineering, outliers]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 7. Handling Outliers

> Detect and treat extreme values without deleting real rare events blindly.

## Definition

**Outliers** are extreme points. Treat via winsorizing, robust scalers, log transforms, or robust models — after asking if they are errors or rare truths.

## Tactics

| Tactic | Notes |
|--------|-------|
| Cap / winsorize | Clip to percentiles |
| RobustScaler | Less sensitive |
| Tree models | More robust to extremes |
| Separate model | Rare-event path |

## Code

```python
import numpy as np

lo, hi = np.percentile(x, [1, 99])
x_capped = np.clip(x, lo, hi)
```

---

## Continue

- **Section hub:** [Feature Engineering](README.md)
- **ML overview:** [Machine Learning](../README.md)
