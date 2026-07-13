"""OpenAI embeddings API example.

Run: python example-embeddings.py
"""

from __future__ import annotations

import os

import numpy as np
from openai import AsyncOpenAI

client = AsyncOpenAI(api_key=os.environ["OPENAI_API_KEY"])


def cosine_similarity(a: list[float], b: list[float]) -> float:
    va, vb = np.array(a), np.array(b)
    return float(np.dot(va, vb) / (np.linalg.norm(va) * np.linalg.norm(vb)))


async def embed_texts(texts: list[str], model: str = "text-embedding-3-small") -> list[list[float]]:
    response = await client.embeddings.create(input=texts, model=model)
    return [item.embedding for item in response.data]


async def main() -> None:
    texts = [
        "Retrieval augmented generation improves LLM answers.",
        "RAG uses vector search to find relevant context.",
        "The weather in Paris is sunny today.",
    ]
    embeddings = await embed_texts(texts)
    sim_01 = cosine_similarity(embeddings[0], embeddings[1])
    sim_02 = cosine_similarity(embeddings[0], embeddings[2])
    print(f"RAG ↔ RAG context: {sim_01:.4f}")
    print(f"RAG ↔ weather:     {sim_02:.4f}")


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
