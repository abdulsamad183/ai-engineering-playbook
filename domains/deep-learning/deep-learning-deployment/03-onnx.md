---
title: "3. ONNX"
description: "Portable model IR — export once, run on many inference runtimes."
domain: deep-learning
tags: [deployment, onnx]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 3. ONNX

> Portable model IR — export once, run on many inference runtimes.

## Definition

**ONNX** is an open interchange format for ML models. Export from PyTorch/TF, run with ONNX Runtime or other engines.

## Sketch

```python
# torch.onnx.export(model, example_input, "model.onnx", ...)
```

## Why use it

- Decouple training framework from serving stack

---

## Continue

- **Section hub:** [Deep Learning Deployment](README.md)
- **DL overview:** [Deep Learning](../README.md)
