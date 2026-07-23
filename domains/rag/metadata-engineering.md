---
title: "Metadata Engineering for RAG"
description: "RAG metadata — document IDs, source tracking, permissions, tags, chunk relationships, and filtering strategies."
domain: rag
tags: [rag, metadata, filtering, permissions]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - chunking.md
  - retrieval-strategies.md
  - production-rag.md
keywords: [metadata, ACL, filtering, document ID, lineage]
author: hp
---

# Metadata Engineering for RAG

> Metadata enables filtering, permissions, freshness, and debugging — not optional in production.

## Table of Contents

- [Overview](#overview)
- [Metadata Schema](#metadata-schema)
- [Core Fields](#core-fields)
- [Filtering Strategies](#filtering-strategies)
- [Relationships](#relationships)
- [Security and Permissions](#security-and-permissions)
- [Python Examples](#python-examples)
- [Interview Preparation](#interview-preparation)
- [Navigation](#navigation)

---

## Overview

Section **5**.

Every chunk should carry traceable metadata:

```json
{
  "chunk_id": "doc-12#3",
  "doc_id": "doc-12",
  "source_uri": "s3://kb/policy.pdf",
  "tenant_id": "acme",
  "acl": ["group:support", "user:123"],
  "created_at": "2026-06-01T00:00:00Z",
  "indexed_at": "2026-07-13T10:00:00Z",
  "doc_type": "policy",
  "language": "en",
  "parent_chunk_id": "doc-12#parent-1",
  "embedding_model": "text-embedding-3-large",
  "index_version": 7
}
```

---

## Metadata Schema

Design schema upfront — changing fields requires reindex or backfill.

| Category | Fields |
|----------|--------|
| Identity | `chunk_id`, `doc_id`, `source_uri` |
| Lineage | `parent_id`, `chunk_index`, `content_hash` |
| Temporal | `created_at`, `updated_at`, `indexed_at` |
| Access | `tenant_id`, `acl`, `classification` |
| Content | `title`, `author`, `tags`, `language` |
| Index | `embedding_model`, `index_version` |

---

## Core Fields

- **document IDs** — stable across reindexes
- **source tracking** — URI + version for refresh
- **timestamps** — freshness ranking
- **permissions** — filter before ANN search
- **chunk IDs** — citation targets

---

## Filtering Strategies

| Strategy | When |
|----------|------|
| Pre-filter (metadata) | Tenant, ACL, doc_type — **always** |
| Post-filter | Score threshold after retrieval |
| Hybrid | Pre-filter narrow + vector search |

Most vector DBs support metadata predicates — use them for security.

---

## Relationships

- Parent-child chunk links
- `see_also` doc graph (future GraphRAG)
- Version chains: `supersedes_doc_id`

---

## Security and Permissions

Fail closed: if ACL metadata missing, exclude chunk. Sync ACL from source system on schedule.

---

## Python Examples

```python
from dataclasses import dataclass, field


@dataclass
class ChunkMetadata:
    chunk_id: str
    doc_id: str
    tenant_id: str
    acl: list[str] = field(default_factory=list)
    tags: list[str] = field(default_factory=list)

    def filter_dict(self) -> dict:
        return {"tenant_id": self.tenant_id, "tags": self.tags}
```

---

## Interview Preparation

**Q: Why metadata matters more than embedding model choice?**

> Wrong tenant filter leaks data; missing tags prevent routing; stale `updated_at` serves old policy — embeddings cannot fix metadata errors.

---

## Navigation

### Next

- [Embeddings for RAG](embeddings-for-rag.md)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Initial publication |
