---
title: "3. Distributed Training"
description: "Data parallel and beyond — scale across GPUs and nodes."
domain: deep-learning
tags: [optimization, distributed]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 3. Distributed Training

> Data parallel and beyond — scale across GPUs and nodes.

## Definition

**Distributed training** splits work across devices (DDP data parallel, FSDP/tensor parallel for huge models).

## Starter mental model

| Mode | Idea |
|------|------|
| Data parallel (DDP) | Same model, split batches |
| FSDP / ZeRO | Shard parameters/states |
| Pipeline / tensor parallel | Split the model itself |

## See also

- [MLOps & LLMOps](../../mlops-llmops/README.md)

---

## Continue

- **Section hub:** [Deep Learning Optimization](README.md)
- **DL overview:** [Deep Learning](../README.md)
