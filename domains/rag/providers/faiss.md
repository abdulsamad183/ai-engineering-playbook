---
title: "FAISS for RAG"
description: "FAISS vector search — architecture, indexes, scaling, Python examples, production use cases."
domain: rag
tags: [rag, faiss, vector-database, self-hosted]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - ../vector-databases.md
  - ../embeddings-for-rag.md
keywords: [FAISS, IVF, HNSW, GPU, local vector search]
author: hp
---

# FAISS for RAG

> Facebook AI Similarity Search — high-performance local/GPU vector indexes for custom RAG stacks.

## Overview

**FAISS** is a library (not a server) for billion-scale similarity search. You manage persistence, metadata, and API layer.

| Aspect | Detail |
|--------|--------|
| **Architecture** | In-process index objects |
| **Strengths** | Speed, GPU, IVF+PQ at scale, free |
| **Weaknesses** | No built-in metadata server, ops burden |
| **Index types** | Flat, IVF, HNSW, PQ combinations |
| **Deployment** | Embed in worker; save index to disk |
| **Pricing** | OSS — infra only |
| **Best for** | Research, on-prem, custom high-throughput |

## Python Example

```python
import faiss
import numpy as np

dim = 1536
vectors = np.random.random((10000, dim)).astype("float32")
faiss.normalize_L2(vectors)

index = faiss.IndexHNSWFlat(dim, 32)
index.add(vectors)

q = np.random.random((1, dim)).astype("float32")
faiss.normalize_L2(q)
distances, indices = index.search(q, k=5)
```

## Production Notes

- Pair with PostgreSQL/SQLite for metadata by `faiss_id`
- Snapshot index files; rebuild jobs on embedding change
- GPU `StandardGpuResources` for large batch search

## Comparison

| vs Chroma | FAISS lower-level, more control |
| vs Pinecone | Self-managed, no SaaS ops |

## Navigation

- [Vector Databases](../vector-databases.md) · [Chroma](chroma.md)
