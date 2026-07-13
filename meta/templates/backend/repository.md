---
title: "Repository Template"
description: "Template for a data access repository in an AI backend."
type: backend-template
---

# Repository Template

## Abstract Port (domain/repositories/)

```python
from abc import ABC, abstractmethod

from my_ai_api.models.conversation import Conversation


class ConversationRepository(ABC):
    @abstractmethod
    async def get_by_id(self, conversation_id: str) -> Conversation | None: ...

    @abstractmethod
    async def list_by_user(self, user_id: str, limit: int = 20) -> list[Conversation]: ...

    @abstractmethod
    async def save(self, conversation: Conversation) -> Conversation: ...

    @abstractmethod
    async def delete(self, conversation_id: str) -> bool: ...
```

## SQLAlchemy Implementation (repositories/)

```python
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from my_ai_api.models.conversation import Conversation as ConversationORM
from my_ai_api.repositories.conversation import ConversationRepository


class SQLAlchemyConversationRepository(ConversationRepository):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_by_id(self, conversation_id: str) -> ConversationORM | None:
        result = await self._session.execute(
            select(ConversationORM).where(ConversationORM.id == conversation_id)
        )
        return result.scalar_one_or_none()

    async def save(self, conversation: ConversationORM) -> ConversationORM:
        self._session.add(conversation)
        await self._session.flush()
        await self._session.refresh(conversation)
        return conversation
```

## DI Wiring

```python
async def get_conversation_repo(
    session: AsyncSession = Depends(get_db_session),
) -> ConversationRepository:
    return SQLAlchemyConversationRepository(session)
```

## See Also

- [SQLAlchemy for AI Applications](../../../domains/databases/postgresql/sqlalchemy-for-ai-applications.md)
