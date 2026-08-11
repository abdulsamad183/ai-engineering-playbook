---
title: "1. Tokenization"
description: "Split text into model units — words, subwords, or characters."
domain: natural-language-processing
tags: [text-processing, tokenize]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 1. Tokenization

> Split text into model units — words, subwords, or characters.

## Definition

**Tokenization** segments text into tokens. Modern NLP usually uses subword tokenizers (BPE, WordPiece, Unigram).

## Code

```python
text = "Transformers are great."
print(text.lower().split())  # naive word tokens
# Prefer model tokenizer: tokenizer.encode(text)
```

## See also

- [Transformers · Tokenizers](../../transformers/transformers-in-practice/02-tokenizers.md)

---

## Continue

- **Section hub:** [Text Processing](README.md)
- **Natural Language Processing overview:** [Natural Language Processing](../README.md)
