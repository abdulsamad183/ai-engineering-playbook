"""Health and readiness endpoints for AI FastAPI services.

Run: uvicorn example-health-endpoints:app --port 8000
"""

from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(title="AI Service")


@app.get("/health")
async def health() -> dict:
    return {"status": "ok"}


@app.get("/ready")
async def ready() -> JSONResponse:
  # In production: ping Redis, Postgres, LLM API
    checks = {"database": True, "redis": True, "llm_provider": True}
    if all(checks.values()):
        return JSONResponse({"status": "ready", "checks": checks})
    return JSONResponse({"status": "not_ready", "checks": checks}, status_code=503)
