---
title: "Matplotlib: Labels, Legends & Style"
description: "Titles, axis labels, legends, grids, and stylesheets."
domain: python-frameworks-libraries
tags: [matplotlib, style]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# Matplotlib: Labels, Legends & Style

> Titles, axis labels, legends, grids, and stylesheets.

## Definition

Readable charts need **labels**, **legends**, and consistent **style**.

## Important APIs

| API | Use |
|-----|-----|
| `set_title`, `set_xlabel`, `set_ylabel` | Text |
| `legend` | Series labels |
| `grid` | Gridlines |
| `plt.style.use` | Theme |
| `tick_params` | Tick styling |

## Code

```python
import matplotlib.pyplot as plt

plt.style.use("seaborn-v0_8-whitegrid")
fig, ax = plt.subplots()
ax.plot([0, 1, 2], [0.2, 0.6, 0.9], label="model A")
ax.plot([0, 1, 2], [0.3, 0.5, 0.7], label="model B")
ax.set_title("Quality over time")
ax.set_xlabel("week"); ax.set_ylabel("score")
ax.legend(loc="lower right")
fig.savefig("styled.png", dpi=120, bbox_inches="tight")
plt.close(fig)
```

---

## Continue

- **Hub:** [Matplotlib hub](README.md)
- **Frameworks overview:** [Python Frameworks & Libraries](../README.md)
