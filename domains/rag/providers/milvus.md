---
title: "Milvus for RAG"
description: "Milvus distributed vector database — architecture, scaling, deployment, Python SDK."
domain: rag
tags: [rag, milvus, vector-database, distributed, phase-7]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - ../vector-databases.md
keywords: [Milvus, Zilliz, distributed vectors]
author: hp
---

# Milvus for RAG

## Overview

**Milvus** is an open-source distributed vector database for billion-scale embeddings.

| Aspect | Detail |
|--------|--------|
| **Architecture** | Storage/compute separation, K8s native |
| **Strengths** | Scale, hybrid search, mature OSS |
| **Weaknesses** | Operational complexity |
| **Index** | HNSW, IVF, DiskANN |
| **Deployment** | Docker, K8s, Zilliz Cloud |
| **Pricing** | OSS + Zilliz Cloud SaaS |
| **Best for** | Large corpora, on-prem scale |

## Python Example

```python
from pymilvus import connections, Collection

connections.connect(uri="http://localhost:19530")
collection = Collection("kb_chunks")
collection.load()

results = collection.search(
    data=[query_embedding],
    anns_field="embedding",
    param={"metric_type": "COSINE", "params": {"ef": 64}},
    limit=10,
    expr='tenant_id == "acme"',
    output_fields=["content", "doc_id"],
)
```

## Production Notes

- Use partition by `tenant_id` for isolation
- Monitor segment flush and compaction
- Zilliz Cloud reduces ops burden

## Navigation

- [Vector Databases](../vector-databases.md) · [Weaviate](weaviate.md)
