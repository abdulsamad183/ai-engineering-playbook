# Pandas

> Tabular data analysis — Series, DataFrames, wrangling, groupby, and I/O for eval sets and logs.

**Prerequisites:** [Python](../../python-engineering/README.md) · [NumPy](../numpy/README.md)  
**Part of:** [Python Frameworks & Libraries](../README.md)

---

## Definition

**Pandas** provides labeled 1D (`Series`) and 2D (`DataFrame`) structures with rich indexing, missing-data handling, joins, and aggregations. It is the default tool for CSV/Parquet eval datasets, trace analysis, and feature tables.

---

## When to use Pandas

| Use | Example |
|-----|---------|
| Tabular datasets | golden Q&A CSVs |
| Cleaning | nulls, dtypes, duplicates |
| Aggregation | metrics by model/version |
| Joins | predictions ⋈ labels |

---

## Learning path

```mermaid
flowchart LR
  A[Series & DataFrame] --> B[IO & select]
  B --> C[Clean & missing]
  C --> D[GroupBy / merge]
  D --> E[Apply & time]
```

---

## Topics

| # | Topic | Document |
|---|-------|----------|
| 1 | Series & DataFrame | [01-series-dataframe.md](01-series-dataframe.md) |
| 2 | Reading & writing data | [02-io-read-write.md](02-io-read-write.md) |
| 3 | Selecting & filtering | [03-selecting-filtering.md](03-selecting-filtering.md) |
| 4 | Missing data | [04-missing-data.md](04-missing-data.md) |
| 5 | GroupBy & aggregation | [05-groupby-aggregation.md](05-groupby-aggregation.md) |
| 6 | Merge, join & concat | [06-merge-join-concat.md](06-merge-join-concat.md) |
| 7 | Apply & transforms | [07-apply-transforms.md](07-apply-transforms.md) |
| 8 | Important APIs cheat sheet | [08-important-apis.md](08-important-apis.md) |

---

## Related

- [NumPy](../numpy/README.md) · [Matplotlib](../matplotlib/README.md) · [LLM Evaluation](../../ai-evaluation/README.md)
