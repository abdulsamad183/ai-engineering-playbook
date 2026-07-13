---
title: "Databases for AI Applications"
description: "Database selection, design, and operations for AI applications — SQL vs NoSQL, PostgreSQL, Redis, object storage, vector DB overview, transactions, indexing, migrations, and connection pooling."
domain: databases
tags: [database, sql, foundations, backend, production]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - postgresql/postgresql-for-ai.md
  - redis/redis-for-ai.md
  - ../rag/README.md
  - ../vector-databases/README.md
  - ../backend-engineering/backend-fundamentals-for-ai.md
  - ../foundations/software-engineering-for-ai.md
keywords: [postgresql, redis, sql, nosql, vector database, connection pooling, migrations, transactions, indexing]
author: hp
---

# Databases for AI Applications

> How to choose, design, and operate databases for production AI systems — from conversation history to embeddings metadata to rate-limit counters.

## Table of Contents

- [Why Databases Matter for AI](#why-databases-matter-for-ai)
- [AI Application Data Architecture](#ai-application-data-architecture)
- [SQL vs NoSQL](#sql-vs-nosql)
- [PostgreSQL](#postgresql)
- [Redis](#redis)
- [Object Storage](#object-storage)
- [Vector Databases (Overview)](#vector-databases-overview)
- [Database Design for AI Applications](#database-design-for-ai-applications)
- [Transactions](#transactions)
- [Indexing](#indexing)
- [Migrations](#migrations)
- [Connection Pooling](#connection-pooling)
- [Production Considerations](#production-considerations)
- [Common Mistakes](#common-mistakes)
- [Interview Preparation](#interview-preparation)
- [Navigation](#navigation)

---

## Why Databases Matter for AI

AI demos store state in memory. Production AI systems store state in databases — and the choice of store determines latency, cost, consistency, and how safely you can ship changes.

| AI Feature | Typical Data Store | Why |
|-----------|-------------------|-----|
| User accounts, billing | PostgreSQL | ACID, relational integrity |
| Conversation history | PostgreSQL / MongoDB | Structured messages, queryable history |
| Document metadata | PostgreSQL | Joins with users, projects, permissions |
| Raw documents (PDFs, images) | Object storage (S3) | Cheap, durable, large blobs |
| Embeddings / similarity search | Vector DB or pgvector | Optimized for ANN search — see [RAG phase](../rag/README.md) |
| LLM response cache | Redis | Sub-millisecond reads, TTL eviction |
| Rate limiting | Redis | Atomic counters, fast increments |
| Job queues | Redis / PostgreSQL | Async embedding, indexing pipelines |

> **Production Standard:** Treat the database layer as infrastructure your domain code talks to through repositories — never embed SQL or Redis commands in route handlers. See [Software Engineering for AI](../foundations/software-engineering-for-ai.md).

---

## AI Application Data Architecture

Most production AI applications use a **polyglot persistence** model: multiple specialized stores, each chosen for what it does best.

```mermaid
graph TB
  subgraph "Application Layer"
    API[FastAPI / API Gateway]
    SVC[RAG Service / Agent Orchestrator]
  end

  subgraph "Transactional Data"
    PG[(PostgreSQL)]
  end

  subgraph "Fast Ephemeral Data"
    RD[(Redis)]
  end

  subgraph "Blob Storage"
    S3[(Object Storage - S3/GCS)]
  end

  subgraph "Vector Search"
  VD[(Vector DB / pgvector)]
  end

  API --> SVC
  SVC --> PG
  SVC --> RD
  SVC --> S3
  SVC --> VD

  PG --- |"users, conversations, metadata"| PG
  RD --- |"cache, sessions, rate limits"| RD
  S3 --- |"PDFs, images, exports"| S3
  VD --- |"embeddings, chunks"| VD
```

### Data Flow: RAG Document Ingestion

```mermaid
sequenceDiagram
  participant U as User
  participant API as API
  participant S3 as Object Storage
  participant PG as PostgreSQL
  participant Q as Job Queue
  participant V as Vector Store

  U->>API: Upload document
  API->>S3: Store raw file
  API->>PG: Insert document metadata (status=pending)
  API->>Q: Enqueue embedding job
  Q->>S3: Fetch raw file
  Q->>V: Store chunks + embeddings
  Q->>PG: Update status=indexed
```

For deep coverage of retrieval pipelines and vector store selection, see the [RAG domain](../rag/README.md) and [Vector Databases domain](../vector-databases/README.md).

---

## SQL vs NoSQL

### When to Choose What

| Dimension | SQL (PostgreSQL) | NoSQL (Document / Key-Value) |
|-----------|-----------------|------------------------------|
| **Data shape** | Structured, relational, joins | Flexible schema, nested documents |
| **Consistency** | Strong ACID guarantees | Often eventual consistency |
| **Queries** | Complex joins, aggregations, analytics | Simple key lookups, limited ad-hoc queries |
| **Schema evolution** | Migrations (Alembic) | Schema-on-read, flexible fields |
| **AI fit** | Users, billing, conversation metadata, audit logs | Chat message blobs, flexible agent state |
| **Team familiarity** | High — default for most backends | Use when shape is genuinely unstructured |

### Decision Framework for AI Apps

```mermaid
flowchart TD
  A[What are you storing?] --> B{Relational integrity needed?}
  B -->|Yes - users, billing, permissions| C[PostgreSQL]
  B -->|No| D{Sub-millisecond reads?}
  D -->|Yes - cache, counters| E[Redis]
  D -->|No| F{Large binary files?}
  F -->|Yes| G[Object Storage]
  F -->|No| H{Vector similarity search?}
  H -->|Yes| I[Vector DB - see RAG phase]
  H -->|No| J{Flexible nested documents?}
  J -->|Yes| K[Document DB - MongoDB]
  J -->|No| C
```

### Default Recommendation

**Start with PostgreSQL** for all transactional data. Add Redis when you need caching or rate limiting. Add object storage when files exceed a few MB. Add a dedicated vector database (or pgvector) when you build RAG — covered in the [RAG phase](../rag/README.md).

PostgreSQL with JSONB columns often eliminates the need for a separate document database:

```sql
-- Store flexible agent state inside a relational model
CREATE TABLE agent_runs (
    id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id     UUID NOT NULL REFERENCES users(id),
    status      TEXT NOT NULL DEFAULT 'running',
    config      JSONB NOT NULL DEFAULT '{}',
    tool_calls  JSONB NOT NULL DEFAULT '[]',
    created_at  TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at  TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- Query nested JSON fields
SELECT id, config->>'model' AS model
FROM agent_runs
WHERE config->>'model' = 'gpt-4o'
  AND status = 'completed';
```

---

## PostgreSQL

PostgreSQL is the default transactional database for AI applications. It handles users, conversations, document metadata, billing, audit logs, and — with the pgvector extension — can serve as a vector store for smaller RAG workloads.

### Core AI Use Cases

| Use Case | Pattern |
|----------|---------|
| Conversation history | `conversations` + `messages` tables with foreign keys |
| Document catalog | Metadata in PG, blobs in S3, linked by `storage_key` |
| User preferences | JSONB column for model/temperature overrides |
| Token usage tracking | Append-only `usage_events` table for billing |
| Feature flags | `features` table or JSONB on `users` |
| Small-scale RAG | pgvector extension for embedding storage |

### Example Schema

```sql
CREATE TABLE users (
    id         UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email      TEXT UNIQUE NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE conversations (
    id         UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id    UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    title      TEXT,
    model      TEXT NOT NULL DEFAULT 'gpt-4o-mini',
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE messages (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    conversation_id UUID NOT NULL REFERENCES conversations(id) ON DELETE CASCADE,
    role            TEXT NOT NULL CHECK (role IN ('user', 'assistant', 'system', 'tool')),
    content         TEXT NOT NULL,
    token_count     INT,
    metadata        JSONB NOT NULL DEFAULT '{}',
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX idx_messages_conversation_created
    ON messages (conversation_id, created_at);
```

### Python Access Pattern

```python
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import select, ForeignKey, Text
from uuid import UUID, uuid4
from datetime import datetime


class Base(DeclarativeBase):
    pass


class Message(Base):
    __tablename__ = "messages"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    conversation_id: Mapped[UUID] = mapped_column(ForeignKey("conversations.id"))
    role: Mapped[str] = mapped_column(Text)
    content: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)


async def get_conversation_history(
    session: AsyncSession, conversation_id: UUID, limit: int = 50
) -> list[Message]:
    result = await session.execute(
        select(Message)
        .where(Message.conversation_id == conversation_id)
        .order_by(Message.created_at.desc())
        .limit(limit)
    )
    return list(reversed(result.scalars().all()))
```

> **Deep dive:** [PostgreSQL for AI](postgresql/postgresql-for-ai.md) — pgvector, JSONB patterns, full-text search, async SQLAlchemy, and production tuning.

---

## Redis

Redis is an in-memory data store used for caching, session management, rate limiting, pub/sub streaming, and short-lived agent state. It is not a replacement for PostgreSQL.

### Core AI Use Cases

| Use Case | Redis Data Structure | TTL |
|----------|---------------------|-----|
| LLM response cache | String (JSON) | 1h–24h |
| Semantic cache key | String (hash of query) | Configurable |
| Rate limiting | String (INCR + EXPIRE) | Per window |
| User sessions | Hash | Session lifetime |
| Streaming pub/sub | Pub/Sub channels | N/A |
| Agent tool results | Hash / String | Minutes |
| Distributed locks | String (SET NX EX) | Seconds |

### Rate Limiting Example

```python
import redis.asyncio as redis

RATE_LIMIT = 60  # requests per minute


async def check_rate_limit(r: redis.Redis, user_id: str) -> bool:
    key = f"rate:{user_id}"
    pipe = r.pipeline()
    pipe.incr(key)
    pipe.expire(key, 60)
    count, _ = await pipe.execute()
    return int(count) <= RATE_LIMIT
```

### LLM Response Cache

```python
import hashlib
import json


def cache_key(model: str, prompt: str, system: str = "") -> str:
    payload = json.dumps({"model": model, "prompt": prompt, "system": system}, sort_keys=True)
    return f"llm_cache:{hashlib.sha256(payload.encode()).hexdigest()}"


async def get_cached_response(r: redis.Redis, key: str) -> str | None:
    return await r.get(key)


async def set_cached_response(r: redis.Redis, key: str, response: str, ttl: int = 3600) -> None:
    await r.set(key, response, ex=ttl)
```

> **Deep dive:** [Redis for AI](redis/redis-for-ai.md) — semantic caching, session patterns, pub/sub streaming, and production configuration.

---

## Object Storage

Object storage (AWS S3, Google Cloud Storage, MinIO) stores raw documents, generated exports, model artifacts, and user uploads. It is optimized for large, immutable blobs — not for querying or transactional updates.

### AI Application Patterns

| Content | Storage Pattern | Metadata Location |
|---------|----------------|-------------------|
| Uploaded PDFs | `s3://bucket/users/{user_id}/docs/{doc_id}.pdf` | PostgreSQL `documents` table |
| Generated reports | `s3://bucket/exports/{job_id}.pdf` | PostgreSQL `export_jobs` table |
| Fine-tuning datasets | `s3://bucket/datasets/{version}/` | Version tag in PG |
| Conversation exports | `s3://bucket/exports/{user_id}/{timestamp}.json` | Optional PG reference |

```mermaid
graph LR
  PG[(PostgreSQL)] -->|"storage_key, mime_type, size"| META[Document Metadata]
  S3[(S3)] -->|"raw bytes"| BLOB[PDF / Image / Audio]
  META -.->|"references"| BLOB
```

### Python Upload Pattern

```python
import boto3
from uuid import uuid4


def upload_document(
    bucket: str,
    user_id: str,
    file_bytes: bytes,
    content_type: str,
) -> str:
    key = f"users/{user_id}/docs/{uuid4()}"
    s3 = boto3.client("s3")
    s3.put_object(
        Bucket=bucket,
        Key=key,
        Body=file_bytes,
        ContentType=content_type,
    )
    return key
```

### Production Considerations

- **Never store blobs in PostgreSQL** for files over ~1 MB — use object storage and store the key.
- **Use pre-signed URLs** for direct client uploads/downloads; the API never proxies large files.
- **Enable versioning** on critical buckets for accidental-delete recovery.
- **Lifecycle policies** move old exports to cheaper storage tiers after 30–90 days.
- **Server-side encryption** (SSE-S3 or SSE-KMS) is non-negotiable for user data.

---

## Vector Databases (Overview)

Vector databases store embedding vectors and perform approximate nearest neighbor (ANN) search — the retrieval step in RAG pipelines. This section is intentionally brief; deep coverage lives in the RAG and vector database domains.

### What They Do

1. Accept embedding vectors (e.g., 1536-dim floats from `text-embedding-3-small`).
2. Index them for fast similarity search (HNSW, IVF, etc.).
3. Return the top-k most similar vectors given a query embedding.

### Options at a Glance

| Option | Best For | Trade-off |
|--------|----------|-----------|
| **pgvector** (PostgreSQL extension) | Small-to-medium datasets (<1M vectors), already using PG | Simpler ops, slower at scale |
| **Pinecone** | Managed, fast time-to-production | Vendor lock-in, cost at scale |
| **Weaviate** | Hybrid search (vector + keyword) | Self-host or managed |
| **Qdrant** | Self-hosted, Rust performance | Ops overhead |
| **Chroma** | Prototyping, local dev | Not production-hardened alone |

### Where Vector DBs Fit

```mermaid
graph LR
  DOC[Documents] --> CHUNK[Chunking]
  CHUNK --> EMB[Embedding Model]
  EMB --> VDB[(Vector Database)]
  QUERY[User Query] --> EMB2[Embedding Model]
  EMB2 --> VDB
  VDB --> CTX[Retrieved Context]
  CTX --> LLM[LLM Generation]
```

### Minimal pgvector Example (Development)

```sql
CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE document_chunks (
    id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    document_id UUID NOT NULL REFERENCES documents(id),
    content     TEXT NOT NULL,
    embedding   vector(1536),
    metadata    JSONB NOT NULL DEFAULT '{}'
);

CREATE INDEX idx_chunks_embedding ON document_chunks
    USING hnsw (embedding vector_cosine_ops);
```

```python
# Insert and search — production patterns covered in RAG phase
query = "SELECT id, content, embedding <=> :query_vec AS distance FROM document_chunks ORDER BY distance LIMIT 5"
```

> **Go deeper:**
> - [RAG Domain](../rag/README.md) — chunking, retrieval strategies, evaluation, production RAG architecture
> - [Vector Databases Domain](../vector-databases/README.md) — indexing algorithms, store comparison, scaling
> - [PostgreSQL for AI](postgresql/postgresql-for-ai.md) — pgvector setup and hybrid search

---

## Database Design for AI Applications

### Design Principles

1. **Separate metadata from blobs** — PostgreSQL holds queryable metadata; S3 holds raw files.
2. **Separate metadata from vectors** — PostgreSQL holds document catalog; vector store holds embeddings.
3. **Design for conversation threading** — `conversations` → `messages` with ordered `created_at`.
4. **Track provenance** — every AI-generated output links back to model, prompt version, and retrieved chunks.
5. **Plan for deletion** — GDPR and data retention require cascade deletes and vector store cleanup.

### Entity Relationship: Typical AI App

```mermaid
erDiagram
  USERS ||--o{ CONVERSATIONS : has
  CONVERSATIONS ||--o{ MESSAGES : contains
  USERS ||--o{ DOCUMENTS : uploads
  DOCUMENTS ||--o{ DOCUMENT_CHUNKS : "split into"
  DOCUMENT_CHUNKS }o--|| VECTOR_INDEX : "embedded in"
  USERS ||--o{ USAGE_EVENTS : generates

  USERS {
    uuid id PK
    text email
    timestamptz created_at
  }
  CONVERSATIONS {
    uuid id PK
    uuid user_id FK
    text model
    timestamptz created_at
  }
  MESSAGES {
    uuid id PK
    uuid conversation_id FK
    text role
    text content
    jsonb metadata
  }
  DOCUMENTS {
    uuid id PK
    uuid user_id FK
    text storage_key
    text status
    jsonb metadata
  }
```

### Provenance Tracking

```sql
CREATE TABLE generation_events (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    message_id      UUID NOT NULL REFERENCES messages(id),
    model           TEXT NOT NULL,
    prompt_version  TEXT NOT NULL,
    retrieved_chunks JSONB NOT NULL DEFAULT '[]',
    input_tokens    INT,
    output_tokens   INT,
    latency_ms      INT,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);
```

This table answers: "Which chunks influenced this answer?" — critical for debugging RAG quality and compliance audits.

### Multi-Tenancy

| Strategy | Isolation | Complexity |
|----------|-----------|------------|
| Row-level (`tenant_id` column) | Logical | Low — default choice |
| Schema-per-tenant | Moderate | Medium |
| Database-per-tenant | Strong | High — enterprise only |

```sql
-- Row-level tenancy: every query must filter by tenant_id
CREATE TABLE documents (
    id         UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id  UUID NOT NULL,
    user_id    UUID NOT NULL,
  -- ...
);

CREATE INDEX idx_documents_tenant ON documents (tenant_id, user_id);
```

> Always enforce tenant isolation in the repository layer, not just in application code. Use PostgreSQL row-level security (RLS) for defense in depth.

---

## Transactions

Transactions group multiple database operations into an atomic unit — all succeed or all roll back. AI applications need transactions wherever partial writes would leave data inconsistent.

### When AI Apps Need Transactions

| Operation | Why Atomic |
|-----------|-----------|
| Create conversation + first message | Orphan conversation without message |
| Deduct credits + log usage | Billing mismatch |
| Update document status + insert chunks | Indexed doc with wrong status |
| Transfer ownership + update permissions | Security gap |

### ACID in Practice

```python
from sqlalchemy.ext.asyncio import AsyncSession


async def create_conversation_with_message(
    session: AsyncSession,
    user_id: UUID,
    content: str,
    model: str,
) -> UUID:
    async with session.begin():
        conversation = Conversation(user_id=user_id, model=model)
        session.add(conversation)
        await session.flush()

        message = Message(
            conversation_id=conversation.id,
            role="user",
            content=content,
        )
        session.add(message)

    return conversation.id
```

### Isolation Levels

| Level | Behavior | AI App Use |
|-------|----------|------------|
| READ COMMITTED | Default in PostgreSQL; sees committed rows | Most operations |
| REPEATABLE READ | Consistent snapshot for transaction duration | Analytics queries |
| SERIALIZABLE | Full isolation, may retry | Financial operations |

### Cross-Store Consistency

Transactions do not span PostgreSQL and Redis or vector stores. Use these patterns:

```mermaid
flowchart LR
  A[Write to PostgreSQL] --> B{Success?}
  B -->|Yes| C[Write to Vector Store]
  B -->|No| D[Rollback - done]
  C --> E{Success?}
  E -->|Yes| F[Done]
  E -->|No| G[Compensating action / retry queue]
```

1. **Write metadata first** (PostgreSQL), then vectors (eventual consistency).
2. **Use outbox pattern** — write a job row in the same transaction, async worker processes it.
3. **Idempotent workers** — safe to retry embedding jobs without duplicates.

---

## Indexing

Indexes speed up reads at the cost of slower writes and more storage. AI applications generate high read volume on conversation history and document lookups.

### Index Types

| Type | Use Case | Example |
|------|----------|---------|
| B-tree (default) | Equality and range queries | `created_at`, `user_id` |
| GIN | JSONB containment, full-text search | `metadata @> '{"source": "upload"}'` |
| HNSW / IVFFlat | Vector similarity (pgvector) | `embedding <=> query` |
| Partial | Filtered subsets | `WHERE status = 'active'` |
| Composite | Multi-column queries | `(conversation_id, created_at)` |

### High-Value Indexes for AI Apps

```sql
-- Conversation history: most common query pattern
CREATE INDEX idx_messages_conv_time
    ON messages (conversation_id, created_at DESC);

-- Document lookup by user
CREATE INDEX idx_documents_user_status
    ON documents (user_id, status);

-- JSONB metadata search
CREATE INDEX idx_messages_metadata
    ON messages USING GIN (metadata);

-- Partial index: only index active documents
CREATE INDEX idx_documents_active
    ON documents (user_id, created_at)
    WHERE status = 'indexed';

-- Full-text search on document content (when not using vector search)
CREATE INDEX idx_chunks_content_fts
    ON document_chunks USING GIN (to_tsvector('english', content));
```

### Index Anti-Patterns

- Indexing every column "just in case" — slows writes, wastes disk.
- Missing indexes on foreign keys — every join becomes a sequential scan.
- Indexing `TEXT` columns used only with `LIKE '%term%'` — use full-text search or trigram indexes instead.

### Monitoring

```sql
-- Find unused indexes
SELECT schemaname, relname, indexrelname, idx_scan
FROM pg_stat_user_indexes
WHERE idx_scan = 0
  AND indexrelname NOT LIKE 'pg_toast%'
ORDER BY pg_relation_size(indexrelid) DESC;
```

---

## Migrations

Schema migrations version-control your database structure. AI applications evolve rapidly — new metadata fields, provenance columns, vector dimensions — and migrations keep environments in sync.

### Tooling

| Tool | Ecosystem | Notes |
|------|-----------|-------|
| **Alembic** | SQLAlchemy | Default for Python/FastAPI projects |
| **Flyway** | JVM / polyglot | SQL-based migration files |
| **Django migrations** | Django | Built-in, auto-generated |
| **Atlas** | Multi-language | Declarative schema management |

### Alembic Workflow

```bash
# Generate migration from model changes
alembic revision --autogenerate -m "add generation_events table"

# Apply migrations
alembic upgrade head

# Rollback one step
alembic downgrade -1
```

### Example Migration

```python
"""add generation_events table

Revision ID: 0003
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB, UUID


def upgrade() -> None:
    op.create_table(
        "generation_events",
        sa.Column("id", UUID, primary_key=True),
        sa.Column("message_id", UUID, sa.ForeignKey("messages.id"), nullable=False),
        sa.Column("model", sa.Text, nullable=False),
        sa.Column("prompt_version", sa.Text, nullable=False),
        sa.Column("retrieved_chunks", JSONB, nullable=False, server_default="[]"),
        sa.Column("input_tokens", sa.Integer),
        sa.Column("output_tokens", sa.Integer),
        sa.Column("latency_ms", sa.Integer),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
    )
    op.create_index("idx_gen_events_message", "generation_events", ["message_id"])


def downgrade() -> None:
    op.drop_table("generation_events")
```

### Migration Best Practices for AI Apps

1. **Never edit applied migrations** — create a new one to fix mistakes.
2. **Make migrations backward-compatible** — add columns as nullable first, backfill, then add constraints.
3. **Test migrations on a copy of production data** before deploying.
4. **Separate DDL from data migrations** — schema changes in Alembic; bulk data transforms in scripts.
5. **Version your prompts separately** — prompt changes are not database migrations.

### Zero-Downtime Patterns

```sql
-- Step 1: Add nullable column
ALTER TABLE messages ADD COLUMN token_count INT;

-- Step 2: Backfill (in application or batch script)
UPDATE messages SET token_count = 0 WHERE token_count IS NULL;

-- Step 3: Add constraint (in next migration)
ALTER TABLE messages ALTER COLUMN token_count SET NOT NULL;
```

---

## Connection Pooling

Database connections are expensive to create (TCP handshake, authentication, memory allocation). Connection pooling reuses connections across requests — essential for AI APIs with high concurrency.

### Why It Matters for AI Apps

AI API endpoints often hold connections during LLM calls (5–30 seconds). Without pooling, each concurrent request opens a new connection, exhausting PostgreSQL's `max_connections` (default: 100).

```mermaid
graph TB
  subgraph "Without Pooling"
    R1[Request 1] --> C1[Connection 1]
    R2[Request 2] --> C2[Connection 2]
    R3[Request N] --> CN[Connection N - exhausted]
  end

  subgraph "With Pooling"
    PR1[Request 1] --> POOL[Connection Pool]
    PR2[Request 2] --> POOL
    PR3[Request N] --> POOL
    POOL --> PC1[Conn 1]
    POOL --> PC2[Conn 2]
    POOL --> PC3[Conn 3-20]
  end
```

### Pool Configuration

```python
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

engine = create_async_engine(
    "postgresql+asyncpg://user:pass@localhost/aiapp",
    pool_size=20,          # persistent connections
    max_overflow=10,       # extra connections under load
    pool_timeout=30,         # seconds to wait for a connection
    pool_recycle=1800,       # recycle connections every 30 min
    pool_pre_ping=True,      # verify connection health before use
)

SessionLocal = async_sessionmaker(engine, expire_on_commit=False)
```

### External Poolers

| Tool | Use Case |
|------|----------|
| **PgBouncer** | Production PostgreSQL — transaction or session pooling |
| **RDS Proxy** | AWS-managed connection pooling for RDS/Aurora |
| **Pgpool-II** | Load balancing + pooling |

### Rules of Thumb

| Setting | Development | Production |
|---------|-------------|------------|
| `pool_size` | 5 | 20–50 (depends on workers) |
| `max_overflow` | 5 | 10–20 |
| `pool_recycle` | 3600 | 1800 |
| PgBouncer pool mode | N/A | `transaction` for most apps |

> **Critical:** Release database connections before making LLM API calls. Hold the connection only for the DB operation, not for the entire request lifecycle.

```python
async def answer_query(session_factory, query: str) -> str:
    # 1. DB work — short-lived connection
    async with session_factory() as session:
        history = await get_conversation_history(session, conversation_id)

    # 2. LLM call — no DB connection held
    response = await llm_client.complete(prompt=build_prompt(history, query))

    # 3. DB work — save response
    async with session_factory() as session:
        await save_message(session, conversation_id, "assistant", response.content)

    return response.content
```

---

## Production Considerations

### Checklist

| Area | Requirement |
|------|-------------|
| **Backups** | Automated daily PG backups, point-in-time recovery enabled |
| **Monitoring** | Query latency, connection count, cache hit ratio, replication lag |
| **Secrets** | Database URLs from environment variables, never in code |
| **Read replicas** | Route analytics and heavy reads to replicas |
| **Connection limits** | PgBouncer in front of PostgreSQL; size pools per worker count |
| **Data retention** | Automated purge of old conversations per policy |
| **Encryption** | TLS in transit, encryption at rest on all stores |
| **Access control** | Least-privilege DB users; app user cannot DROP TABLE |

### Monitoring Queries

```sql
-- Active connections
SELECT count(*) FROM pg_stat_activity WHERE state = 'active';

-- Slow queries (requires pg_stat_statements)
SELECT query, mean_exec_time, calls
FROM pg_stat_statements
ORDER BY mean_exec_time DESC
LIMIT 10;

-- Table sizes
SELECT relname, pg_size_pretty(pg_total_relation_size(relid))
FROM pg_stat_user_tables
ORDER BY pg_total_relation_size(relid) DESC;
```

### Health Check Endpoint

```python
from fastapi import APIRouter

router = APIRouter()


@router.get("/health/db")
async def db_health(session: AsyncSession = Depends(get_session)):
    result = await session.execute(text("SELECT 1"))
    return {"status": "ok", "db": result.scalar() == 1}
```

See [Backend Fundamentals for AI](../backend-engineering/backend-fundamentals-for-ai.md) for API health check patterns and deployment integration.

---

## Common Mistakes

| Mistake | Impact | Fix |
|---------|--------|-----|
| Storing embeddings only in PostgreSQL without pgvector | Full table scans on similarity search | Use pgvector index or dedicated vector DB |
| Storing large files in PostgreSQL | Bloated DB, slow backups, high cost | Object storage + metadata in PG |
| No connection pooling | `max_connections` exhaustion under load | SQLAlchemy pool + PgBouncer |
| Holding DB connections during LLM calls | Connection starvation | Release connection before external API calls |
| No migrations — manual schema changes | Environment drift, deploy failures | Alembic with CI migration checks |
| Using Redis as primary data store | Data loss on restart/eviction | Redis for ephemeral data only; PG for durable state |
| Missing indexes on foreign keys | Slow joins on conversation history | Index all FK columns used in queries |
| No provenance tracking | Cannot debug bad RAG answers | `generation_events` table with retrieved chunks |
| Caching without TTL | Stale responses served indefinitely | Always set TTL; version cache keys with prompt version |
| Single database for everything | Wrong tool for the job | Polyglot persistence — right store per data type |

---

## Interview Preparation

### Frequently Asked Questions

**Q1: How would you design the database layer for a RAG application?**

> **Strong answer:** PostgreSQL for users, document metadata, and conversation history. Object storage (S3) for raw documents. Vector database (or pgvector for smaller scale) for embeddings and similarity search. Redis for caching frequent queries and rate limiting. Metadata and vectors linked by document ID. Async workers handle ingestion: upload → S3 → chunk → embed → vector store → update PG status. Cross-reference the [RAG domain](../rag/README.md) for retrieval pipeline details.

**Q2: SQL vs NoSQL — how do you decide for an AI application?**

> **Strong answer:** Default to PostgreSQL for anything needing relational integrity, joins, or ACID transactions (users, billing, conversations). Use Redis for ephemeral, fast data (cache, rate limits). Use object storage for blobs. Use a vector database for embedding search. Consider a document database only when data is genuinely unstructured and you do not need joins — but PostgreSQL JSONB often suffices. The decision is about access patterns, not hype.

**Q3: How do you handle database connections in a high-concurrency AI API?**

> **Strong answer:** Connection pooling via SQLAlchemy (pool_size, max_overflow, pool_pre_ping). PgBouncer in production for transaction-level pooling. Critical rule: release connections before LLM API calls that take seconds. Size pools based on worker count, not request count. Monitor active connections and set alerts near `max_connections`.

**Q4: How do you keep PostgreSQL and a vector store in sync?**

> **Strong answer:** Write metadata to PostgreSQL first in a transaction, then enqueue an async job (outbox pattern) to embed and index in the vector store. Workers are idempotent. On delete, remove from both stores — PG in a transaction, vector store via compensating job. Accept eventual consistency for the vector index; PG is the source of truth for document existence.

**Q5: What indexes would you create for a chat application?**

> **Strong answer:** Composite index on `(conversation_id, created_at)` for message history retrieval. Index on `user_id` for conversation listing. GIN index on JSONB `metadata` if querying nested fields. Partial indexes for filtered queries (e.g., active documents only). Monitor with `pg_stat_user_indexes` to drop unused indexes.

### Real-World Scenario

**Scenario:** Your AI chat application works in development but PostgreSQL hits `max_connections` errors at 50 concurrent users. LLM responses take 10–15 seconds.

> **Discussion points:**
> 1. Diagnose: are connections held during LLM calls? (Likely yes.)
> 2. Fix: release DB connections before LLM calls; use connection pooling.
> 3. Add PgBouncer with transaction pooling mode.
> 4. Size `pool_size` = `(num_workers × expected_concurrent_db_ops)`.
> 5. Add monitoring on `pg_stat_activity` and alert at 80% of `max_connections`.

---

## Navigation

### Prerequisites

- [Software Engineering for AI](../foundations/software-engineering-for-ai.md) — repository pattern, layered architecture
- [AI Engineering Overview](../foundations/ai-engineering-overview.md)

### Related Topics

- [PostgreSQL for AI](postgresql/postgresql-for-ai.md) — pgvector, JSONB, async patterns
- [Redis for AI](redis/redis-for-ai.md) — caching, rate limiting, streaming
- [Backend Fundamentals for AI](../backend-engineering/backend-fundamentals-for-ai.md) — API design, health checks
- [RAG Domain](../rag/README.md) — retrieval pipelines, vector store deep dive
- [Vector Databases Domain](../vector-databases/README.md) — ANN algorithms, store comparison

### Next Topics

- [PostgreSQL for AI](postgresql/postgresql-for-ai.md)
- [Redis for AI](redis/redis-for-ai.md)
- [RAG Domain](../rag/README.md) — when you build retrieval

### Future Reading

- [Data Engineering Domain](../data-engineering/README.md)
- [Performance Optimization Domain](../performance-optimization/README.md)
- [Observability Domain](../observability/README.md)

---

## See Also

- [Databases Domain README](README.md)
- [SQL Subdomain](sql/README.md)
- [Master Index](../../meta/indexes/MASTER-INDEX.md)

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Initial version |
