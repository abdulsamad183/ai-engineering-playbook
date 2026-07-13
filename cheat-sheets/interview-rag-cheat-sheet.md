# Interview RAG Cheat Sheet

```
Ingest → Chunk → Embed → Index
Query → Retrieve → (Rerank) → Generate → Cite
```
- Hybrid: BM25 + vector
- Rerank top-50 only
- Faithfulness ≠ retrieval score
- ACL filter at retrieval
- Eval: context precision, faithfulness

See [RAG Interviews](../domains/interview-preparation/rag-interviews.md).
