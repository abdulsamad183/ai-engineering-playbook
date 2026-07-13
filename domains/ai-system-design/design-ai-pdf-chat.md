---
title: "Design: AI PDF Chat"
description: "PDF chat — ingestion, OCR, chunking, tables, images, citations, long documents."
domain: ai-system-design
tags: [system-design, pdf, document-chat, ocr, phase-11]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - ../rag/document-ingestion-pipeline.md
  - ../rag/chunking.md
keywords: [PDF chat, OCR, table extraction]
author: hp
---

# Design: AI PDF Chat

## Problem Statement

Chat with uploaded PDFs including scanned docs, tables, and 500+ page files.

## Architecture

```mermaid
flowchart LR
    UP[Upload] --> S3[Object storage]
    S3 --> PARSE[Parse pipeline]
    PARSE --> OCR[OCR if scanned]
    PARSE --> CHUNK[Chunk + metadata]
    CHUNK --> VDB[(Vector index)]
    Q[Question] --> RET[Retrieve]
    RET --> GEN[Generate + cite page]
```

## Components

- **PDF ingestion** — PyMuPDF, unstructured.io
- **OCR** — Tesseract / cloud OCR for scans
- **Tables** — extract as markdown/CSV chunks
- **Images** — caption via vision model; separate index
- **Citations** — page + bounding box in metadata
- **Long docs** — hierarchical summarize + retrieve

## Tradeoffs

| Page-level chunks | Semantic chunks |
|-------------------|-------------------|
| Precise cites | Better semantics |

## Navigation

- [Email Assistant](design-ai-email-assistant.md)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Phase 11 Section 11 |
