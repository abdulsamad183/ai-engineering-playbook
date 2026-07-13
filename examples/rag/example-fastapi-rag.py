"""FastAPI RAG endpoint — query with tenant filter.

Run: uvicorn example-fastapi-rag:app --reload
"""

from __future__ import annotations

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="RAG API")


class QueryRequest(BaseModel):
    question: str = Field(min_length=1)
    tenant_id: str
    top_k: int = 5


class QueryResponse(BaseModel):
    answer: str
    sources: list[str]


# Inject real RAG service in production
async def rag_service_query(question: str, tenant_id: str, top_k: int) -> QueryResponse:
    return QueryResponse(
        answer=f"Demo answer for: {question}",
        sources=["chunk-demo-1"],
    )


@app.post("/v1/rag/query", response_model=QueryResponse)
async def query(req: QueryRequest) -> QueryResponse:
    try:
        return await rag_service_query(req.question, req.tenant_id, req.top_k)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e
