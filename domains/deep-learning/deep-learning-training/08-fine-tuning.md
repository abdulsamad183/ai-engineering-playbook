---
title: "8. Fine-Tuning"
description: "Update pretrained parameters on your task — full, partial, or parameter-efficient."
domain: deep-learning
tags: [training, fine-tuning]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 8. Fine-Tuning

> Update pretrained parameters on your task — full, partial, or parameter-efficient.

## Definition

**Fine-tuning** continues training pretrained weights on downstream data. Can update all weights or a small adapter set (LoRA, etc.).

## Strategies

| Strategy | Notes |
|----------|-------|
| Full FT | Maximum flexibility; more compute |
| Head-only | Fast baseline |
| PEFT / LoRA | Efficient for large models |

## See also

- [LLM Fine-Tuning](../../llm-fine-tuning/README.md)

---

## Continue

- **Section hub:** [Deep Learning Training](README.md)
- **DL overview:** [Deep Learning](../README.md)
