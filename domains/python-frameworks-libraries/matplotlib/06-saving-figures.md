---
title: "Matplotlib: Saving Figures"
description: "Export PNG/SVG/PDF for reports and docs."
domain: python-frameworks-libraries
tags: [matplotlib, export]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# Matplotlib: Saving Figures

> Export PNG/SVG/PDF for reports and docs.

## Definition

`Figure.savefig` writes plots to disk. Choose format by use: PNG (slides), SVG/PDF (vector docs).

## Important parameters

| Param | Use |
|-------|-----|
| `dpi` | Raster resolution |
| `bbox_inches="tight"` | Trim whitespace |
| `transparent` | Transparent background |
| `format` | `png`, `svg`, `pdf` |

## Code

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot([1, 2, 3], [3, 2, 5])
fig.savefig("plot.png", dpi=150, bbox_inches="tight")
fig.savefig("plot.svg", bbox_inches="tight")
plt.close(fig)
```

## Tip

Always `plt.close(fig)` in batch report generation to avoid memory leaks.

---

## Continue

- **Hub:** [Matplotlib hub](README.md)
- **Frameworks overview:** [Python Frameworks & Libraries](../README.md)
