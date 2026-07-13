---
title: "Background Task Template"
description: "Background job pattern template for AI backends."
type: backend-template
---

# Background Task Template

## FastAPI BackgroundTasks (Fire-and-Forget)

```python
from fastapi import BackgroundTasks

@router.post("/documents")
async def upload_document(
    file: UploadFile,
    background_tasks: BackgroundTasks,
    service: DocumentService = Depends(get_document_service),
):
    doc = await service.save_metadata(file)
    background_tasks.add_task(service.process_document, doc.id)
    return {"id": doc.id, "status": "processing"}
```

## Durable Queue (ARQ / Celery)

```python
# workers/tasks.py
async def ingest_document(ctx, document_id: str) -> dict:
    """ARQ task: chunk, embed, and store document."""
    async with get_db_session() as session:
        doc = await document_repo.get_by_id(session, document_id)
        chunks = await chunker.split(doc.content)
        embeddings = await embedding_client.embed_batch([c.text for c in chunks])
        await vector_repo.upsert_batch(session, chunks, embeddings)
        await document_repo.mark_indexed(session, document_id)
    return {"document_id": document_id, "chunks": len(chunks)}


# Enqueue from service
await redis.enqueue_job("ingest_document", document_id)
```

## When to Use Which

| Pattern | Durability | Use Case |
|---------|-----------|----------|
| `BackgroundTasks` | None (lost on crash) | Email, cache invalidation |
| Redis queue (ARQ) | Survives restart | Document ingestion, embeddings |
| Celery | Full workflow | Complex multi-step pipelines |

## See Also

- [Background Processing for AI](../../../domains/backend-engineering/background-processing-for-ai.md)
