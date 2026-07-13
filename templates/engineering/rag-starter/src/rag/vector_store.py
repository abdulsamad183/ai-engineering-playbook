"""In-memory vector store — swap for Pinecone, Qdrant, pgvector."""

from dataclasses import dataclass


@dataclass
class VectorRecord:
    id: str
    text: str
    vector: list[float]
    metadata: dict


class VectorStore:
    def __init__(self) -> None:
        self._records: list[VectorRecord] = []

    def upsert(self, records: list[VectorRecord]) -> None:
        self._records.extend(records)

    def search(self, query_vector: list[float], k: int = 5) -> list[VectorRecord]:
        def score(v: list[float]) -> float:
            return sum(a * b for a, b in zip(query_vector, v))

        return sorted(self._records, key=lambda r: score(r.vector), reverse=True)[:k]
