# RAG Performance Optimization Checklist

- [ ] Batch embeddings at ingest
- [ ] Cache query embeddings + retrieval (versioned key)
- [ ] Prompt-cache stable system prefix
- [ ] Reduce top_k before LLM (rerank narrows)
- [ ] Parallel ingest workers
- [ ] Right-size ANN ef_search (recall vs latency)
- [ ] Async ingest; don't block query path

See [Production RAG](../domains/rag/production-rag.md).
