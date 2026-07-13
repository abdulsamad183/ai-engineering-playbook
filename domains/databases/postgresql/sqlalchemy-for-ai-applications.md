---
title: "SQLAlchemy for AI Applications"
description: "SQLAlchemy 2.0 patterns for AI applications — ORM, async sessions, models, relationships, queries, transactions, repository pattern, and PostgreSQL schema design for conversations and documents."
domain: databases
tags: [database, sql, postgresql, sqlalchemy, backend, production]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - postgresql-for-ai.md
  - alembic-migrations-for-ai.md
  - ../databases-for-ai-applications.md
  - ../redis/redis-for-ai.md
  - ../../backend-engineering/backend-fundamentals-for-ai.md
  - ../../foundations/software-engineering-for-ai.md
keywords: [sqlalchemy, asyncpg, orm, async session, repository pattern, postgresql schema, conversations, documents]
author: hp
---

# SQLAlchemy for AI Applications

> Production SQLAlchemy 2.0 patterns for AI backends — declarative models, async sessions, query patterns, transactions, and repository implementations for conversation and document storage.

## Table of Contents

- [Why SQLAlchemy for AI](#why-sqlalchemy-for-ai)
- [Project Setup](#project-setup)
- [PostgreSQL Schema Design for AI](#postgresql-schema-design-for-ai)
- [Declarative Models](#declarative-models)
- [Relationships](#relationships)
- [Session Management](#session-management)
- [Sync vs Async ORM](#sync-vs-async-orm)
- [Query Patterns](#query-patterns)
- [Transactions](#transactions)
- [Repository Pattern](#repository-pattern)
- [Testing with SQLAlchemy](#testing-with-sqlalchemy)
- [Common Mistakes](#common-mistakes)
- [Interview Preparation](#interview-preparation)
- [Navigation](#navigation)

---

## Why SQLAlchemy for AI

AI applications need durable, queryable state: users, conversations, messages, document metadata, usage events, and agent run logs. SQLAlchemy 2.0 is the standard Python ORM for PostgreSQL — it maps tables to typed Python objects, generates parameterized SQL, and integrates cleanly with FastAPI's async request lifecycle.

| Concern | Raw SQL | SQLAlchemy 2.0 |
|---------|---------|----------------|
| Type safety | Manual row mapping | `Mapped[T]` annotations |
| SQL injection | Risk if string-concatenated | Parameterized by default |
| Async FastAPI | Blocks event loop with sync drivers | `asyncpg` + `AsyncSession` |
| Schema evolution | Manual DDL scripts | Alembic autogenerate — see [Alembic guide](alembic-migrations-for-ai.md) |
| Testability | Hard to mock DB | Repository interfaces + in-memory fakes |

> **Production Standard:** Keep SQLAlchemy in the repository layer. Route handlers and services depend on repository interfaces, not on `session.execute()` directly. See [Software Engineering for AI](../../foundations/software-engineering-for-ai.md).

```mermaid
graph TB
  subgraph "Application Layer"
    API[FastAPI Routes]
    SVC[Chat / RAG Services]
  end

  subgraph "Data Access Layer"
    REPO[Repository Interfaces]
    IMPL[SQLAlchemy Repositories]
  end

  subgraph "SQLAlchemy Core"
    SESS[AsyncSession]
    ORM[Declarative Models]
  end

  subgraph "PostgreSQL"
    PG[(Tables)]
  end

  API --> SVC
  SVC --> REPO
  REPO --> IMPL
  IMPL --> SESS
  SESS --> ORM
  ORM --> PG
```

---

## Project Setup

### Dependencies

```bash
pip install "sqlalchemy[asyncio]>=2.0" asyncpg alembic
```

### Directory Layout

```
app/
├── db/
│   ├── engine.py          # create_async_engine, session factory
│   ├── base.py            # DeclarativeBase
│   ├── models/
│   │   ├── __init__.py    # export all models for Alembic
│   │   ├── user.py
│   │   ├── conversation.py
│   │   └── document.py
│   └── repositories/
│       ├── conversation.py
│       └── document.py
├── api/
│   └── deps.py            # get_session dependency
└── main.py
```

### Engine and Session Factory

```python
# app/db/engine.py
from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from app.db.base import Base


def create_engine(database_url: str):
    """database_url: postgresql+asyncpg://user:pass@host:5432/dbname"""
    return create_async_engine(
        database_url,
        pool_size=20,
        max_overflow=10,
        pool_timeout=30,
        pool_recycle=1800,
        pool_pre_ping=True,
        echo=False,
    )


def create_session_factory(engine) -> async_sessionmaker[AsyncSession]:
    return async_sessionmaker(
        engine,
        class_=AsyncSession,
        expire_on_commit=False,  # objects remain usable after commit
    )


async def get_session(
    session_factory: async_sessionmaker[AsyncSession],
) -> AsyncGenerator[AsyncSession, None]:
    async with session_factory() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
```

### FastAPI Dependency

```python
# app/api/deps.py
from fastapi import Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession


def get_session_factory(request: Request):
    return request.app.state.session_factory


async def get_db(
    session_factory=Depends(get_session_factory),
) -> AsyncGenerator[AsyncSession, None]:
    async for session in get_session(session_factory):
        yield session
```

---

## PostgreSQL Schema Design for AI

This section covers schema design from the SQLAlchemy perspective. For PostgreSQL-specific features (pgvector indexing, JSONB query patterns, full-text search, RLS, partitioning), see [PostgreSQL for AI](postgresql-for-ai.md).

### Design Principles

| Principle | AI Application Rationale |
|-----------|-------------------------|
| Normalize durable entities | Users, conversations, documents have clear lifecycles |
| Use JSONB for evolving metadata | Model params, tool calls, agent config change faster than DDL |
| UUID primary keys | Safe for distributed ID generation, no enumeration |
| `ON DELETE CASCADE` on child rows | Deleting a conversation removes messages atomically |
| Composite indexes match query patterns | `(conversation_id, created_at)` for message pagination |
| Status columns with CHECK constraints | Document ingestion pipeline: `pending → processing → indexed` |

### Core Schema (SQL Reference)

The SQLAlchemy models in later sections map to this schema:

```sql
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

CREATE TABLE users (
    id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email         TEXT UNIQUE NOT NULL,
    display_name  TEXT,
    preferences   JSONB NOT NULL DEFAULT '{}',
    created_at    TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at    TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE conversations (
    id         UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id    UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    title      TEXT,
    model      TEXT NOT NULL DEFAULT 'gpt-4o-mini',
    metadata   JSONB NOT NULL DEFAULT '{}',
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
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

CREATE TABLE documents (
    id           UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id      UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    filename     TEXT NOT NULL,
    storage_key  TEXT NOT NULL,
    mime_type    TEXT NOT NULL,
    size_bytes   BIGINT NOT NULL,
    status       TEXT NOT NULL DEFAULT 'pending'
                 CHECK (status IN ('pending', 'processing', 'indexed', 'failed')),
    chunk_count  INT DEFAULT 0,
    metadata     JSONB NOT NULL DEFAULT '{}',
    created_at   TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at   TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX idx_conversations_user ON conversations (user_id, created_at DESC);
CREATE INDEX idx_messages_conv_time ON messages (conversation_id, created_at);
CREATE INDEX idx_documents_user_status ON documents (user_id, status);
CREATE INDEX idx_messages_metadata ON messages USING GIN (metadata);
```

> **Cross-reference:** pgvector chunk tables, HNSW indexes, and hybrid search SQL are in [PostgreSQL for AI — pgvector](postgresql-for-ai.md#pgvector-for-embeddings). Object storage keys (`storage_key`) pair with S3 — see [Databases for AI Applications](../databases-for-ai-applications.md#object-storage).

---

## Declarative Models

SQLAlchemy 2.0 uses `DeclarativeBase` with `Mapped` type annotations.

```python
# app/db/base.py
from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import BigInteger, CheckConstraint, ForeignKey, Integer, Text, func
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class TimestampMixin:
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        onupdate=func.now(),
    )


class User(Base, TimestampMixin):
    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(PG_UUID(as_uuid=True), primary_key=True, default=uuid4)
    email: Mapped[str] = mapped_column(Text, unique=True)
    display_name: Mapped[str | None] = mapped_column(Text)
    preferences: Mapped[dict] = mapped_column(JSONB, default=dict)

    conversations: Mapped[list["Conversation"]] = relationship(back_populates="user")
    documents: Mapped[list["Document"]] = relationship(back_populates="user")


class Conversation(Base, TimestampMixin):
    __tablename__ = "conversations"

    id: Mapped[UUID] = mapped_column(PG_UUID(as_uuid=True), primary_key=True, default=uuid4)
    user_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE")
    )
    title: Mapped[str | None] = mapped_column(Text)
    model: Mapped[str] = mapped_column(Text, default="gpt-4o-mini")
    metadata_: Mapped[dict] = mapped_column("metadata", JSONB, default=dict)

    user: Mapped["User"] = relationship(back_populates="conversations")
    messages: Mapped[list["Message"]] = relationship(
        back_populates="conversation",
        order_by="Message.created_at",
        cascade="all, delete-orphan",
    )


class Message(Base):
    __tablename__ = "messages"
    __table_args__ = (
        CheckConstraint(
            "role IN ('user', 'assistant', 'system', 'tool')",
            name="ck_messages_role",
        ),
    )

    id: Mapped[UUID] = mapped_column(PG_UUID(as_uuid=True), primary_key=True, default=uuid4)
    conversation_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True), ForeignKey("conversations.id", ondelete="CASCADE")
    )
    role: Mapped[str] = mapped_column(Text)
    content: Mapped[str] = mapped_column(Text)
    token_count: Mapped[int | None] = mapped_column(Integer)
    metadata_: Mapped[dict] = mapped_column("metadata", JSONB, default=dict)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    conversation: Mapped["Conversation"] = relationship(back_populates="messages")


class Document(Base, TimestampMixin):
    __tablename__ = "documents"
    __table_args__ = (
        CheckConstraint(
            "status IN ('pending', 'processing', 'indexed', 'failed')",
            name="ck_documents_status",
        ),
    )

    id: Mapped[UUID] = mapped_column(PG_UUID(as_uuid=True), primary_key=True, default=uuid4)
    user_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE")
    )
    filename: Mapped[str] = mapped_column(Text)
    storage_key: Mapped[str] = mapped_column(Text)
    mime_type: Mapped[str] = mapped_column(Text)
    size_bytes: Mapped[int] = mapped_column(BigInteger)
    status: Mapped[str] = mapped_column(Text, default="pending")
    chunk_count: Mapped[int | None] = mapped_column(Integer, default=0)
    metadata_: Mapped[dict] = mapped_column("metadata", JSONB, default=dict)

    user: Mapped["User"] = relationship(back_populates="documents")
```

### Naming Conventions

- Use `metadata_` as the Python attribute when the column is named `metadata` (reserved in SQLAlchemy).
- Export all models from `app/db/models/__init__.py` so Alembic's `target_metadata` discovers every table.
- Prefer `server_default` for timestamps — let PostgreSQL set `now()`, not Python `datetime.utcnow()`.

---

## Relationships

### Relationship Types in AI Schemas

| Relationship | Example | Loading Strategy |
|-------------|---------|------------------|
| One-to-many | User → Conversations | `selectinload` for list endpoints |
| One-to-many | Conversation → Messages | `selectinload` or explicit query |
| Many-to-one | Message → Conversation | Lazy load OK in single-object fetches |

### Cascade Rules

```python
messages: Mapped[list["Message"]] = relationship(
    back_populates="conversation",
    cascade="all, delete-orphan",  # deleting conversation deletes messages
)
```

`delete-orphan` ensures orphaned messages are removed when detached from a conversation. Match this with `ON DELETE CASCADE` at the database level for consistency.

### Eager Loading (N+1 Prevention)

```python
from sqlalchemy.orm import selectinload

stmt = (
    select(Conversation)
    .where(Conversation.user_id == user_id)
    .options(selectinload(Conversation.messages))
    .order_by(Conversation.created_at.desc())
    .limit(20)
)
result = await session.execute(stmt)
conversations = result.scalars().all()
```

`selectinload` issues one additional query per relationship — efficient for collections. Use `joinedload` when you always need the parent and a single child row in one JOIN.

---

## Session Management

### Session Lifecycle

```mermaid
sequenceDiagram
  participant API as FastAPI
  participant Dep as get_db
  participant Sess as AsyncSession
  participant PG as PostgreSQL

  API->>Dep: Request starts
  Dep->>Sess: Open session
  API->>Sess: Repository queries / adds
  Dep->>Sess: commit() on success
  Dep->>Sess: rollback() on exception
  Dep->>Sess: Close session
```

### Unit of Work per Request

One `AsyncSession` per HTTP request is the standard FastAPI pattern. The dependency commits on success and rolls back on any exception.

```python
async def create_conversation(
    user_id: UUID,
    model: str,
    session: AsyncSession,
) -> Conversation:
    conversation = Conversation(user_id=user_id, model=model)
    session.add(conversation)
    await session.flush()  # get ID without committing
    return conversation
```

Use `flush()` when you need the generated ID within the same transaction before commit.

### `expire_on_commit=False`

Set `expire_on_commit=False` on the session factory. Without it, committed objects are expired and the next attribute access triggers a lazy reload — problematic in async code after the session closes.

---

## Sync vs Async ORM

| Aspect | Sync (`psycopg2`) | Async (`asyncpg`) |
|--------|-------------------|-------------------|
| FastAPI compatibility | Blocks event loop | Non-blocking |
| Session class | `Session` | `AsyncSession` |
| Execute | `session.execute(stmt)` | `await session.execute(stmt)` |
| URL scheme | `postgresql+psycopg2://` | `postgresql+asyncpg://` |

**Always use async** in FastAPI AI applications. Sync SQLAlchemy is acceptable for CLI scripts, Celery workers (if not using async workers), and one-off data migrations.

```python
# Async query — the production default
result = await session.execute(
    select(Message)
    .where(Message.conversation_id == conversation_id)
    .order_by(Message.created_at)
    .limit(50)
)
messages = result.scalars().all()

# Core-style execution for raw SQL (pgvector queries)
from sqlalchemy import text

result = await session.execute(
    text("SELECT id, content FROM document_chunks WHERE document_id = :doc_id LIMIT :n"),
    {"doc_id": str(document_id), "n": 10},
)
rows = result.mappings().all()
```

---

## Query Patterns

### Select and Filter

```python
from sqlalchemy import select, and_, or_

# Single object by ID with ownership check
stmt = select(Conversation).where(
    and_(Conversation.id == conversation_id, Conversation.user_id == user_id)
)
conversation = (await session.execute(stmt)).scalar_one_or_none()

# Paginated messages (cursor-based)
stmt = (
    select(Message)
    .where(
        Message.conversation_id == conversation_id,
        Message.created_at < cursor_time,  # cursor from previous page
    )
    .order_by(Message.created_at.desc())
    .limit(page_size)
)
```

### Aggregations

```python
from sqlalchemy import func

stmt = (
    select(
        Conversation.id,
        func.count(Message.id).label("message_count"),
        func.coalesce(func.sum(Message.token_count), 0).label("total_tokens"),
    )
    .join(Message, Message.conversation_id == Conversation.id)
    .where(Conversation.user_id == user_id)
    .group_by(Conversation.id)
    .order_by(func.max(Message.created_at).desc())
)
```

### Upsert (PostgreSQL)

```python
from sqlalchemy.dialects.postgresql import insert

stmt = (
    insert(User)
    .values(email=email, display_name=name)
    .on_conflict_do_update(
        index_elements=["email"],
        set_={"display_name": name, "updated_at": func.now()},
    )
    .returning(User)
)
user = (await session.execute(stmt)).scalar_one()
```

### Bulk Insert Messages

```python
async def add_messages_batch(
    session: AsyncSession,
    conversation_id: UUID,
    messages: list[dict],
) -> None:
    await session.execute(
        insert(Message),
        [
            {
                "conversation_id": conversation_id,
                "role": m["role"],
                "content": m["content"],
                "token_count": m.get("token_count"),
            }
            for m in messages
        ],
    )
```

---

## Transactions

### Explicit Transaction Boundaries

```python
async def transfer_and_log(
    session: AsyncSession,
    user_id: UUID,
    document_id: UUID,
    new_status: str,
) -> None:
    async with session.begin_nested():  # SAVEPOINT
        doc = await session.get(Document, document_id, with_for_update=True)
        if doc is None or doc.user_id != user_id:
            raise ValueError("Document not found")
        doc.status = new_status

    # Outer transaction commits via FastAPI dependency
```

### `with_for_update()` for Concurrency

Use row-level locks when multiple workers might update the same document ingestion status:

```python
stmt = (
    select(Document)
    .where(Document.id == document_id, Document.status == "pending")
    .with_for_update(skip_locked=True)  # skip rows locked by other workers
)
doc = (await session.execute(stmt)).scalar_one_or_none()
```

### Multi-Repository Transactions

Pass the same `AsyncSession` instance to multiple repository methods within one request — they share the transaction automatically.

```python
async def ingest_document(session: AsyncSession, user_id: UUID, file_meta: dict) -> UUID:
    doc_repo = PostgresDocumentRepository(session)
    usage_repo = PostgresUsageRepository(session)

    doc_id = await doc_repo.create(user_id, file_meta)
    await usage_repo.record_storage_event(user_id, file_meta["size_bytes"])
    # Single commit when request completes
    return doc_id
```

---

## Repository Pattern

Repositories hide SQLAlchemy from services. Define ABC interfaces; implement with `AsyncSession`.

```python
# app/db/repositories/conversation.py
from abc import ABC, abstractmethod
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.db.models import Conversation, Message


class ConversationRepository(ABC):
    @abstractmethod
    async def create(self, user_id: UUID, model: str, title: str | None = None) -> UUID: ...

    @abstractmethod
    async def get_with_messages(
        self, conversation_id: UUID, user_id: UUID, limit: int
    ) -> Conversation | None: ...

    @abstractmethod
    async def add_message(
        self,
        conversation_id: UUID,
        role: str,
        content: str,
        token_count: int | None = None,
        metadata: dict | None = None,
    ) -> UUID: ...

    @abstractmethod
    async def list_for_user(self, user_id: UUID, limit: int, offset: int) -> list[Conversation]: ...


class PostgresConversationRepository(ConversationRepository):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def create(self, user_id: UUID, model: str, title: str | None = None) -> UUID:
        conversation = Conversation(user_id=user_id, model=model, title=title)
        self._session.add(conversation)
        await self._session.flush()
        return conversation.id

    async def get_with_messages(
        self, conversation_id: UUID, user_id: UUID, limit: int
    ) -> Conversation | None:
        stmt = (
            select(Conversation)
            .where(Conversation.id == conversation_id, Conversation.user_id == user_id)
            .options(selectinload(Conversation.messages))
        )
        conversation = (await self._session.execute(stmt)).scalar_one_or_none()
        if conversation and len(conversation.messages) > limit:
            conversation.messages = conversation.messages[-limit:]
        return conversation

    async def add_message(
        self,
        conversation_id: UUID,
        role: str,
        content: str,
        token_count: int | None = None,
        metadata: dict | None = None,
    ) -> UUID:
        message = Message(
            conversation_id=conversation_id,
            role=role,
            content=content,
            token_count=token_count,
            metadata_=metadata or {},
        )
        self._session.add(message)
        await self._session.flush()
        return message.id

    async def list_for_user(self, user_id: UUID, limit: int, offset: int) -> list[Conversation]:
        stmt = (
            select(Conversation)
            .where(Conversation.user_id == user_id)
            .order_by(Conversation.created_at.desc())
            .limit(limit)
            .offset(offset)
        )
        return list((await self._session.execute(stmt)).scalars().all())
```

### Document Repository

```python
class PostgresDocumentRepository:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def create_pending(
        self,
        user_id: UUID,
        filename: str,
        storage_key: str,
        mime_type: str,
        size_bytes: int,
    ) -> UUID:
        doc = Document(
            user_id=user_id,
            filename=filename,
            storage_key=storage_key,
            mime_type=mime_type,
            size_bytes=size_bytes,
            status="pending",
        )
        self._session.add(doc)
        await self._session.flush()
        return doc.id

    async def claim_for_processing(self, document_id: UUID) -> Document | None:
        stmt = (
            select(Document)
            .where(Document.id == document_id, Document.status == "pending")
            .with_for_update(skip_locked=True)
        )
        doc = (await self._session.execute(stmt)).scalar_one_or_none()
        if doc:
            doc.status = "processing"
            await self._session.flush()
        return doc

    async def mark_indexed(self, document_id: UUID, chunk_count: int) -> None:
        doc = await self._session.get(Document, document_id)
        if doc:
            doc.status = "indexed"
            doc.chunk_count = chunk_count
```

### Wiring in FastAPI

```python
def get_conversation_repo(session: AsyncSession = Depends(get_db)) -> ConversationRepository:
    return PostgresConversationRepository(session)


@router.post("/conversations/{conversation_id}/messages")
async def send_message(
    conversation_id: UUID,
    body: MessageCreate,
    user: User = Depends(get_current_user),
    repo: ConversationRepository = Depends(get_conversation_repo),
):
    conv = await repo.get_with_messages(conversation_id, user.id, limit=1)
    if conv is None:
        raise HTTPException(404, "Conversation not found")
    message_id = await repo.add_message(conversation_id, "user", body.content)
    return {"message_id": message_id}
```

---

## Testing with SQLAlchemy

### In-Memory Fake Repository

```python
class InMemoryConversationRepository(ConversationRepository):
    def __init__(self) -> None:
        self._conversations: dict[UUID, Conversation] = {}
        self._messages: dict[UUID, list[Message]] = {}

    async def create(self, user_id: UUID, model: str, title: str | None = None) -> UUID:
        conv = Conversation(id=uuid4(), user_id=user_id, model=model, title=title)
        self._conversations[conv.id] = conv
        self._messages[conv.id] = []
        return conv.id

    async def add_message(self, conversation_id: UUID, role: str, content: str, **_) -> UUID:
        msg = Message(id=uuid4(), conversation_id=conversation_id, role=role, content=content)
        self._messages[conversation_id].append(msg)
        return msg.id
```

### Integration Tests with Testcontainers

```python
import pytest
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

@pytest.fixture
async def db_session():
    engine = create_async_engine("postgresql+asyncpg://test:test@localhost:5433/testdb")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    factory = async_sessionmaker(engine, expire_on_commit=False)
    async with factory() as session:
        yield session
    await engine.dispose()
```

Run migrations against the test database instead of `create_all()` when testing migration compatibility — see [Alembic Migrations for AI](alembic-migrations-for-ai.md).

---

## Common Mistakes

| Mistake | Impact | Fix |
|---------|--------|-----|
| Sync driver in async FastAPI | Event loop blocking, latency spikes | `postgresql+asyncpg://` |
| Lazy loading after session close | `DetachedInstanceError` | `selectinload` or `expire_on_commit=False` |
| N+1 queries loading messages | 1 query per conversation | `selectinload(Conversation.messages)` |
| Business logic in route handlers | Untestable, tangled code | Repository + service layer |
| `datetime.utcnow()` as default | Timezone-naive timestamps | `server_default=func.now()` |
| Missing model exports for Alembic | Autogenerate misses tables | Export all models in `models/__init__.py` |
| One session per repository method | Broken transactions | Inject shared `AsyncSession` |
| Storing blobs in ORM models | Table bloat | `storage_key` + object storage |

---

## Interview Preparation

### Frequently Asked Questions

**Q1: Why use SQLAlchemy instead of raw SQL or an async query builder?**

> **Strong answer:** SQLAlchemy 2.0 gives typed ORM models, composable query building, connection pooling, and Alembic integration. Raw SQL is fine for specialized queries (pgvector similarity), but ORM models keep schema and Python types in sync. Repositories wrap SQLAlchemy so services stay testable with fakes.

**Q2: How do you prevent N+1 queries when loading a user's conversations with recent messages?**

> **Strong answer:** Use `selectinload(Conversation.messages)` in the initial query, or fetch conversations and messages in two queries with `WHERE conversation_id IN (...)`. Never access `conversation.messages` in a loop without eager loading. Monitor with SQL logging or APM query counts.

**Q3: How do you design a document ingestion schema?**

> **Strong answer:** `documents` table with `status` CHECK constraint (`pending → processing → indexed → failed`), `storage_key` for S3, `chunk_count` for RAG metadata. Workers claim rows with `SELECT ... FOR UPDATE SKIP LOCKED`. Chunks and embeddings in a separate table — see [PostgreSQL for AI](postgresql-for-ai.md). Never store file bytes in PostgreSQL.

**Q4: Sync vs async session — when does it matter?**

> **Strong answer:** Async matters in FastAPI because each blocked DB call stalls all concurrent requests on that worker. Use `AsyncSession` + `asyncpg`. Sync is acceptable for batch scripts and synchronous workers where concurrency is process-based, not coroutine-based.

### Real-World Scenario

**Scenario:** After deploying a new feature, API latency doubles. APM shows 50+ SQL queries per chat request.

> **Discussion points:**
> 1. Likely N+1 — loading messages per conversation in a loop.
> 2. Add `selectinload` or batch message fetch.
> 3. Check for lazy-loaded relationships accessed after session close (may cause hidden extra queries).
> 4. Review pagination — loading entire message history instead of last N messages.
> 5. Add query count integration test as a regression guard.

---

## Navigation

### Prerequisites

- [Databases for AI Applications](../databases-for-ai-applications.md)
- [PostgreSQL for AI](postgresql-for-ai.md) — pgvector, JSONB, production tuning
- [Software Engineering for AI](../../foundations/software-engineering-for-ai.md)
- [Python for AI Engineering](../../python-engineering/python-for-ai-engineering.md)

### Related Topics

- [Alembic Migrations for AI](alembic-migrations-for-ai.md) — schema versioning
- [Redis for AI](../redis/redis-for-ai.md) — ephemeral cache alongside PostgreSQL
- [Backend Fundamentals for AI](../../backend-engineering/backend-fundamentals-for-ai.md)
- [FastAPI Foundation](../../fastapi/fastapi-foundation.md)

### Next Topics

- [Alembic Migrations for AI](alembic-migrations-for-ai.md) — evolve schemas safely
- [Redis Backend Patterns for AI](../redis/redis-backend-patterns-for-ai.md) — cache and rate limits

---

## See Also

- [PostgreSQL Subdomain README](README.md)
- [Databases Domain README](../README.md)
- [Master Index](../../../meta/indexes/MASTER-INDEX.md)

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Initial version — SQLAlchemy 2.0 async ORM, schema design, repositories, transactions |
