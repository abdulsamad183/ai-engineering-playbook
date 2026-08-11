---
title: "Matplotlib: Histograms & Heatmaps"
description: "Distributions and matrix visualizations."
domain: python-frameworks-libraries
tags: [matplotlib, heatmap]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# Matplotlib: Histograms & Heatmaps

> Distributions and matrix visualizations.

## Definition

**Histograms** show distributions; **heatmaps** (`imshow` / `pcolormesh`) show matrices — confusion matrices, attention, correlation.

## Important methods

| Method | Use |
|--------|-----|
| `Axes.hist` | Histogram |
| `Axes.imshow` | Image/matrix |
| `Axes.hist2d` | 2D density |
| `fig.colorbar` | Scale bar |

## Code

```python
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
scores = rng.normal(0.7, 0.15, size=500)

fig, ax = plt.subplots()
ax.hist(scores, bins=20, color="steelblue", edgecolor="white")
ax.set_title("Score distribution")
fig.savefig("hist.png", dpi=120)
plt.close(fig)

mat = np.array([[50, 2], [5, 43]])
fig, ax = plt.subplots()
im = ax.imshow(mat, cmap="Blues")
ax.set_xticks([0, 1], ["pred0", "pred1"])
ax.set_yticks([0, 1], ["lab0", "lab1"])
fig.colorbar(im, ax=ax)
fig.savefig("cm.png", dpi=120)
plt.close(fig)
```

---

## Continue

- **Hub:** [Matplotlib hub](README.md)
- **Frameworks overview:** [Python Frameworks & Libraries](../README.md)
