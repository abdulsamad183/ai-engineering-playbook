---
title: "3. TF-IDF"
description: "Weight rare informative terms higher than raw counts."
domain: natural-language-processing
tags: [text-repr, tfidf]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 3. TF-IDF

> Weight rare informative terms higher than raw counts.

## Definition

**TF-IDF** scales term frequency by inverse document frequency so common terms contribute less.

## Code

```python
from sklearn.feature_extraction.text import TfidfVectorizer

X = TfidfVectorizer(ngram_range=(1, 2)).fit_transform(corpus)
```

---

## Continue

- **Section hub:** [Text Representation](README.md)
- **Natural Language Processing overview:** [Natural Language Processing](../README.md)
