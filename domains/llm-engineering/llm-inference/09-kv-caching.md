---
title: "9. KV Caching"
description: "Inference-time cache for attention speed."
domain: llm-engineering
tags: [inference, kvc]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 9. KV Caching

> Inference-time cache for attention speed.

## Definition

Serving stacks keep a **KV cache** per request/sequence to avoid O(T²) recompute each new token.

---

## Continue

- **Section hub:** [LLM Inference](README.md)
- **LLM overview:** [Large Language Models](../README.md)
