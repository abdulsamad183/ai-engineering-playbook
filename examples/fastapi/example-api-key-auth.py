"""API key authentication example for AI backends.

Run: uvicorn example-api-key-auth:app --reload
     curl -H "X-API-Key: test-key-123" http://localhost:8000/v1/chat
"""

from __future__ import annotations

import hashlib
import secrets

from fastapi import Depends, FastAPI, HTTPException, Security, status
from fastapi.security import APIKeyHeader
from pydantic import BaseModel

app = FastAPI(title="API Key Auth Example")

api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)

# Production: store hashed keys in database
VALID_KEY_HASHES = {
    hashlib.sha256(b"test-key-123").hexdigest(),
}


def hash_api_key(key: str) -> str:
    return hashlib.sha256(key.encode()).hexdigest()


async def verify_api_key(api_key: str | None = Security(api_key_header)) -> str:
    if api_key is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing API key",
        )
    key_hash = hash_api_key(api_key)
    if key_hash not in VALID_KEY_HASHES:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API key",
        )
    return api_key


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    response: str


@app.post("/v1/chat", response_model=ChatResponse)
async def chat(
    body: ChatRequest,
    api_key: str = Depends(verify_api_key),
):
    return ChatResponse(response=f"Authenticated request: {body.message}")


def generate_api_key() -> str:
    """Use when issuing new API keys to customers."""
    return secrets.token_urlsafe(32)
