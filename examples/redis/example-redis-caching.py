"""Redis caching patterns for AI backends.

Prerequisites: pip install redis

Run: REDIS_URL=redis://localhost:6379/0 python example-redis-caching.py
"""

from __future__ import annotations

import hashlib
import json
import os

import redis.asyncio as redis

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")


class LLMResponseCache:
    def __init__(self, redis_client: redis.Redis, ttl_seconds: int = 3600):
        self._redis = redis_client
        self._ttl = ttl_seconds

    def _cache_key(self, model: str, prompt: str) -> str:
        digest = hashlib.sha256(f"{model}:{prompt}".encode()).hexdigest()
        return f"llm:cache:{digest}"

    async def get(self, model: str, prompt: str) -> str | None:
        key = self._cache_key(model, prompt)
        cached = await self._redis.get(key)
        return cached.decode() if cached else None

    async def set(self, model: str, prompt: str, response: str) -> None:
        key = self._cache_key(model, prompt)
        await self._redis.setex(key, self._ttl, response)


class RateLimiter:
    def __init__(self, redis_client: redis.Redis, max_requests: int = 60, window_seconds: int = 60):
        self._redis = redis_client
        self._max = max_requests
        self._window = window_seconds

    async def is_allowed(self, user_id: str) -> bool:
        key = f"rate:{user_id}"
        pipe = self._redis.pipeline()
        pipe.incr(key)
        pipe.expire(key, self._window)
        results = await pipe.execute()
        return results[0] <= self._max


async def main() -> None:
    client = redis.from_url(REDIS_URL, decode_responses=False)
    cache = LLMResponseCache(client)

    prompt = "What is RAG?"
    model = "gpt-4o-mini"

    hit = await cache.get(model, prompt)
    if hit:
        print("Cache hit:", hit)
    else:
        response = "RAG stands for Retrieval Augmented Generation."
        await cache.set(model, prompt, response)
        print("Cache miss — stored:", response)

    await client.aclose()


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
