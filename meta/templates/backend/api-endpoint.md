---
title: "API Endpoint Template"
description: "Template for a production FastAPI endpoint in an AI backend."
type: backend-template
---

# API Endpoint Template

## File Location

`src/my_ai_api/api/v1/endpoints/{resource}.py`

## Template

```python
from fastapi import APIRouter, Depends, HTTPException, status

from my_ai_api.api.dependencies import get_{service}_service, get_current_user
from my_ai_api.schemas.{resource} import {Resource}Request, {Resource}Response
from my_ai_api.services.{resource}_service import {Resource}Service
from my_ai_api.core.exceptions import {Resource}NotFoundError

router = APIRouter(prefix="/{resources}", tags=["{resources}"])


@router.post(
    "",
    response_model={Resource}Response,
    status_code=status.HTTP_201_CREATED,
    summary="Create {resource}",
)
async def create_{resource}(
    body: {Resource}Request,
    service: {Resource}Service = Depends(get_{service}_service),
    user=Depends(get_current_user),
) -> {Resource}Response:
    result = await service.create(user_id=user.id, data=body)
    return {Resource}Response.model_validate(result)


@router.get(
    "/{id}",
    response_model={Resource}Response,
    summary="Get {resource} by ID",
)
async def get_{resource}(
    id: str,
    service: {Resource}Service = Depends(get_{service}_service),
    user=Depends(get_current_user),
) -> {Resource}Response:
    try:
        result = await service.get_by_id(id, user_id=user.id)
    except {Resource}NotFoundError:
        raise HTTPException(status_code=404, detail="{Resource} not found")
    return {Resource}Response.model_validate(result)
```

## Rules

1. Route handlers validate input and delegate — no business logic.
2. Use `response_model` for output validation.
3. Map domain exceptions to HTTP status codes here.
4. Protect with `Depends(get_current_user)` when auth required.

## See Also

- [API Design for AI](../../../domains/apis/api-design-for-ai.md)
- [Service Template](service.md)
