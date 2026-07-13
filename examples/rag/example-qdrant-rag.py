"""Qdrant RAG upsert and search pattern.

Requires: qdrant-client, running Qdrant at localhost:6333
Run: python example-qdrant-rag.py
"""

# See domains/rag/providers/qdrant.md for full guide

def demo():
    from qdrant_client import QdrantClient
    from qdrant_client.models import VectorParams, Distance, PointStruct

    client = QdrantClient(url="http://localhost:6333")
    name = "kb_demo"
    if not client.collection_exists(name):
        client.create_collection(
            collection_name=name,
            vectors_config=VectorParams(size=4, distance=Distance.COSINE),
        )
    client.upsert(
        collection_name=name,
        points=[PointStruct(id=1, vector=[0.1, 0.2, 0.3, 0.4], payload={"content": "Refund in 3 days"})],
    )
    print(client.search(collection_name=name, query_vector=[0.1, 0.2, 0.3, 0.4], limit=1))


if __name__ == "__main__":
    try:
        demo()
    except Exception as e:
        print("Start Qdrant or see providers/qdrant.md:", e)
