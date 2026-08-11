---
title: "File Handling"
description: "Read and write files safely — text/binary modes, pathlib, context managers, and large-file patterns."
domain: python-engineering
tags: [python, files, pathlib, tutorial]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# File Handling

> Read and write files safely — text/binary modes, pathlib, context managers, and large-file patterns.

## Definition

**File handling** is reading from and writing to files on disk (or file-like objects). Prefer **`pathlib.Path`** + **`with open(...)`** so files close even when errors occur.

## Uses

- Load prompts, configs, datasets
- Write logs, exports, evaluation reports
- Stream large corpora line-by-line

## Modes (common)

| Mode | Meaning |
|------|---------|
| `"r"` | Read text (default) |
| `"w"` | Write text (truncate) |
| `"a"` | Append text |
| `"x"` | Exclusive create |
| `"rb"`/`"wb"` | Binary |
| `"+"` | Read/write combo |

## Code examples

```python
from pathlib import Path

path = Path("example.txt")

# Write text (UTF-8)
path.write_text("hello\nworld\n", encoding="utf-8")

# Read all
text = path.read_text(encoding="utf-8")
print(text)

# Stream lines (memory friendly)
with path.open("r", encoding="utf-8") as f:
    for line in f:
        print(line.rstrip())
```

```python
# JSON / structured data
import json
data_path = Path("data.json")
data_path.write_text(json.dumps({"k": 5}, indent=2), encoding="utf-8")
obj = json.loads(data_path.read_text(encoding="utf-8"))
print(obj["k"])
```

```python
# Binary
bpath = Path("blob.bin")
bpath.write_bytes(b"\x00\x01\x02")
print(bpath.read_bytes())
```

```python
# Safe write pattern (write temp then replace)
def atomic_write(path: Path, content: str) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(content, encoding="utf-8")
    tmp.replace(path)

atomic_write(Path("safe.txt"), "ok\n")
```

```python
# Directory ops
out = Path("outputs")
out.mkdir(parents=True, exist_ok=True)
for p in Path(".").glob("*.md"):
    print("md:", p.name)
```

## Always specify encoding

On some platforms default encoding is not UTF-8. **Always pass `encoding="utf-8"`** for text.

## Common mistakes

- Forgetting to close files (use `with`)
- Loading a 10GB file with `.read()` 
- Hard-coded backslashes instead of `Path`

---

## Continue

- **Previous:** [Exception Handling](18-exception-handling.md)
- **Hub:** [Python topics](../README.md)
- **Next:** [Modules & Packages](20-modules-packages.md)
- **AI production guide:** [Python for AI Engineering](../python-for-ai-engineering.md)
