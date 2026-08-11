---
title: "5. Tensor Parallelism"
description: "Shard large matmuls across GPUs in a block."
domain: llm-engineering
tags: [infra, tp]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 5. Tensor Parallelism

> Shard large matmuls across GPUs in a block.

## Definition

**Tensor parallelism** splits individual weight matrices so layers span multiple GPUs with collective ops.

---

## Continue

- **Section hub:** [LLM Infrastructure](README.md)
- **LLM overview:** [Large Language Models](../README.md)
