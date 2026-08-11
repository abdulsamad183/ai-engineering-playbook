---
title: "Matplotlib: Figures & Axes"
description: "Core objects — Figure, Axes, and pyplot vs OO API."
domain: python-frameworks-libraries
tags: [matplotlib, figures]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# Matplotlib: Figures & Axes

> Core objects — Figure, Axes, and pyplot vs OO API.

## Definition

- **`Figure`**: the whole window/page
- **`Axes`**: one plotting area with x/y (or 3D) coordinates
- **`pyplot` (`plt`)**: convenience wrappers

## Key classes

| Class | Role |
|-------|------|
| `matplotlib.figure.Figure` | Canvas |
| `matplotlib.axes.Axes` | Single plot |
| `pyplot` | State-based API |

## Code

```python
import matplotlib.pyplot as plt

# OO style (recommended)
fig, ax = plt.subplots(figsize=(6, 4))
ax.plot([1, 2, 3], [1, 4, 9])
ax.set_title("Squares")
# plt.show()  # in scripts/notebooks
fig.savefig("demo.png", dpi=120, bbox_inches="tight")
plt.close(fig)
```

## Uses

- Build reusable plotting helpers for eval reports

---

## Continue

- **Hub:** [Matplotlib hub](README.md)
- **Frameworks overview:** [Python Frameworks & Libraries](../README.md)
