---
title: "4. Text Normalization"
description: "Canonicalize variants — case, unicode, numbers, and slang carefully."
domain: natural-language-processing
tags: [nlp-basics, normalize]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 4. Text Normalization

> Canonicalize variants — case, unicode, numbers, and slang carefully.

## Definition

**Normalization** reduces superficial variation (case, accents, spelling variants) so models see more consistent forms.

## Examples

| Transform | Caution |
|-----------|---------|
| Lowercasing | May hurt NER (US vs us) |
| Unicode NFKC | Good default for many apps |
| Number normalization | Task-specific |
| Spelling correction | Can destroy meaning |

## Code

```python
import unicodedata

def normalize(s: str) -> str:
    s = unicodedata.normalize("NFKC", s)
    return " ".join(s.split())
```

---

## Continue

- **Section hub:** [NLP Basics](README.md)
- **Natural Language Processing overview:** [Natural Language Processing](../README.md)
