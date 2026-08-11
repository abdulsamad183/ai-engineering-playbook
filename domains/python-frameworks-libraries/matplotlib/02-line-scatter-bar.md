---
title: "Matplotlib: Line, Scatter & Bar"
description: "The three most common chart types for AI metrics."
domain: python-frameworks-libraries
tags: [matplotlib, charts]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# Matplotlib: Line, Scatter & Bar

> The three most common chart types for AI metrics.

## Definition

Common plot types map metrics to visual encodings: lines (trends), scatter (relationships), bars (categories).

## Important methods

| Method | Use |
|--------|-----|
| `Axes.plot` | Lines |
| `Axes.scatter` | Points |
| `Axes.bar` / `barh` | Categories |
| `Axes.fill_between` | Bands / CI |

## Code

```python
import numpy as np
import matplotlib.pyplot as plt

steps = np.arange(1, 11)
loss = 1 / steps

fig, ax = plt.subplots()
ax.plot(steps, loss, marker="o", label="train loss")
ax.scatter([3, 7], [1/3, 1/7], color="red", zorder=3)
ax.legend()
ax.set_xlabel("step"); ax.set_ylabel("loss")
fig.savefig("loss.png", dpi=120, bbox_inches="tight")
plt.close(fig)

models = ["a", "b", "c"]
acc = [0.81, 0.76, 0.88]
fig, ax = plt.subplots()
ax.bar(models, acc)
ax.set_ylim(0, 1)
fig.savefig("acc.png", dpi=120, bbox_inches="tight")
plt.close(fig)
```

---

## Continue

- **Hub:** [Matplotlib hub](README.md)
- **Frameworks overview:** [Python Frameworks & Libraries](../README.md)
