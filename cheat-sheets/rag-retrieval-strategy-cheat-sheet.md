# RAG Retrieval Strategy Cheat Sheet

> See [Retrieval Strategies](../domains/rag/retrieval-strategies.md).

| Corpus | Strategy |
|--------|----------|
| General KB | Hybrid (dense+BM25) → rerank |
| Exact IDs/codes | BM25-heavy hybrid |
| Long structured docs | Hierarchical + parent retrieval |
| Vague questions | Query rewrite + multi-query |
| Small corpus (<5K) | Dense only may suffice |

**Default:** Retrieve 50 → rerank 8 → compress to budget
