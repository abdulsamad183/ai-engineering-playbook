---
title: "OpenAI"
description: "OpenAI API guide for AI engineering — models, chat completions, Responses API, embeddings, structured outputs, streaming, function calling, pricing, and production best practices."
domain: llm-engineering
tags: [openai, llm, api, streaming, production, intermediate]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - ../llm-streaming.md
  - ../vision-and-multimodal-models.md
  - anthropic-claude.md
  - google-gemini.md
keywords: [OpenAI, GPT-4, chat completions, Responses API, embeddings, function calling, structured outputs]
author: hp
---

# OpenAI

> Production guide to OpenAI APIs — model selection, chat completions, the Responses API, embeddings, structured outputs, streaming, function calling, pricing, and operational best practices.

## Table of Contents

- [Overview](#overview)
- [Use Cases](#use-cases)
- [Getting Started](#getting-started)
- [Models](#models)
- [Chat Completions API](#chat-completions-api)
- [Responses API](#responses-api)
- [Embeddings](#embeddings)
- [Structured Outputs](#structured-outputs)
- [Streaming](#streaming)
- [Function Calling](#function-calling)
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
| Provider | OpenAI |
| Access | REST API, official Python/JS SDKs |
| Models Supported | GPT-4.1, GPT-4o, o-series, embeddings, Whisper, DALL·E |
| API Style | OpenAI-compatible (widely cloned) |

OpenAI provides the most widely adopted LLM API surface.
Its chat completions format is the de facto standard that Groq, OpenRouter, Azure OpenAI, and Ollama emulate.

> **Production Standard:** Pin model versions in configuration, use the official async SDK, and abstract behind an `LLMClient` port — never scatter `openai` imports across route handlers.

---

## Use Cases

| Use Case | Fit | Notes |
|----------|-----|-------|
| General chat and copilots | High | GPT-4.1 / GPT-4o families |
| Structured data extraction | High | JSON schema / `response_format` |
| RAG answer generation | High | Pair with embedding models |
| Agent tool use | High | Function calling + Responses API |
| Vision / document AI | High | GPT-4o multimodal |
| Reasoning-heavy tasks | High | o3, o4-mini reasoning models |
| Local / air-gapped | Low | Use Ollama or Azure private endpoints |
| Cheapest bulk inference | Medium | gpt-4.1-nano, batch API |

---

## Getting Started

### Prerequisites

- OpenAI account and API key
- Python 3.11+ recommended
- `OPENAI_API_KEY` in environment (never commit)

### Quick Start

```python
import os

from openai import AsyncOpenAI

client = AsyncOpenAI(api_key=os.environ["OPENAI_API_KEY"])

response = await client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Summarize REST in one sentence."},
    ],
)
print(response.choices[0].message.content)
```

### SDK Installation

```bash
pip install openai>=1.40.0
```

Use `AsyncOpenAI` in FastAPI services — the sync client blocks the event loop.

---

## Models

### Chat and Reasoning (July 2026 landscape)

| Model | Strength | Context | Best For |
|-------|----------|---------|----------|
| `gpt-4.1` | Quality, instruction following | 1M (API) | Production chat, agents |
| `gpt-4.1-mini` | Cost/latency balance | 1M | Default production tier |
| `gpt-4.1-nano` | Lowest cost | 1M | Classification, routing |
| `gpt-4o` | Multimodal | 128k | Vision, audio experiments |
| `o4-mini` | Reasoning | 200k | Math, code, multi-step |
| `o3` | Deep reasoning | 200k | Hard problems, higher cost/latency |

Pin explicit model strings in config — aliases like `gpt-4o` may point to newer snapshots over time.

### Embedding Models

| Model | Dimensions | Notes |
|-------|------------|-------|
| `text-embedding-3-small` | 1536 (configurable) | Default for RAG |
| `text-embedding-3-large` | 3072 | Higher quality, higher cost |

### Audio and Image

| API | Model | Purpose |
|-----|-------|---------|
| Transcriptions | `whisper-1` | Speech-to-text |
| Image generation | `gpt-image-1` / DALL·E 3 | Image creation (separate from chat) |

---

## Chat Completions API

The workhorse endpoint: `POST /v1/chat/completions`.

```python
response = await client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {"role": "system", "content": "You classify support tickets."},
        {"role": "user", "content": "My invoice is wrong and I want a refund."},
    ],
    temperature=0.2,
    max_tokens=256,
)
content = response.choices[0].message.content
usage = response.usage  # prompt_tokens, completion_tokens, total_tokens
```

### Key Parameters

| Parameter | Purpose |
|-----------|---------|
| `temperature` | Randomness (0–2); use 0–0.3 for extraction |
| `max_tokens` | Cap output length |
| `top_p` | Nucleus sampling alternative to temperature |
| `stop` | Stop sequences |
| `response_format` | JSON mode or JSON schema |
| `tools` | Function definitions for tool calling |
| `tool_choice` | `auto`, `required`, or specific function |

### Message Roles

| Role | Usage |
|------|-------|
| `system` | Instructions and policy |
| `user` | End-user input |
| `assistant` | Prior model turns |
| `tool` | Function results (tool calling loop) |

---

## Responses API

The Responses API (`client.responses.create`) is OpenAI's newer unified interface for agents, tools, and multimodal inputs.

```python
response = await client.responses.create(
    model="gpt-4.1-mini",
    input="What is the weather in Paris?",
    tools=[
        {
            "type": "function",
            "name": "get_weather",
            "description": "Get weather for a city",
            "parameters": {
                "type": "object",
                "properties": {"city": {"type": "string"}},
                "required": ["city"],
            },
        }
    ],
)
```

### Chat Completions vs Responses

| | Chat Completions | Responses API |
|--|------------------|---------------|
| Maturity | Universal, stable | Newer, agent-focused |
| Tool loop | Manual message assembly | Built-in tool orchestration |
| Ecosystem | All proxies support | OpenAI-native |
| Migration | Keep for simple chat | Prefer for new agent features |

For greenfield agent systems on OpenAI only, evaluate Responses first.
For provider-agnostic code, wrap both behind your `LLMClient` interface.

---

## Embeddings

```python
response = await client.embeddings.create(
    model="text-embedding-3-small",
    input=["First document chunk.", "Second chunk."],
)
vectors = [item.embedding for item in response.data]
```

### Best Practices

- Batch up to hundreds of chunks per request (watch payload size)
- Cache embeddings by content hash at ingestion
- Use `dimensions` parameter to reduce storage if your vector DB supports it
- Normalize vectors if your similarity metric expects it (cosine on OpenAI embeddings works without manual normalization)

---

## Structured Outputs

Force JSON matching a schema — preferred over "return JSON" in the prompt.

```python
from pydantic import BaseModel


class TicketClassification(BaseModel):
    category: str
    urgency: str
    summary: str


response = await client.beta.chat.completions.parse(
    model="gpt-4.1-mini",
    messages=[{"role": "user", "content": user_message}],
    response_format=TicketClassification,
)
parsed: TicketClassification = response.choices[0].message.parsed
```

### JSON Schema Mode

```python
response = await client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=messages,
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "ticket",
            "schema": TicketClassification.model_json_schema(),
            "strict": True,
        },
    },
)
```

Validate with Pydantic after parsing — never trust raw JSON in production without validation.

---

## Streaming

```python
stream = await client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=messages,
    stream=True,
    stream_options={"include_usage": True},
)
async for chunk in stream:
    if chunk.choices and chunk.choices[0].delta.content:
        yield chunk.choices[0].delta.content
    if chunk.usage:
        log_usage(chunk.usage)
```

See [LLM Streaming](../llm-streaming.md) for SSE and FastAPI patterns.

---

## Function Calling

### Define Tools

```python
tools = [
    {
        "type": "function",
        "function": {
            "name": "search_docs",
            "description": "Search internal documentation",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string"},
                    "limit": {"type": "integer", "default": 5},
                },
                "required": ["query"],
            },
        },
    }
]
```

### Tool Loop

```python
messages = [{"role": "user", "content": "Find our refund policy."}]
response = await client.chat.completions.create(
    model="gpt-4.1-mini", messages=messages, tools=tools, tool_choice="auto"
)
msg = response.choices[0].message
if msg.tool_calls:
    messages.append(msg)
    for call in msg.tool_calls:
        result = await execute_tool(call.function.name, call.function.arguments)
        messages.append({
            "role": "tool",
            "tool_call_id": call.id,
            "content": result,
        })
    response = await client.chat.completions.create(
        model="gpt-4.1-mini", messages=messages, tools=tools
    )
```

Cap tool loop iterations (e.g., 5) to prevent runaway agent costs.

---

## Integration Patterns

1. **Port/adapter** — `OpenAIClient` implements `LLMClient`; swap for Anthropic in tests
2. **Retry with backoff** — retry 429/5xx with exponential backoff and jitter
3. **Fallback model** — `gpt-4.1-mini` → `gpt-4.1-nano` on rate limit
4. **Batch API** — 50% discount for non-urgent offline jobs (24h window)
5. **Azure OpenAI** — same SDK with `AzureOpenAI` client for enterprise compliance

---

## API Reference Summary

| Endpoint / Method | Purpose | Key Parameters |
|-------------------|---------|----------------|
| `POST /v1/chat/completions` | Text chat | `model`, `messages`, `stream` |
| `POST /v1/responses` | Agent / unified | `input`, `tools` |
| `POST /v1/embeddings` | Vector embeddings | `model`, `input` |
| `POST /v1/audio/transcriptions` | Speech-to-text | `file`, `model` |
| `POST /v1/images/generations` | Image creation | `prompt`, `model` |
| `POST /v1/files` | Upload for reuse | `file`, `purpose` |

> Full API documentation: [OpenAI API Reference](https://platform.openai.com/docs/api-reference)

---

## Pricing and Limits

Pricing changes frequently — verify at [openai.com/pricing](https://openai.com/pricing).

| Tier | Cost (indicative) | Rate Limits | Notes |
|------|-------------------|-------------|-------|
| Pay-as-you-go | Per-token model pricing | Tier-based RPM/TPM | Increases with usage tier |
| Batch API | ~50% discount | Separate limits | Async 24h completion |
| Enterprise | Custom | Higher limits | Azure / private contract |

### Cost Optimization

- Use `gpt-4.1-nano` for routing and classification
- Cache system prompts with prompt caching (where available) or application-level cache
- Set `max_tokens` aggressively for short outputs
- Log `usage` on every request for chargeback dashboards

---

## Production Usage

> **Production Standard:** API keys from environment, retries on transient errors, timeouts on every call, usage logging, and no PII in application logs.

### Authentication

```python
# Good — settings via Pydantic BaseSettings
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    openai_api_key: str
    openai_default_model: str = "gpt-4.1-mini"
```

### Retry Strategy

```python
from tenacity import retry, stop_after_attempt, wait_exponential_jitter

@retry(stop=stop_after_attempt(3), wait=wait_exponential_jitter(initial=1, max=30))
async def complete_with_retry(client, **kwargs):
    return await client.chat.completions.create(**kwargs)
```

### Error Handling

| Status | Meaning | Action |
|--------|---------|--------|
| 400 | Bad request | Fix payload, do not retry |
| 401 | Invalid key | Alert ops |
| 429 | Rate limit | Backoff, optionally fallback model |
| 500/503 | Server error | Retry with limit |

### Observability

Log: `model`, `latency_ms`, `input_tokens`, `output_tokens`, `request_id`, `finish_reason`.
Use OpenAI's `x-request-id` header for support tickets.

---

## Limitations

- Data residency: US-centric unless using Azure OpenAI in target region
- Rate limits vary by account tier — plan for 429s at scale
- Reasoning models (o-series) have higher latency and cost
- Function calling can loop indefinitely without caps
- Model behavior changes when OpenAI updates snapshots behind aliases
- No true on-prem offering — compliance via Azure or enterprise agreements

---

## Alternatives

| Tool | Strengths | Weaknesses |
|------|-----------|------------|
| Anthropic Claude | Long context, document quality | Different API surface |
| Google Gemini | Multimodal, competitive pricing | Different SDK |
| Groq | Ultra-low latency | Limited model set |
| OpenRouter | Multi-provider routing | Extra dependency |
| Ollama | Local, private | Hardware requirements |

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Hardcoded API key | Environment variables + secrets manager |
| No `max_tokens` | Set output cap per endpoint |
| Ignoring `usage` | Log tokens for every call |
| Sync client in async app | `AsyncOpenAI` |
| Unbounded tool loops | Max iterations + timeout |
| Parsing JSON without schema | Structured outputs + Pydantic |

---

## Navigation

### Prerequisites

- [LLM Streaming](../llm-streaming.md)

### Related Topics

- [Anthropic Claude](anthropic-claude.md)
- [Google Gemini](google-gemini.md)
- [OpenRouter](openrouter.md)

---

## See Also

- [Vision and Multimodal Models](../vision-and-multimodal-models.md)
- [Software Engineering for AI](../../foundations/software-engineering-for-ai.md)

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Initial version |
