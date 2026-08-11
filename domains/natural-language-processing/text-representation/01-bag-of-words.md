---
title: "1. Bag of Words"
description: "Sparse count vectors — ignore order, keep word presence/frequency."
domain: natural-language-processing
tags: [text-repr, bow]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 1. Bag of Words

> Sparse count vectors — ignore order, keep word presence/frequency.

## Definition

**Bag of Words (BoW)** represents a document as token counts (or binary presence) over a vocabulary.

## Code

```python
from sklearn.feature_extraction.text import CountVectorizer

X = CountVectorizer().fit_transform(["I love NLP", "NLP loves data"])
```

---

## Continue

- **Section hub:** [Text Representation](README.md)
- **Natural Language Processing overview:** [Natural Language Processing](../README.md)
