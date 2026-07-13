# Embedding Model Selection Cheat Sheet

> See [Embeddings for RAG](../domains/rag/embeddings-for-rag.md).

| Need | Model direction |
|------|-----------------|
| Fast MVP | OpenAI text-embedding-3-small |
| Best quality (API) | text-embedding-3-large / Voyage-3 |
| On-prem | BGE-M3, E5-mistral |
| Multilingual | Cohere embed-multilingual, multilingual-e5 |
| Code | Voyage-code, code-specific fine-tunes |

**Rules:** Same model index+query · Version in metadata · Full reindex on change
