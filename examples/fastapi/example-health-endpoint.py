"""Health and readiness endpoints for AI backends.

Run: uvicorn example-health-endpoint:app --reload
"""

from fastapi import FastAPI, Response, status
from pydantic import BaseModel

app = FastAPI(title="Health Check Example")


class HealthResponse(BaseModel):
    status: str
    version: str = "1.0.0"


class ReadinessResponse(BaseModel):
    status: str
    checks: dict[str, str]


@app.get("/health", response_model=HealthResponse)
async def health():
    """Liveness probe — is the process running?"""
    return HealthResponse(status="ok")


@app.get("/ready", response_model=ReadinessResponse)
async def readiness(response: Response):
    """Readiness probe — can the service handle traffic?"""
    checks = {
        "database": await check_database(),
        "redis": await check_redis(),
        "llm_api": await check_llm_reachable(),
    }
    all_ok = all(v == "ok" for v in checks.values())
    if not all_ok:
        response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE
    return ReadinessResponse(
        status="ok" if all_ok else "degraded",
        checks=checks,
    )


async def check_database() -> str:
    # Production: execute SELECT 1 against PostgreSQL
    return "ok"


async def check_redis() -> str:
    # Production: PING redis
    return "ok"


async def check_llm_reachable() -> str:
    # Production: lightweight HEAD request or cached health check
    return "ok"
