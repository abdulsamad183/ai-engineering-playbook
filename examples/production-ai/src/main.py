"""Dockerized FastAPI AI service entrypoint.

Build: docker build -f Dockerfile -t ai-playbook-api .
Run: docker run -p 8000:8000 ai-playbook-api
"""

from fastapi import FastAPI

app = FastAPI(title="AI Playbook API")


@app.get("/health")
async def health() -> dict:
    return {"status": "ok"}


@app.post("/chat")
async def chat(body: dict) -> dict:
    message = body.get("message", "")
    return {"reply": f"echo: {message}"}
