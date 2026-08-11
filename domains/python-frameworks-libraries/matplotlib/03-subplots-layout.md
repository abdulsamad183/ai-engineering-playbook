---
title: "Matplotlib: Subplots & Layout"
description: "Multiple axes, gridspec, and tight layouts."
domain: python-frameworks-libraries
tags: [matplotlib, subplots]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# Matplotlib: Subplots & Layout

> Multiple axes, gridspec, and tight layouts.

## Definition

**Subplots** place multiple Axes on one Figure for side-by-side comparisons.

## Important APIs

| API | Use |
|-----|-----|
| `plt.subplots(r, c)` | Grid of axes |
| `fig.add_subplot` | Manual add |
| `tight_layout` / `constrained_layout` | Spacing |
| `sharex` / `sharey` | Linked axes |

## Code

```python
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(8, 3), constrained_layout=True)
axes[0].plot([1, 2, 3], [1, 2, 3])
axes[0].set_title("A")
axes[1].bar(["x", "y"], [3, 5])
axes[1].set_title("B")
fig.savefig("grid.png", dpi=120)
plt.close(fig)
```

---

## Continue

- **Hub:** [Matplotlib hub](README.md)
- **Frameworks overview:** [Python Frameworks & Libraries](../README.md)
