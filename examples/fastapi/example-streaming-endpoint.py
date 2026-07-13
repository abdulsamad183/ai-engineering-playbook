"""FastAPI streaming endpoint example.

Demonstrates Server-Sent Events (SSE) for streaming LLM responses.

Prerequisites:
    pip install fastapi uvicorn

Run:
    uvicorn example-streaming-endpoint:app --reload
    curl -N http://localhost:8000/v1/chat/stream -H "Content-Type: application/json" \
         -d '{"message": "Hello"}'
"""

from __future__ import annotations

import asyncio
from collections.abc import AsyncGenerator

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Streaming Chat Example")


class ChatRequest(BaseModel):
    message: str


async def mock_llm_stream(prompt: str) -> AsyncGenerator[str, None]:
    """Simulate token-by-token LLM streaming."""
    response = f"You asked: {prompt}. Here is a streamed response about AI engineering."
    for word in response.split():
        yield word + " "
        await asyncio.sleep(0.1)


@app.post("/v1/chat/stream")
async def stream_chat(request: ChatRequest):
    from fastapi.responses import StreamingResponse

    async def event_generator():
        async for token in mock_llm_stream(request.message):
            yield f"data: {token}\n\n"
        yield "data: [DONE]\n\n"

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )


@app.get("/health")
async def health():
    return {"status": "ok"}
