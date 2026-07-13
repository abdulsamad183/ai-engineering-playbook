# RAG Production Deployment Checklist

- [ ] Blue/green index versions
- [ ] Incremental ingest + checksum dedup
- [ ] Tenant ACL on every query
- [ ] Context trace logging (chunk IDs, scores)
- [ ] Alerts: empty retrieval, latency p95, ingest DLQ
- [ ] Embedding model version in metadata
- [ ] Disaster recovery snapshots

See [Production RAG](../domains/rag/production-rag.md).
