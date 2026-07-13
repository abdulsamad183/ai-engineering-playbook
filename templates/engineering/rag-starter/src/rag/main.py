from rag.embeddings import EmbeddingProvider
from rag.pipeline import index_corpus
from rag.prompt import build_rag_prompt
from rag.retrieval import Retriever
from rag.vector_store import VectorStore


def main() -> None:
    store = VectorStore()
    embedder = EmbeddingProvider()
    index_corpus("data", store, embedder)
    retriever = Retriever(store, embedder)
    prompt, citations = build_rag_prompt("What is RAG?", retriever)
    print(prompt)
    print("Citations:", citations)


if __name__ == "__main__":
    main()
