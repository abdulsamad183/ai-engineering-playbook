---
title: "Transformer Concepts Cheat Sheet"
description: "Quick reference for transformer architecture — attention, KV cache, positional encoding, and model variants."
domain: papers
tags: [cheat-sheet, transformers, attention, phase-papers]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - ../domains/papers/attention-is-all-you-need.md
keywords: [transformer, self-attention, KV cache, positional encoding]
author: hp
---

# Transformer Concepts Cheat Sheet

> See [Attention Is All You Need](../domains/papers/attention-is-all-you-need.md).

## Key Concepts

| Concept | One-Line Definition |
|---------|-------------------|
| Self-attention | Each token attends to all tokens — parallel, O(n²) |
| Multi-head attention | Multiple attention subspaces in parallel |
| Scaled dot-product | `softmax(QK^T / √d_k) · V` — prevents saturation |
| Positional encoding | Injects token order (sinusoidal, RoPE, ALiBi) |
| Causal masking | Decoder sees only past tokens (autoregressive) |
| KV cache | Stores K/V tensors during inference — faster generation |
| Layer norm + residual | Training stability across deep stacks |

## Model Variants

| Variant | Examples | Use For |
|---------|----------|---------|
| Encoder-only | BERT, embedding models | Classification, embeddings, reranking |
| Decoder-only | GPT, Llama, Claude | Chat, completion, agents |
| Encoder-decoder | T5, BART | Translation, summarization |

## Complexity & Memory

| Factor | Impact |
|--------|--------|
| Sequence length n | Attention: O(n²) |
| Hidden dim d | Linear scaling |
| Num layers L | Linear scaling |
| KV cache | `2 × L × n × d × bytes` per request |

## Inference Optimization

| Technique | What It Does |
|-----------|-------------|
| KV cache | Skip recompute of prior tokens |
| Flash Attention | IO-aware attention — faster, less memory |
| Quantization (INT8/FP8) | Smaller weights, faster inference |
| Speculative decoding | Draft model + verify with large model |

## Do's and Don'ts

| Do | Don't |
|----|-------|
| Budget context by attention cost | Assume unlimited context is free |
| Use encoder models for embeddings | Use chat models for embeddings |
| Account for KV cache in memory planning | Ignore inference memory |
| Match model type to task | Treat all LLMs identically |

## Useful Links

- [Attention Is All You Need](../domains/papers/attention-is-all-you-need.md)
- [LLM Engineering](../domains/llm-engineering/README.md)

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Initial cheat sheet |
