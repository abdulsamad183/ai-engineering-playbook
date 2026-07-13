"""Complete RAG pipeline reference — ingest, index, retrieve, generate.

Run: python example-complete-rag-pipeline.py
"""

from __future__ import annotations

from dataclasses import dataclass, field
import hashlib


@dataclass
class Chunk:
    chunk_id: str
    doc_id: str
    text: str
    metadata: dict = field(default_factory=dict)


@dataclass
class InMemoryVectorIndex:
    """Demo index; swap for Qdrant/pgvector in production."""

    _chunks: dict[str, Chunk] = field(default_factory=dict)
    _vectors: dict[str, list[float]] = field(default_factory=dict)

    def upsert(self, chunk: Chunk, vector: list[float]) -> None:
        self._chunks[chunk.chunk_id] = chunk
        self._vectors[chunk.chunk_id] = vector

    def search(self, query_vec: list[float], top_k: int = 5, filters: dict | None = None) -> list[Chunk]:
        def score(cid: str) -> float:
            v = self._vectors[cid]
            return sum(a * b for a, b in zip(query_vec, v))

        candidates = []
        for cid, chunk in self._chunks.items():
            if filters and not all(chunk.metadata.get(k) == v for k, v in filters.items()):
                continue
            candidates.append((score(cid), chunk))
        candidates.sort(key=lambda x: -x[0])
        return [c for _, c in candidates[:top_k]]


def chunk_document(doc_id: str, text: str, size: int = 500) -> list[Chunk]:
    chunks = []
    for i in range(0, len(text), size):
        part = text[i : i + size]
        cid = f"{doc_id}#{i // size}"
        chunks.append(Chunk(cid, doc_id, part, {"doc_id": doc_id}))
    return chunks


def fake_embed(text: str, dim: int = 8) -> list[float]:
    h = hashlib.sha256(text.encode()).digest()
    return [h[i % len(h)] / 255.0 for i in range(dim)]


class SimpleRAG:
    def __init__(self, index: InMemoryVectorIndex):
        self.index = index

    def ingest(self, doc_id: str, text: str) -> int:
        count = 0
        for chunk in chunk_document(doc_id, text):
            self.index.upsert(chunk, fake_embed(chunk.text))
            count += 1
        return count

    def query(self, question: str, filters: dict | None = None) -> dict:
        hits = self.index.search(fake_embed(question), top_k=3, filters=filters)
        context = "\n".join(f"[{h.chunk_id}] {h.text}" for h in hits)
        answer = f"Based on sources: {context[:200]}..."
        return {"answer": answer, "sources": [h.chunk_id for h in hits]}


if __name__ == "__main__":
    rag = SimpleRAG(InMemoryVectorIndex())
    rag.ingest("policy-1", "Refunds process within 3 business days. Enterprise SLA is 99.9%.")
    print(rag.query("How long for refunds?"))
