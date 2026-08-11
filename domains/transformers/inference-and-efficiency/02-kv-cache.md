---
title: "2. KV Cache"
description: "Reuse past keys/values — the main latency win for generation."
domain: transformers
tags: [inference, kv]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 2. KV Cache

> Reuse past keys/values — the main latency win for generation.

## Definition

A **KV cache** stores attention K/V from previous tokens so decoding doesn't recompute the full past each step.

---

## Continue

- **Section hub:** [Inference & Efficiency](README.md)
- **Transformers overview:** [Transformers](../README.md)
