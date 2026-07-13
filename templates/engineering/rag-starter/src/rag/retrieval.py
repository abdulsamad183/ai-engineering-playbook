"""Retrieval + optional reranking."""

from rag.embeddings import EmbeddingProvider
from rag.vector_store import VectorStore


class Retriever:
    def __init__(self, store: VectorStore, embedder: EmbeddingProvider) -> None:
        self.store = store
        self.embedder = embedder

    def retrieve(self, query: str, k: int = 5) -> list[dict]:
        qv = self.embedder.embed([query])[0]
        hits = self.store.search(qv, k=k)
        return [{"id": h.id, "text": h.text, "metadata": h.metadata} for h in hits]


def rerank(query: str, docs: list[dict], top_n: int = 3) -> list[dict]:
    return sorted(docs, key=lambda d: len(set(query.split()) & set(d["text"].split())), reverse=True)[:top_n]
