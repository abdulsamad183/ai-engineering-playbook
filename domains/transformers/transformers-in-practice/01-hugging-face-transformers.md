---
title: "1. Hugging Face Transformers"
description: "Load models/tokenizers — the practical default API."
domain: transformers
tags: [practice, hf]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 1. Hugging Face Transformers

> Load models/tokenizers — the practical default API.

## Definition

The **`transformers`** library standardizes model loading, configs, and trainer/pipeline utilities across architectures.

## Sketch

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

tok = AutoTokenizer.from_pretrained("gpt2")
model = AutoModelForCausalLM.from_pretrained("gpt2")
```

---

## Continue

- **Section hub:** [Transformers in Practice](README.md)
- **Transformers overview:** [Transformers](../README.md)
