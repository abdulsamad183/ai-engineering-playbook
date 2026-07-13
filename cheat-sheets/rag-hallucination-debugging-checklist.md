# RAG Hallucination Debugging Checklist

1. [ ] Gold doc in retrieval top-K? (if no → retrieval)
2. [ ] Max similarity score above threshold?
3. [ ] Correct chunk text in assembled prompt?
4. [ ] Citations present and valid?
5. [ ] System prompt requires abstention?
6. [ ] Post-check: claim ⊆ source text?

See [Hallucination Prevention](../domains/rag/hallucination-prevention.md) · [RAG Mistakes](../domains/rag/rag-mistakes.md).
