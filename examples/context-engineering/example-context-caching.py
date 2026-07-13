"""Context caching — retrieval result cache with version key.

Run: python example-context-caching.py
"""

from __future__ import annotations

import hashlib
import json
import time


class RetrievalCache:
    def __init__(self, ttl_seconds: int = 300):
        self.ttl = ttl_seconds
        self._store: dict[str, tuple[float, list[dict]]] = {}

    def _key(self, query: str, tenant_id: str, index_version: int) -> str:
        payload = json.dumps({"q": query.lower().strip(), "t": tenant_id, "v": index_version})
        return hashlib.sha256(payload.encode()).hexdigest()[:16]

    def get(self, query: str, tenant_id: str, index_version: int) -> list[dict] | None:
        key = self._key(query, tenant_id, index_version)
        entry = self._store.get(key)
        if not entry:
            return None
        expires_at, value = entry
        if time.time() > expires_at:
            del self._store[key]
            return None
        return value

    def set(self, query: str, tenant_id: str, index_version: int, chunks: list[dict]) -> None:
        key = self._key(query, tenant_id, index_version)
        self._store[key] = (time.time() + self.ttl, chunks)


if __name__ == "__main__":
    cache = RetrievalCache(ttl_seconds=60)
    chunks = [{"id": "doc-1", "text": "Refund policy"}]
    cache.set("refund policy", "tenant-a", index_version=3, chunks=chunks)
    print(cache.get("refund policy", "tenant-a", 3))
