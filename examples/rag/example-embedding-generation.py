"""Embedding generation batch pattern.

Run: python example-embedding-generation.py
"""

from __future__ import annotations


async def embed_texts_batched(
    texts: list[str],
    embed_fn,
    batch_size: int = 100,
) -> list[list[float]]:
    vectors: list[list[float]] = []
    for i in range(0, len(texts), batch_size):
        batch = texts[i : i + batch_size]
        vectors.extend(await embed_fn(batch))
    return vectors


def mock_embed_batch(texts: list[str]) -> list[list[float]]:
    return [[float(len(t) % 10)] * 4 for t in texts]


async def main() -> None:
    texts = [f"chunk {i}" for i in range(250)]
    vecs = await embed_texts_batched(texts, lambda b: mock_embed_batch(b), batch_size=100)
    print(len(vecs))


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
