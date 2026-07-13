"""File upload API for RAG document ingestion.

Run: uvicorn example-file-upload:app --reload
"""

from __future__ import annotations

import uuid
from pathlib import Path

from fastapi import FastAPI, File, HTTPException, UploadFile, status
from pydantic import BaseModel

app = FastAPI(title="File Upload Example")

UPLOAD_DIR = Path("/tmp/ai-uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

ALLOWED_TYPES = {"application/pdf", "text/plain", "text/markdown"}
MAX_SIZE_BYTES = 10 * 1024 * 1024  # 10 MB


class UploadResponse(BaseModel):
    document_id: str
    filename: str
    size_bytes: int
    status: str


@app.post("/v1/documents/upload", response_model=UploadResponse, status_code=status.HTTP_201_CREATED)
async def upload_document(file: UploadFile = File(...)):
    if file.content_type not in ALLOWED_TYPES:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported file type: {file.content_type}",
        )

    content = await file.read()
    if len(content) > MAX_SIZE_BYTES:
        raise HTTPException(status_code=413, detail="File too large")

    doc_id = str(uuid.uuid4())
    safe_name = Path(file.filename or "upload").name
    dest = UPLOAD_DIR / f"{doc_id}_{safe_name}"
    dest.write_bytes(content)

    # Production: enqueue background job for chunking + embedding
    return UploadResponse(
        document_id=doc_id,
        filename=safe_name,
        size_bytes=len(content),
        status="queued",
    )
