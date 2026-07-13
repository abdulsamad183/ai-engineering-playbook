# Vector Database Selection Cheat Sheet

> See [Vector Databases](../domains/rag/vector-databases.md) and [providers](../domains/rag/providers/).

| Scenario | Pick |
|----------|------|
| Prototype | Chroma |
| Already on Postgres | pgvector |
| Managed SaaS | Pinecone |
| Self-host production | Qdrant |
| Billion vectors | Milvus / FAISS+custom |
| Native hybrid BM25+vector | Weaviate |

**Check:** Metadata filters, ops burden, cost at your scale.
