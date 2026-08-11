---
title: "2. Inference Optimization"
description: "Cut latency/cost — batching, KV tricks, kernels, and smaller models."
domain: deep-learning
tags: [deployment, inference]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 2. Inference Optimization

> Cut latency/cost — batching, KV tricks, kernels, and smaller models.

## Definition

**Inference optimization** improves tokens/sec or ms/request via graph compilers, batching, quantization, caching, and better kernels.

## Levers

- Dynamic batching  
- Precision (FP16/INT8)  
- Engine choice (ONNX Runtime, TensorRT, vLLM for LLMs)

---

## Continue

- **Section hub:** [Deep Learning Deployment](README.md)
- **DL overview:** [Deep Learning](../README.md)
