---
title: "Pandas: Reading & Writing Data"
description: "CSV, JSON, Parquet I/O — the gateway to real datasets."
domain: python-frameworks-libraries
tags: [pandas, io]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# Pandas: Reading & Writing Data

> CSV, JSON, Parquet I/O — the gateway to real datasets.

## Definition

Pandas **I/O functions** load and save tabular data from files and buffers.

## Important functions

| Function | Use |
|----------|-----|
| `pd.read_csv` | CSV/TSV |
| `pd.read_json` | JSON/NDJSON |
| `pd.read_parquet` | Parquet |
| `DataFrame.to_csv` | Write CSV |
| `DataFrame.to_parquet` | Write Parquet |
| `DataFrame.to_dict` | Python dict records |

## Code

```python
import pandas as pd
from pathlib import Path

df = pd.DataFrame({"id": [1, 2], "text": ["hello", "world"]})
path = Path("sample.csv")
df.to_csv(path, index=False)

loaded = pd.read_csv(path)
print(loaded)

# Useful read_csv options
# pd.read_csv(path, usecols=["id", "text"], dtype={"id": "int64"})
# pd.read_json("traces.jsonl", lines=True)
```

## Tips

- Prefer Parquet for large numeric tables
- Set `index=False` unless the index is meaningful
- Parse dates with `parse_dates=["ts"]`

---

## Continue

- **Hub:** [Pandas hub](README.md)
- **Frameworks overview:** [Python Frameworks & Libraries](../README.md)
