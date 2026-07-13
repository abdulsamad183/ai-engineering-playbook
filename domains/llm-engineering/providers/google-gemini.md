---
title: "Google Gemini"
description: "Google Gemini API guide — models, multimodal inputs, long context, embeddings, streaming, function calling, pricing, and production integration patterns."
domain: llm-engineering
tags: [llm, api, streaming, production, intermediate]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - ../vision-and-multimodal-models.md
  - ../llm-streaming.md
  - openai.md
  - anthropic-claude.md
keywords: [Gemini, Google AI, multimodal, long context, Vertex AI, function calling]
author: hp
---

# Google Gemini

> Production guide to Google's Gemini models — multimodal capabilities, long context windows, API integration via Google AI Studio and Vertex AI, and engineering best practices.

## Table of Contents

- [Overview](#overview)
- [Use Cases](#use-cases)
- [Getting Started](#getting-started)
- [Models](#models)
- [Core Features](#core-features)
- [Multimodal Inputs](#multimodal-inputs)
- [Streaming](#streaming)
- [Function Calling](#function-calling)
- [Embeddings](#embeddings)
- [Integration Patterns](#integration-patterns)
- [API Reference Summary](#api-reference-summary)
- [Pricing and Limits](#pricing-and-limits)
- [Production Usage](#production-usage)
- [Limitations](#limitations)
- [Alternatives](#alternatives)
- [Common Mistakes](#common-mistakes)
- [Navigation](#navigation)

---

## Overview

| Attribute | Value |
|-----------|-------|
| Category | LLM Provider |
| Provider | Google DeepMind / Google Cloud |
| Access | Google AI Studio API, Vertex AI |
| Models Supported | Gemini 2.x Pro, Flash, Flash-Lite |
| Differentiator | Native multimodal (text, image, audio, video), long context |

Gemini is Google's flagship multimodal LLM family, available through a developer API (Google AI Studio) and enterprise Vertex AI on GCP.
It competes on context length, native video/audio understanding, and price-performance on Flash tiers.

> **Production Standard:** Choose Google AI Studio for prototypes; migrate to Vertex AI for enterprise IAM, VPC, and data governance.

---

## Use Cases

| Use Case | Fit | Notes |
|----------|-----|-------|
| Multimodal document AI | High | PDF, image, video native support |
| Long-context analysis | High | 1M+ tokens on select models |
| Cost-sensitive chat | High | Gemini Flash tiers |
| GCP-native applications | High | Vertex AI integration |
| OpenAI-compatible proxies | Medium | Some gateways map Gemini |
| Lowest-latency inference | Medium | Groq may win on specific models |
| Air-gapped deployment | Low | Cloud-only (Vertex private endpoints possible) |

---

## Getting Started

### Prerequisites

- Google account (AI Studio) or GCP project (Vertex AI)
- API key (AI Studio) or service account (Vertex)
- `google-genai` Python SDK

### Quick Start (Google AI Studio)

```bash
pip install google-genai
```

```python
import os

from google import genai

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain vector databases in two sentences.",
)
print(response.text)
```

### Vertex AI

```python
from google import genai

client = genai.Client(
    vertexai=True,
    project="my-gcp-project",
    location="us-central1",
)
```

Vertex uses IAM — no API key in application code.

---

## Models

| Model | Strength | Context | Best For |
|-------|----------|---------|----------|
| `gemini-2.5-pro` | Quality, reasoning | 1M+ | Complex analysis, coding |
| `gemini-2.5-flash` | Speed + cost | 1M+ | Default production tier |
| `gemini-2.5-flash-lite` | Lowest cost | 1M+ | Classification, routing |
| `gemini-2.0-flash` | Previous gen | 1M | Legacy deployments |

Verify current model IDs in [Google AI documentation](https://ai.google.dev/gemini-api/docs/models) — names evolve with releases.

---

## Core Features

### Generate Content

```python
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[
        {"role": "user", "parts": [{"text": "Summarize this meeting transcript."}]},
    ],
    config={
        "temperature": 0.3,
        "max_output_tokens": 1024,
        "response_mime_type": "application/json",
        "response_schema": MeetingSummary,
    },
)
```

### System Instructions

```python
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Classify this ticket.",
    config={"system_instruction": "You are a support triage bot. Output JSON only."},
)
```

### JSON / Schema Output

Gemini supports `response_mime_type` and Pydantic-compatible schemas — similar to OpenAI structured outputs.

---

## Multimodal Inputs

Gemini's primary strength is native multimodal understanding.

### Image

```python
from google.genai import types

with open("invoice.jpg", "rb") as f:
    image_bytes = f.read()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[
        types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg"),
        "Extract line items as JSON.",
    ],
)
```

### PDF and Video

Upload via File API for large assets:

```python
uploaded = client.files.upload(file="contract.pdf")
response = client.models.generate_content(
    model="gemini-2.5-pro",
    contents=[uploaded, "List all termination clauses."],
)
```

See [Vision and Multimodal Models](../vision-and-multimodal-models.md) for pipeline patterns.

### Audio

```python
uploaded = client.files.upload(file="meeting.mp3")
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[uploaded, "Provide action items with owners."],
)
```

---

## Streaming

```python
for chunk in client.models.generate_content_stream(
    model="gemini-2.5-flash",
    contents="Write a haiku about distributed systems.",
):
    if chunk.text:
        print(chunk.text, end="", flush=True)
```

Async streaming is available in the async client variant — use in FastAPI services.

Normalize Gemini chunks in your LLM adapter to match your internal streaming interface.
See [LLM Streaming](../llm-streaming.md).

---

## Function Calling

```python
schedule_meeting = {
    "name": "schedule_meeting",
    "description": "Schedule a calendar meeting",
    "parameters": {
        "type": "object",
        "properties": {
            "title": {"type": "string"},
            "datetime": {"type": "string"},
        },
        "required": ["title", "datetime"],
    },
}

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Schedule a sync tomorrow at 2pm called Sprint Planning.",
    config={"tools": [schedule_meeting]},
)
```

Process `function_call` parts in the response, execute locally, and send `function_response` in a follow-up turn.

---

## Embeddings

```python
result = client.models.embed_content(
    model="text-embedding-004",
    contents=["Chunk one.", "Chunk two."],
)
embeddings = [e.values for e in result.embeddings]
```

Use for RAG pipelines on GCP alongside Vertex Vector Search or third-party vector DBs.

---

## Integration Patterns

1. **Vertex for production** — IAM, audit logs, VPC-SC, CMEK encryption
2. **AI Studio for dev** — fast iteration with API key
3. **GCS → Gemini** — store uploads in GCS, pass `gs://` URIs on Vertex
4. **Multimodal RAG** — embed text chunks, attach page images at query time
5. **Model router** — Flash for triage, Pro for complex escalation

---

## API Reference Summary

| Endpoint / Method | Purpose | Key Parameters |
|-------------------|---------|----------------|
| `models.generate_content` | Chat / completion | `model`, `contents`, `config` |
| `models.generate_content_stream` | Streaming | Same as above |
| `models.embed_content` | Embeddings | `model`, `contents` |
| `files.upload` | Media upload | `file`, mime type |
| `models.count_tokens` | Token budgeting | `model`, `contents` |

> Full documentation: [Google AI Gemini API](https://ai.google.dev/gemini-api/docs)

---

## Pricing and Limits

| Tier | Cost | Rate Limits | Notes |
|------|------|-------------|-------|
| AI Studio free | Limited free quota | RPM caps | Development only |
| Pay-as-you-go | Per-token pricing | Tier-based | Flash is cost-competitive |
| Vertex AI | GCP billing | Quota per project | Enterprise features |

Use `count_tokens` before sending large multimodal payloads to avoid bill shock.

---

## Production Usage

> **Production Standard:** Use Vertex AI in production GCP deployments; enforce quotas; scan uploads; log token counts.

### Authentication

| Environment | Method |
|-------------|--------|
| Local dev | `GEMINI_API_KEY` |
| GCE / GKE / Cloud Run | Workload identity → Vertex |
| CI | Service account key in secrets manager (rotate regularly) |

### Safety Settings

```python
from google.genai import types

config = types.GenerateContentConfig(
    safety_settings=[
        types.SafetySetting(
            category="HARM_CATEGORY_HATE_SPEECH",
            threshold="BLOCK_MEDIUM_AND_ABOVE",
        ),
    ]
)
```

Tune thresholds per product — over-blocking frustrates users; under-blocking creates risk.

### Error Handling

| Error | Action |
|-------|--------|
| 429 RESOURCE_EXHAUSTED | Backoff, request quota increase |
| SAFETY block | Return user-friendly message, log category |
| Invalid argument | Fix payload, check mime types |

### Observability

Log: `model`, `input_tokens`, `output_tokens`, `latency_ms`, `safety_block`, `file_count`.

---

## Limitations

- API surface differs from OpenAI — adapter layer required for multi-provider apps
- File uploads expire — re-upload or refresh for long-running workflows
- Free tier not suitable for production traffic
- Model availability varies by region on Vertex
- Very long context requests have higher latency and cost
- Safety filters may block legitimate content in sensitive domains

---

## Alternatives

| Tool | Strengths | Weaknesses |
|------|-----------|------------|
| OpenAI GPT-4.1 | Ecosystem, tool maturity | Shorter context on some tiers |
| Anthropic Claude | Document quality | No native video |
| Groq | Speed | Fewer models |
| Vertex PaLM (legacy) | GCP | Deprecated — migrate to Gemini |

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| AI Studio key in production | Vertex AI + workload identity |
| Sending huge videos inline | File API + duration limits |
| Ignoring safety blocks | Handle `prompt_feedback` in responses |
| No token counting | `count_tokens` before large calls |
| OpenAI SDK assumptions | Use `google-genai` native types |

---

## Navigation

### Prerequisites

- [Vision and Multimodal Models](../vision-and-multimodal-models.md)

### Related Topics

- [OpenAI](openai.md)
- [Anthropic Claude](anthropic-claude.md)

---

## See Also

- [LLM Streaming](../llm-streaming.md)
- [File Handling for AI](../../backend-engineering/file-handling-for-ai.md)

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Initial version |
