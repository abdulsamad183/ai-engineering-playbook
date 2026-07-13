---
title: "API Response Template"
description: "Standard API response envelope for AI backends."
type: backend-template
---

# API Response Template

## Standard Envelope

```python
from typing import Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class APIResponse(BaseModel, Generic[T]):
    data: T
    meta: dict = Field(default_factory=dict)


class APIError(BaseModel):
    code: str
    message: str
    details: dict | None = None


class ErrorResponse(BaseModel):
    error: APIError
    request_id: str | None = None
```

## Paginated Response

```python
class PaginationMeta(BaseModel):
    cursor: str | None = None
    has_more: bool = False
    total: int | None = None


class PaginatedResponse(BaseModel, Generic[T]):
    data: list[T]
    meta: PaginationMeta
```

## Usage in Route

```python
@router.get("/conversations", response_model=PaginatedResponse[ConversationResponse])
async def list_conversations(...) -> PaginatedResponse[ConversationResponse]:
    items, cursor, has_more = await service.list_conversations(...)
    return PaginatedResponse(
        data=[ConversationResponse.model_validate(i) for i in items],
        meta=PaginationMeta(cursor=cursor, has_more=has_more),
    )
```

## See Also

- [API Design for AI](../../../domains/apis/api-design-for-ai.md)
