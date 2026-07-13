---
title: "Service Template"
description: "Template for a service layer class in an AI backend."
type: backend-template
---

# Service Template

## File Location

`src/my_ai_api/services/{name}_service.py`

## Template

```python
import logging

from my_ai_api.clients.llm import LLMClient
from my_ai_api.core.exceptions import ConversationNotFoundError
from my_ai_api.repositories.conversation import ConversationRepository
from my_ai_api.schemas.chat import ChatRequest, ChatResponse


class ChatService:
    def __init__(
        self,
        conversation_repo: ConversationRepository,
        llm_client: LLMClient,
        logger: logging.Logger,
    ) -> None:
        self._repo = conversation_repo
        self._llm = llm_client
        self._logger = logger

    async def send_message(self, request: ChatRequest, user_id: str) -> ChatResponse:
        conversation = await self._repo.get_by_id(request.conversation_id)
        if conversation is None or conversation.user_id != user_id:
            raise ConversationNotFoundError(request.conversation_id)

        conversation.add_user_message(request.message)

        llm_response = await self._llm.complete(
            messages=conversation.to_llm_messages(),
            model=request.model,
        )

        conversation.add_assistant_message(llm_response.content)
        await self._repo.save(conversation)

        self._logger.info(
            "chat_completed",
            extra={
                "conversation_id": conversation.id,
                "model": llm_response.model,
                "tokens": llm_response.total_tokens,
            },
        )

        return ChatResponse(
            conversation_id=conversation.id,
            message=llm_response.content,
            model=llm_response.model,
        )
```

## Rules

1. Services orchestrate — they do not know about HTTP.
2. Inject all dependencies via constructor.
3. Log business events with structured `extra` fields.
4. Raise domain exceptions; routes map to HTTP errors.

## See Also

- [Backend Architecture for AI](../../../domains/backend-engineering/backend-architecture-for-ai.md)
