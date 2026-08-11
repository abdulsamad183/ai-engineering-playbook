---
title: "5. Regular Expressions"
description: "Pattern matching for extraction, cleaning, and validation."
domain: natural-language-processing
tags: [text-processing, regex]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 5. Regular Expressions

> Pattern matching for extraction, cleaning, and validation.

## Definition

**Regex** finds and rewrites text patterns — emails, IDs, whitespace, light parsing.

## Code

```python
import re

re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}", text)
re.sub(r"\\s+", " ", text).strip()
```

## See also

- [Python Regex](../../python-engineering/topics/28-regular-expressions.md)

---

## Continue

- **Section hub:** [Text Processing](README.md)
- **Natural Language Processing overview:** [Natural Language Processing](../README.md)
