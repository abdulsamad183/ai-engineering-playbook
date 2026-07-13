---
title: "Qdrant for RAG"
description: "Qdrant vector database — filtering, payloads, gRPC performance, deployment, Python client."
domain: rag
tags: [rag, qdrant, vector-database, phase-7]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - ../vector-databases.md
keywords: [Qdrant, payload filter, HNSW, Rust]
author: hp
---

# Qdrant for RAG

## Overview

**Qdrant** is a high-performance vector DB written in Rust with rich payload filtering — popular production choice.

| Aspect | Detail |
|--------|--------|
| **Architecture** | Collections, shards, replicas |
| **Strengths** | Fast filters, simple API, on-prem + cloud |
| **Weaknesses** | Smaller ecosystem than Pinecone for beginners |
| **Index** | HNSW |
| **Deployment** | Docker, K8s, Qdrant Cloud |
| **Pricing** | OSS + cloud tiers |
| **Best for** | Production self-host with strong metadata filters |

## Python Example

```python
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, Filter, FieldCondition, MatchValue

client = QdrantClient(url="http://localhost:6333")

client.upsert(
    collection_name="kb",
    points=[PointStruct(
        id="chunk-1",
        vector=embedding,
        payload={"tenant_id": "acme", "content": "Refund in 3 days.", "doc_id": "p-44"},
    )],
)

hits = client.search(
    collection_name="kb",
    query_vector=query_embedding,
    query_filter=Filter(must=[FieldCondition(key="tenant_id", match=MatchValue(value="acme"))]),
    limit=10,
)
```

## Production Notes

- Quantization for memory savings on large collections
- Snapshot API for backups
- gRPC client for lower latency

## Navigation

- [Vector Databases](../vector-databases.md) · [Production RAG](../production-rag.md)
