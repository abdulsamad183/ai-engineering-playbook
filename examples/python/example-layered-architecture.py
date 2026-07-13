"""Layered architecture example for AI applications.

Demonstrates clean separation: domain ports, infrastructure adapters,
service layer, and thin API routes. Swap LLM providers without changing
business logic.

Run: python example-layered-architecture.py
"""

from __future__ import annotations

import asyncio
import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Protocol

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
logger = logging.getLogger(__name__)


# --- Domain Layer ---


@dataclass
class Message:
    role: str
    content: str


@dataclass
class Conversation:
    id: str
    messages: list[Message] = field(default_factory=list)

    def add_message(self, role: str, content: str) -> None:
        self.messages.append(Message(role=role, content=content))


@dataclass
class LLMResponse:
    content: str
    model: str
    input_tokens: int = 0
    output_tokens: int = 0


class LLMClient(ABC):
    @abstractmethod
    async def complete(self, prompt: str, system: str = "") -> LLMResponse:
        ...


class ConversationRepository(ABC):
    @abstractmethod
    async def get_by_id(self, conversation_id: str) -> Conversation | None:
        ...

    @abstractmethod
    async def save(self, conversation: Conversation) -> None:
        ...


# --- Infrastructure Layer ---


class MockLLMClient(LLMClient):
  """Test double — swap for OpenAIClient in production."""

  def __init__(self, model: str = "mock-gpt-4o-mini"):
      self._model = model

  async def complete(self, prompt: str, system: str = "") -> LLMResponse:
      await asyncio.sleep(0.05)  # simulate network latency
      return LLMResponse(
          content=f"[mock response to: {prompt[:50]}...]",
          model=self._model,
          input_tokens=len(prompt.split()),
          output_tokens=10,
      )


class InMemoryConversationRepository(ConversationRepository):
    def __init__(self) -> None:
        self._store: dict[str, Conversation] = {}

    async def get_by_id(self, conversation_id: str) -> Conversation | None:
        return self._store.get(conversation_id)

    async def save(self, conversation: Conversation) -> None:
        self._store[conversation.id] = conversation


# --- Service Layer ---


class ConversationNotFoundError(Exception):
    pass


class ChatService:
    def __init__(
        self,
        llm: LLMClient,
        repo: ConversationRepository,
        logger: logging.Logger,
    ) -> None:
        self._llm = llm
        self._repo = repo
        self._logger = logger

    async def send_message(self, conversation_id: str, user_message: str) -> str:
        conversation = await self._repo.get_by_id(conversation_id)
        if conversation is None:
            raise ConversationNotFoundError(conversation_id)

        conversation.add_message("user", user_message)
        response = await self._llm.complete(
            prompt=user_message,
            system="You are a helpful AI engineering assistant.",
        )
        conversation.add_message("assistant", response.content)
        await self._repo.save(conversation)

        self._logger.info(
            "message_processed conversation=%s model=%s tokens=%d",
            conversation_id,
            response.model,
            response.input_tokens + response.output_tokens,
        )
        return response.content


# --- API Layer (thin) ---


class ChatAPI:
    """Simulates a FastAPI route handler — validates input, delegates to service."""

    def __init__(self, chat_service: ChatService) -> None:
        self._service = chat_service

    async def post_message(self, conversation_id: str, message: str) -> dict:
        try:
            response = await self._service.send_message(conversation_id, message)
            return {"response": response}
        except ConversationNotFoundError:
            return {"error": "Conversation not found", "status": 404}


# --- Composition Root ---


def build_app() -> ChatAPI:
    llm = MockLLMClient()
    repo = InMemoryConversationRepository()
    service = ChatService(llm=llm, repo=repo, logger=logger)
    return ChatAPI(chat_service=service)


async def main() -> None:
    app = build_app()
    repo = InMemoryConversationRepository()
    await repo.save(Conversation(id="conv-1"))

    # Re-wire with shared repo for demo
    llm = MockLLMClient()
    service = ChatService(llm=llm, repo=repo, logger=logger)
    api = ChatAPI(chat_service=service)

    result = await api.post_message("conv-1", "What is clean architecture?")
    print("API response:", result)


if __name__ == "__main__":
    asyncio.run(main())
