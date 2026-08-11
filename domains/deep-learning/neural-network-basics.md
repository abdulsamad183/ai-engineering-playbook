---
title: "Neural Network Basics"
description: "Layers, activations, and what a network is computing."
domain: deep-learning
tags: [deep-learning]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# Neural Network Basics

> Layers, activations, and what a network is computing.

## Definition

A neural network composes simple functions (linear transforms + nonlinear activations) into a flexible predictor. Depth and width control capacity; activations (ReLU, GELU) enable nonlinear decision boundaries.

## Why it matters

Transformers are still neural networks. Understanding layers and representations makes attention and fine-tuning far less mysterious.

## How it works

```mermaid
flowchart LR
  x[x] --> Linear[Wx + b]
  Linear --> Act[Activation]
  Act --> Next[Next layer]
```

## Key principles

1. **Capacity vs data** — Bigger nets need more data/regularization.
2. **Representations matter** — Hidden layers learn features automatically.
3. **Init and scale** — Poor initialization stalls training.

## Common applications

| Application | Description |
|-------------|-------------|
| Image models | CNNs / ViTs |
| Text models | Transformers |
| Tabular DL | MLPs when justified |

## Common mistakes

- Assuming deeper always means better
- Ignoring vanishing/exploding gradients historically solved by residuals/norms

## Further reading

- [Training loop & optimization](training-loop-and-optimization.md)
- [Transformers](../transformers/README.md)
