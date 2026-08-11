---
title: "5. Dense Networks"
description: "DenseNet-style connectivity — concatenate features from earlier layers."
domain: deep-learning
tags: [architectures, densenet]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 5. Dense Networks

> DenseNet-style connectivity — concatenate features from earlier layers.

## Definition

**Dense networks** (DenseNet family) connect each layer to all subsequent layers via concatenation, encouraging feature reuse and stronger gradient flow.

## Contrast

| ResNet | DenseNet |
|--------|----------|
| Add skip | Concatenate skips |
| Residual function | Feature reuse |

## When to know this

- Reading vision papers / backbones  
- Understanding connectivity patterns beyond plain stacks

---

## Continue

- **Section hub:** [Neural Network Architectures](README.md)
- **DL overview:** [Deep Learning](../README.md)
