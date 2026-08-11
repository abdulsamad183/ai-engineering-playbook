---
title: "5. Quantization"
description: "Lower-bit weights/activations — INT8/INT4 for fast inference."
domain: deep-learning
tags: [optimization, quantization]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 5. Quantization

> Lower-bit weights/activations — INT8/INT4 for fast inference.

## Definition

**Quantization** stores and/or computes with fewer bits. Can be post-training (PTQ) or quantization-aware training (QAT).

## Practice

- Validate quality on a real eval set after quantizing  
- Prefer hardened tooling (bitsandbytes, AWQ, TensorRT, ONNX Runtime)

---

## Continue

- **Section hub:** [Deep Learning Optimization](README.md)
- **DL overview:** [Deep Learning](../README.md)
