---
title: "6. Transfer Learning"
description: "Reuse pretrained CNN features — freeze, fine-tune, or replace the head."
domain: deep-learning
tags: [cnn, transfer]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 6. Transfer Learning

> Reuse pretrained CNN features — freeze, fine-tune, or replace the head.

## Definition

**Transfer learning** starts from weights trained on a large dataset (e.g. ImageNet) and adapts them to your task with less data/compute.

## Patterns

| Pattern | When |
|---------|------|
| Feature extractor | Freeze backbone, train head |
| Partial fine-tune | Unfreeze top blocks |
| Full fine-tune | Enough data + careful LR |

## See also

- [Transfer Learning (Training)](../deep-learning-training/07-transfer-learning.md) · [Fine-Tuning](../deep-learning-training/08-fine-tuning.md)

---

## Continue

- **Section hub:** [Convolutional Neural Networks](README.md)
- **DL overview:** [Deep Learning](../README.md)
