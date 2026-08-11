---
title: "5. Parameters & Model Size"
description: "Billions of weights — quality, cost, and memory tradeoffs."
domain: llm-engineering
tags: [fundamentals, params]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 5. Parameters & Model Size

> Billions of weights — quality, cost, and memory tradeoffs.

## Definition

**Parameter count** approximates capacity/cost. Memory ≈ params × bytes/param (+ KV cache, activations).

## Rules of thumb

| Size class | Typical use |
|------------|-------------|
| 1–8B | Edge / cheap local |
| 7–70B | Strong general apps |
| 100B+ | Frontier quality (API/cluster) |

---

## Continue

- **Section hub:** [LLM Fundamentals](README.md)
- **LLM overview:** [Large Language Models](../README.md)
