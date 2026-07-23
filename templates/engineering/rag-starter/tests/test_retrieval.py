from rag.embeddings import EmbeddingProvider
from rag.prompt import build_rag_prompt
from rag.retrieval import Retriever
from rag.vector_store import VectorRecord, VectorStore


def test_vector_store_upsert_and_search_returns_results():
    store = VectorStore()
    store.upsert(
        [
            VectorRecord(id="1", text="alpha document", vector=[1.0, 0.0, 0.0], metadata={}),
            VectorRecord(id="2", text="beta document", vector=[0.0, 1.0, 0.0], metadata={}),
        ]
    )
    results = store.search([1.0, 0.0, 0.0], k=1)
    assert len(results) == 1
    assert results[0].id == "1"
    assert results[0].text == "alpha document"


def test_build_rag_prompt_includes_question():
    store = VectorStore()
    embedder = EmbeddingProvider()
    texts = ["Refunds take three business days.", "Shipping is free over fifty dollars."]
    vectors = embedder.embed(texts)
    store.upsert(
        [
            VectorRecord(id=str(i), text=t, vector=v, metadata={})
            for i, (t, v) in enumerate(zip(texts, vectors))
        ]
    )
    retriever = Retriever(store, embedder)
    question = "How long do refunds take?"
    prompt, docs = build_rag_prompt(question, retriever, top_n=2)
    assert question in prompt
    assert "Question:" in prompt
    assert len(docs) > 0
