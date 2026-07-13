"""Phoenix-style RAG span logging (conceptual).

Run: python example-phoenix-integration.py
"""

from dataclasses import dataclass, field


@dataclass
class RagTrace:
    query: str
    retrieved_chunks: list[dict] = field(default_factory=list)
    answer: str = ""

    def add_chunk(self, doc_id: str, score: float, text: str) -> None:
        self.retrieved_chunks.append({"doc_id": doc_id, "score": score, "text_preview": text[:80]})

    def to_export(self) -> dict:
        return {
            "query": self.query,
            "num_chunks": len(self.retrieved_chunks),
            "chunks": self.retrieved_chunks,
            "answer_preview": self.answer[:200],
        }


def main() -> None:
    t = RagTrace(query="refund policy")
    t.add_chunk("policy-1", 0.92, "Refunds within 30 days with receipt")
    t.answer = "You can request a refund within 30 days."
    print(t.to_export())


if __name__ == "__main__":
    main()
