"""FastAPI dependency injection example for AI services.

Demonstrates wiring LLM clients and services via Depends(),
and overriding dependencies in tests.

Prerequisites:
    pip install fastapi uvicorn httpx pytest

Run:
    uvicorn example-dependency-injection:app --reload
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from functools import lru_cache

from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel, SecretStr
from pydantic_settings import BaseSettings


# --- Configuration ---


class Settings(BaseSettings):
    openai_api_key: SecretStr = SecretStr("test-key")
    llm_model: str = "gpt-4o-mini"


@lru_cache
def get_settings() -> Settings:
    return Settings()


# --- Domain ---


@dataclass
class LLMResponse:
    content: str
    model: str


class LLMClient(ABC):
    @abstractmethod
    async def complete(self, prompt: str) -> LLMResponse:
        ...


class OpenAIClient(LLMClient):
    def __init__(self, api_key: str, model: str):
        self._api_key = api_key
        self._model = model

    async def complete(self, prompt: str) -> LLMResponse:
        # Production: call OpenAI API
        return LLMResponse(content=f"[OpenAI] Response to: {prompt}", model=self._model)


class MockLLMClient(LLMClient):
    async def complete(self, prompt: str) -> LLMResponse:
        return LLMResponse(content=f"[Mock] Response to: {prompt}", model="mock")


class ChatService:
    def __init__(self, llm: LLMClient):
        self._llm = llm

    async def chat(self, message: str) -> str:
        response = await self._llm.complete(message)
        return response.content


# --- Dependencies ---


def get_llm_client(settings: Settings = Depends(get_settings)) -> LLMClient:
    return OpenAIClient(
        api_key=settings.openai_api_key.get_secret_value(),
        model=settings.llm_model,
    )


def get_chat_service(llm: LLMClient = Depends(get_llm_client)) -> ChatService:
    return ChatService(llm=llm)


# --- API ---


app = FastAPI(title="DI Example")


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    response: str


@app.post("/v1/chat", response_model=ChatResponse)
async def chat(
    body: ChatRequest,
    service: ChatService = Depends(get_chat_service),
):
    content = await service.chat(body.message)
    return ChatResponse(response=content)


# --- Test override example (run with pytest) ---

def test_chat_with_mock():
    from fastapi.testclient import TestClient

    app.dependency_overrides[get_llm_client] = lambda: MockLLMClient()
    client = TestClient(app)
    response = client.post("/v1/chat", json={"message": "Hello"})
    assert response.status_code == 200
    assert "[Mock]" in response.json()["response"]
    app.dependency_overrides.clear()
