"""WebSocket chat endpoint for real-time AI applications.

Run: uvicorn example-websocket-chat:app --reload
Test: websocat ws://localhost:8000/ws/chat
"""

from __future__ import annotations

import json

from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI(title="WebSocket Chat Example")


class ConnectionManager:
    def __init__(self):
        self.active: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active.remove(websocket)

    async def send_json(self, websocket: WebSocket, data: dict):
        await websocket.send_text(json.dumps(data))


manager = ConnectionManager()


@app.websocket("/ws/chat")
async def websocket_chat(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            raw = await websocket.receive_text()
            message = json.loads(raw)

            # Acknowledge receipt
            await manager.send_json(websocket, {"type": "ack", "message_id": message.get("id")})

            # Simulate streaming LLM response
            response_text = f"Echo: {message.get('content', '')}"
            for word in response_text.split():
                await manager.send_json(websocket, {"type": "token", "content": word + " "})
            await manager.send_json(websocket, {"type": "done"})

    except WebSocketDisconnect:
        manager.disconnect(websocket)
