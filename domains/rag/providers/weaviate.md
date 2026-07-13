---
title: "Weaviate for RAG"
description: "Weaviate vector database — GraphQL API, hybrid search, modules, deployment."
domain: rag
tags: [rag, weaviate, vector-database, hybrid-search, phase-7]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - ../vector-databases.md
  - ../bm25.md
keywords: [Weaviate, hybrid search, GraphQL]
author: hp
---

# Weaviate for RAG

## Overview

**Weaviate** is an open-source vector database with built-in hybrid (BM25 + vector) search and modular embedders.

| Aspect | Detail |
|--------|--------|
| **Architecture** | Go core, REST/GraphQL |
| **Strengths** | Native hybrid, schema classes, modules |
| **Weaknesses** | Learning curve vs simple APIs |
| **Index** | HNSW |
| **Deployment** | Docker, K8s, Weaviate Cloud |
| **Pricing** | OSS + cloud |
| **Best for** | Hybrid search without glue code |

## Python Example

```python
import weaviate

client = weaviate.connect_to_local()
collection = client.collections.get("KbChunk")

collection.data.insert({
    "content": "Refund in 3 business days.",
    "tenant_id": "acme",
})

response = collection.query.hybrid(
    query="refund timeline",
    alpha=0.5,
    limit=5,
    filters=weaviate.classes.query.Filter.by_property("tenant_id").equal("acme"),
)
```

## Production Notes

- `alpha` tunes BM25 vs vector balance
- Multi-tenancy via separate collections or filters
- Backup before schema migrations

## Navigation

- [Vector Databases](../vector-databases.md) · [Hybrid Retrieval](../retrieval-strategies.md)
