---
title: "6. Data Augmentation"
description: "Synthesize variety — crops, flips, mixup, SpecAugment, NLP noise."
domain: deep-learning
tags: [training, augmentation]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 6. Data Augmentation

> Synthesize variety — crops, flips, mixup, SpecAugment, NLP noise.

## Definition

**Data augmentation** applies label-preserving (or carefully designed) transforms to enlarge effective dataset diversity and reduce overfitting.

## Examples

| Domain | Augmentations |
|--------|---------------|
| Vision | Flip, crop, color jitter, RandAugment |
| Audio | Time/freq masks |
| Text | Token dropout, back-translation (careful) |

## Tip

- Augment train only; keep eval deterministic

---

## Continue

- **Section hub:** [Deep Learning Training](README.md)
- **DL overview:** [Deep Learning](../README.md)
