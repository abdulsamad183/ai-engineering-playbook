"""RAG evaluation — retrieval + generation metrics.

Run: python example-rag-evaluation.py
"""


def retrieval_recall_at_k(retrieved: list[str], gold: set[str], k: int) -> float:
    if not gold:
        return 1.0
    return len(set(retrieved[:k]) & gold) / len(gold)


def context_precision(retrieved: list[str], relevant: set[str]) -> float:
    if not retrieved:
        return 0.0
    return sum(1 for r in retrieved if r in relevant) / len(retrieved)


def main() -> None:
    retrieved = ["doc1", "doc3", "doc2"]
    gold = {"doc1", "doc2"}
    print("recall@2:", retrieval_recall_at_k(retrieved, gold, k=2))
    print("context_precision:", context_precision(retrieved, gold))


if __name__ == "__main__":
    main()
