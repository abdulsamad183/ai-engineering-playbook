---
title: "PostgreSQL Interviews for AI Engineers"
description: "PostgreSQL — MVCC, indexing, JSONB, full-text search, pooling, partitioning."
domain: interview-preparation
tags: [interview, postgresql, database]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - sql-interviews.md
  - ../databases/postgresql/README.md
keywords: [PostgreSQL interview, MVCC, JSONB, pgvector]
author: hp
---

# PostgreSQL Interviews for AI Engineers

## Overview

Section **5**. Postgres is the default **OLTP + metadata** store; often hosts **pgvector** for small/medium RAG.

## Core Concepts

| Topic | Interview angle |
|-------|-----------------|
| **MVCC** | Readers don't block writers; vacuum |
| **B-tree vs GIN** | Equality vs JSONB/full-text |
| **Query planner** | `EXPLAIN ANALYZE` |
| **Connection pooling** | PgBouncer — AI APIs open many conns |
| **JSONB** | Tool args, flexible metadata |
| **Full-text** | Hybrid with vector search |
| **Partitioning** | Large message tables by month |

## FAQ

**Q: Explain MVCC simply.**

> Each row has versions; transactions see a snapshot; old versions cleaned by autovacuum. Long transactions block vacuum → bloat.

**Q: When use JSONB vs normalized columns?**

> JSONB for evolving tool schemas, provider payloads; normalize fields you filter/join often.

**Q: pgvector vs dedicated vector DB?**

> pgvector: simpler ops, ACID with metadata, moderate scale. Pinecone/Qdrant: higher QPS, ANN at billion scale.

**Follow-up:** How index vectors?

> HNSW or IVFFlat — trade build time vs recall.

## Production Discussion

- Row-level security for multi-tenant chat
- Read replicas for analytics eval queries

## Further Reading

- [RAG pgvector](../rag/providers/pgvector.md)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Section 5 |
