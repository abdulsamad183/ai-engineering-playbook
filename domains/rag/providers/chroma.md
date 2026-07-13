---
title: "Chroma for RAG"
description: "Chroma vector database — architecture, deployment, Python API, production considerations."
domain: rag
tags: [rag, chroma, vector-database, phase-7]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - ../vector-databases.md
keywords: [Chroma, embedded vector DB, prototyping]
author: hp
---

# Chroma for RAG

## Overview

**Chroma** is an open-source embedding database with simple Python API — popular for prototypes and small production workloads.

| Aspect | Detail |
|--------|--------|
| **Architecture** | Client-server or embedded |
| **Strengths** | Easy API, fast dev, metadata filters |
| **Weaknesses** | Less proven at massive scale vs Milvus/Qdrant |
| **Index** | HNSW (via backend) |
| **Deployment** | Docker, embedded in app |
| **Pricing** | OSS + Chroma Cloud |
| **Best for** | MVPs, local dev, small-medium KB |

## Python Example

```python
import chromadb

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection("kb", metadata={"hnsw:space": "cosine"})

collection.add(
    ids=["chunk-1"],
    documents=["Refund policy: 3 business days."],
    metadatas=[{"tenant_id": "acme", "doc_type": "policy"}],
)

results = collection.query(
    query_texts=["how long for refund"],
    n_results=5,
    where={"tenant_id": "acme"},
)
```

## Production Notes

- Migrate to Qdrant/pgvector when QPS or corpus size grows
- Persist client path to durable volume
- Version collections on embedding model change

## Navigation

- [Vector Databases](../vector-databases.md) · [PGVector](pgvector.md)
