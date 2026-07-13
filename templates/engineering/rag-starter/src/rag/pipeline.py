from rag.chunking import chunk_text
from rag.embeddings import EmbeddingProvider
from rag.ingestion import load_documents
from rag.vector_store import VectorRecord, VectorStore


def index_corpus(data_path: str, store: VectorStore, embedder: EmbeddingProvider) -> int:
    count = 0
    for doc in load_documents(data_path):
        for i, chunk in enumerate(chunk_text(doc["text"])):
            vec = embedder.embed([chunk])[0]
            store.upsert(
                [VectorRecord(id=f"{doc['id']}:{i}", text=chunk, vector=vec, metadata={"source": doc["source"]})]
            )
            count += 1
    return count
