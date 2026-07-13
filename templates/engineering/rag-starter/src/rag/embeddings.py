"""Embedding provider interface — swap OpenAI, Cohere, local models."""

import hashlib


class EmbeddingProvider:
  def embed(self, texts: list[str]) -> list[list[float]]:
      return [[float(int(hashlib.md5(t.encode()).hexdigest()[:8], 16) % 1000) / 1000] * 8 for t in texts]
