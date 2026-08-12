---
title: "3. Dimensions and Models"
description: "Embedding dimensions, Matryoshka truncation, model families, and how to choose an encoder for your corpus."
domain: embeddings-vector-databases
tags: [embeddings-vector-databases, models, dimensions]
status: published
created: 2026-08-12
updated: 2026-08-12
version: "1.0"
related:
  - 01-embeddings-explained.md
  - 02-similarity-and-metrics.md
  - ../operations/01-choosing-embedding-and-vdb.md
keywords: [dimensions, MTEB, BGE, OpenAI embeddings, Matryoshka]
author: hp
---

# 3. Dimensions and Models

> Dimension count, model family, and license shape cost, latency, and recall. Pick the encoder like a product dependency — versioned, evaluated, and replaceable.

## Table of Contents

- [Definition](#definition)
- [What Dimension Means](#what-dimension-means)
- [Matryoshka and Truncation](#matryoshka-and-truncation)
- [Model Families](#model-families)
- [Specialization Axes](#specialization-axes)
- [Cost and Latency](#cost-and-latency)
- [Selection Checklist](#selection-checklist)
- [Python Examples](#python-examples)
- [Common Mistakes](#common-mistakes)
- [Interview Preparation](#interview-preparation)
- [Navigation](#navigation)

---

## Definition

**Dimensionality** is the length of each embedding vector. **Model choice** is which trained encoder produces those vectors. Together they determine storage, ANN speed, API spend, and retrieval quality on your domain.

---

## What Dimension Means

| Dims | Typical tradeoff |
|------|------------------|
| 256–384 | Fast, cheap, good for prototypes / constrained RAM |
| 768–1024 | Common open-model sweet spot |
| 1536–3072 | High-capacity API models; more storage/bandwidth |

Higher dimensions can encode more nuance but increase RAM, disk, and distance-compute cost. Gains diminish; **always measure recall@k on your golden set**.

```mermaid
flowchart TB
  Needs[Language / domain / latency / privacy] --> Pick[Candidate models]
  Pick --> Bench[Embed golden queries + corpus sample]
  Bench --> Metric[Recall@k / MRR / latency / $]
  Metric --> Decide[Lock model_id + dim + metric]
```

---

## Matryoshka and Truncation

Some models (e.g. OpenAI `text-embedding-3-*`, Matryoshka-trained open models) allow **shortening** vectors while preserving useful geometry.

Rules:

1. Truncate to the first `d` dimensions only if the model supports it.
2. **Re-normalize** after truncation for cosine search.
3. Store `embedding_dim` in metadata; indexes are dim-specific.
4. Re-evaluate — do not assume 50% dims ⇒ 50% quality loss.

---

## Model Families

| Family | Hosting | Notes |
|--------|---------|-------|
| OpenAI text-embedding-3 | API | Strong general quality; dims configurable |
| Cohere embed | API | Strong multilingual options |
| Voyage | API | Long-context / code variants |
| BGE / E5 / GTE | Self-host | Popular open retrieval models |
| Instructor / GTE-instruction | Self-host | Task instructions in text |
| CLIP / multimodal | Varies | Image–text joint space |

**Rule:** Same `model_id` (and instruction format) for ingest and query.

---

## Specialization Axes

- **Language** — multilingual vs English-only
- **Domain** — legal, medical, support macros (fine-tune or domain models)
- **Modality** — text-only vs multimodal
- **Code** — identifier-preserving code embedders for repo RAG
- **Context length** — long-passage models vs short chunk models

---

## Cost and Latency

Cost ≈ `(corpus_tokens × reindex_frequency + query_tokens × QPS × seconds)` × price.

Latency budget:

- Batch embed on ingest (100–500 inputs/call typical)
- Cache frequent query embeddings briefly
- Prefer local models when data residency or P99 embed latency is strict

---

## Selection Checklist

1. Language and domain coverage
2. Asymmetric retrieval support / instructions
3. Dim + metric + normalization story
4. License and data residency
5. Eval: recall@k on **your** queries
6. Ops: rate limits, GPUs, reindex time
7. Escape hatch: can you dual-run a challenger model?

---

## Python Examples

```python
# Dimension truncation + renormalize (Matryoshka-style)
import numpy as np


def truncate_normalize(vecs: np.ndarray, dim: int) -> np.ndarray:
    x = vecs[:, :dim].astype(np.float32)
    norms = np.linalg.norm(x, axis=1, keepdims=True) + 1e-12
    return x / norms


# Compare two models on a tiny golden set (sketch)
def recall_at_k(relevant: set[str], retrieved: list[str], k: int) -> float:
    hit = sum(1 for doc in retrieved[:k] if doc in relevant)
    return hit / max(len(relevant), 1)
```

```python
MODEL_REGISTRY = {
    "openai:text-embedding-3-small@1536": {
        "provider": "openai",
        "model": "text-embedding-3-small",
        "dimensions": 1536,
        "metric": "cosine",
        "normalize": True,
    },
    "local:bge-small-en-v1.5@384": {
        "provider": "sentence-transformers",
        "model": "BAAI/bge-small-en-v1.5",
        "dimensions": 384,
        "metric": "cosine",
        "normalize": True,
    },
}
```

---

## Common Mistakes

- Choosing by MTEB rank alone
- Mixing dims after a “quick” model swap
- Ignoring instruction prefixes required by E5/BGE variants
- No budget for periodic re-embed jobs
- Storing API vectors without recording model + dim in metadata

---

## Interview Preparation

**Q: Does higher dimension always improve retrieval?**

> No. Beyond a point, returns diminish and cost rises. Validate on domain eval sets; consider Matryoshka truncation.

**Q: What must you store with each vector?**

> Model id/version, dimension, metric/normalization assumptions, chunking policy version.

---

## Navigation

- **Prev:** [Similarity & Metrics](02-similarity-and-metrics.md)
- **Next section:** [ANN & Approximate Search](../indexing-and-search/01-ann-and-approximate-search.md)
- **Section hub:** [Embedding Foundations](README.md)
