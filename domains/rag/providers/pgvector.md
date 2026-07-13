---
title: "PGVector for RAG"
description: "PostgreSQL pgvector — HNSW indexes, metadata joins, hybrid SQL+RAG, production deployment."
domain: rag
tags: [rag, pgvector, postgresql, vector-database, phase-7]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - ../vector-databases.md
  - ../../databases/databases-for-ai-applications.md
keywords: [pgvector, PostgreSQL, HNSW, SQL filters]
author: hp
---

# PGVector for RAG

## Overview

**pgvector** extends PostgreSQL with vector types and ANN indexes — ideal when you already run Postgres and want SQL + vectors unified.

| Aspect | Detail |
|--------|--------|
| **Architecture** | Vectors in PG tables + HNSW/IVFFlat |
| **Strengths** | ACID, joins, permissions, ops familiarity |
| **Weaknesses** | Scale limits vs dedicated vector DBs |
| **Index** | HNSW, IVFFlat |
| **Deployment** | RDS, Cloud SQL, self-hosted PG 15+ |
| **Pricing** | Postgres infra cost |
| **Best for** | Enterprise with existing PG, hybrid SQL+RAG |

## Python Example

```sql
CREATE EXTENSION vector;
CREATE TABLE chunks (
  id TEXT PRIMARY KEY,
  doc_id TEXT,
  tenant_id TEXT,
  content TEXT,
  embedding vector(1536)
);
CREATE INDEX ON chunks USING hnsw (embedding vector_cosine_ops);
```

```python
# SQLAlchemy + raw query
# SELECT id, content, 1 - (embedding <=> :query_vec) AS score
# FROM chunks WHERE tenant_id = :tenant ORDER BY embedding <=> :query_vec LIMIT 5
```

## Production Notes

- Combine BM25 (`tsvector`) + vector in same DB for hybrid
- Row-level security for multi-tenant
- `VACUUM` and index rebuild after bulk load

## Navigation

- [Vector Databases](../vector-databases.md) · [BM25](../bm25.md)
