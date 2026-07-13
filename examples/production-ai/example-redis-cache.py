"""Redis caching pattern for AI responses.

Run: python example-redis-cache.py
"""

import hashlib
import json
from typing import Callable


class MemoryRedis:
    """Stand-in for redis-py when Redis not running."""

    def __init__(self) -> None:
        self._store: dict[str, str] = {}

    def get(self, key: str) -> str | None:
        return self._store.get(key)

    def setex(self, key: str, ttl: int, value: str) -> None:
        self._store[key] = value  # TTL ignored in demo


def cache_key(prompt: str, model: str, version: str) -> str:
    raw = f"{version}:{model}:{prompt}"
    return "ai:resp:" + hashlib.sha256(raw.encode()).hexdigest()


def cached_llm_call(redis: MemoryRedis, prompt: str, model: str, version: str, fn: Callable) -> str:
    key = cache_key(prompt, model, version)
    hit = redis.get(key)
    if hit:
        return json.loads(hit)["text"]
    text = fn(prompt)
    redis.setex(key, 300, json.dumps({"text": text}))
    return text


if __name__ == "__main__":
    r = MemoryRedis()
    calls = {"n": 0}

    def llm(p: str) -> str:
        calls["n"] += 1
        return "cached answer"

    print(cached_llm_call(r, "hi", "gpt-4", "v1", llm))
    print(cached_llm_call(r, "hi", "gpt-4", "v1", llm))
    print("llm calls:", calls["n"])
