# RAG Reranking Checklist

- [ ] Retrieve 30–50 candidates (not 5)
- [ ] Cross-encoder or API reranker configured
- [ ] Pass top 5–10 to LLM after rerank
- [ ] Measure NDCG@10 before/after rerank
- [ ] Latency budget includes rerank (100–500ms)
- [ ] Cache rerank for identical query+index version (optional)

See [Reranking](../domains/rag/reranking.md).
