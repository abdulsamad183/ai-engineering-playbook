---
title: "Anthropic Claude"
description: "Anthropic Claude API guide — models, Messages API, tool use, long context, prompt caching, streaming, pricing, and production best practices."
domain: llm-engineering
tags: [anthropic, llm, api, streaming, production, intermediate]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - ../llm-streaming.md
  - ../vision-and-multimodal-models.md
  - openai.md
  - google-gemini.md
keywords: [Claude, Anthropic, tool use, prompt caching, long context, Messages API]
author: hp
---

# Anthropic Claude

> Production guide to Anthropic's Claude models — Messages API, tool use, 200k+ context, prompt caching for cost reduction, vision, streaming, and operational patterns.

## Table of Contents

- [Overview](#overview)
- [Use Cases](#use-cases)
- [Getting Started](#getting-started)
- [Models](#models)
- [Messages API](#messages-api)
- [Tool Use](#tool-use)
- [Long Context](#long-context)
- [Prompt Caching](#prompt-caching)
- [Vision](#vision)
- [Streaming](#streaming)
- [Structured Outputs](#structured-outputs)
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
| Provider | Anthropic |
| Access | REST API, Python/TS SDK |
| Models Supported | Claude Opus, Sonnet, Haiku (4.x family) |
| Differentiators | Long context, document quality, prompt caching, tool use |

Claude is Anthropic's LLM family, accessed via the **Messages API**.
It excels at long-document analysis, nuanced instruction following, and agentic tool use with strong safety defaults.

> **Production Standard:** Use prompt caching for stable system prompts and RAG context prefixes. Cap tool-use loops and log cache hit metrics.

---

## Use Cases

| Use Case | Fit | Notes |
|----------|-----|-------|
| Long document analysis | High | 200k context standard |
| Code generation and review | High | Sonnet/Opus strong |
| Agent tool use | High | Native tool_use blocks |
| Customer support | High | Haiku for speed, Sonnet for quality |
| Vision / PDF (via images) | High | Page rasterization pattern |
| Cheapest high-volume | Medium | Haiku tier |
| Native video | Low | Frame extraction required |
| OpenAI-compatible drop-in | Low | Adapter needed |

---

## Getting Started

### Prerequisites

- Anthropic API key from Console
- `ANTHROPIC_API_KEY` environment variable

### Quick Start

```bash
pip install anthropic>=0.40.0
```

```python
import os

import anthropic

client = anthropic.AsyncAnthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

message = await client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    system="You are a concise technical writer.",
    messages=[{"role": "user", "content": "Explain CQRS in three bullets."}],
)
print(message.content[0].text)
```

---

## Models

| Model | Strength | Context | Best For |
|-------|----------|---------|----------|
| `claude-opus-4-20250514` | Highest capability | 200k | Hard reasoning, critical tasks |
| `claude-sonnet-4-20250514` | Balance | 200k | Default production |
| `claude-3-5-haiku-20241022` | Speed, cost | 200k | Classification, routing |

Pin dated model IDs — Anthropic releases new snapshots with suffix dates.

### Model Selection Guide

```text
Router (Haiku) → simple FAQ, classification
Sonnet → chat, RAG, most agents
Opus → complex analysis, high-stakes generation (use sparingly)
```

---

## Messages API

Unlike OpenAI's chat completions, Claude uses a dedicated Messages API.

```python
response = await client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=2048,
    system="You extract structured data from support tickets.",
    messages=[
        {"role": "user", "content": "I was charged twice for order #8821."},
    ],
    temperature=0.2,
)
text = response.content[0].text
usage = response.usage  # input_tokens, output_tokens
```

### Key Differences from OpenAI

| Concept | OpenAI | Anthropic |
|---------|--------|-----------|
| System prompt | `messages` role `system` | Top-level `system` parameter |
| Content | String or parts array | String or content blocks |
| Stop reason | `finish_reason` | `stop_reason` |
| Max output | `max_tokens` | `max_tokens` (required) |

`max_tokens` is **required** — always set it explicitly.

---

## Tool Use

Claude's tool use (function calling equivalent) returns `tool_use` content blocks.

### Define Tools

```python
tools = [
    {
        "name": "get_order_status",
        "description": "Look up order status by order ID",
        "input_schema": {
            "type": "object",
            "properties": {
                "order_id": {"type": "string", "description": "Order ID"},
            },
            "required": ["order_id"],
        },
    }
]
```

### Tool Loop

```python
messages = [{"role": "user", "content": "Where is order #8821?"}]
response = await client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    tools=tools,
    messages=messages,
)

while response.stop_reason == "tool_use":
    messages.append({"role": "assistant", "content": response.content})
    tool_results = []
    for block in response.content:
        if block.type == "tool_use":
            result = await execute_tool(block.name, block.input)
            tool_results.append({
                "type": "tool_result",
                "tool_use_id": block.id,
                "content": result,
            })
    messages.append({"role": "user", "content": tool_results})
    response = await client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1024,
        tools=tools,
        messages=messages,
    )
```

### Tool Choice

| Value | Behavior |
|-------|----------|
| `auto` | Model decides (default) |
| `any` | Must use a tool |
| `tool` + `name` | Force specific tool |

Cap iterations at 5–10 to control cost.

---

## Long Context

Claude supports 200k tokens (and beta extended context on select models).

### Context Budgeting

```python
# Use token counting API before sending
count = await client.messages.count_tokens(
    model="claude-sonnet-4-20250514",
    system=system_prompt,
    messages=messages,
)
if count.input_tokens > 180_000:
    messages = truncate_or_summarize(messages)
```

### RAG with Long Context

For corpora that fit in context, Claude can ingest full documents — reducing retrieval complexity.
For larger corpora, combine retrieval (top-k chunks) with long-context synthesis.

| Strategy | When |
|----------|------|
| Full-doc in context | < 150k tokens total |
| RAG + synthesis | Larger knowledge bases |
| Hierarchical | Summarize sections, then merge |

---

## Prompt Caching

Prompt caching reduces cost and latency for repeated prefix content (system prompts, tool definitions, RAG context).

### How It Works

Mark cacheable blocks with `cache_control`:

```python
response = await client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    system=[
        {
            "type": "text",
            "text": LONG_SYSTEM_PROMPT,
            "cache_control": {"type": "ephemeral"},
        }
    ],
    messages=[{"role": "user", "content": "Summarize the policy section on refunds."}],
)
```

### Cache Economics

| Metric | Effect |
|--------|--------|
| Cache write | Higher cost on first request (creates cache) |
| Cache read | ~90% discount on cached input tokens |
| TTL | Ephemeral cache (~5 min default) — design for burst traffic |

### What to Cache

- Stable system instructions
- Tool definitions (unchanging across requests)
- Large RAG context prefixes when the same document set is queried repeatedly
- Few-shot examples

### What Not to Cache

- Per-user PII in system prompts
- Rapidly changing content
- Unique one-off queries

Monitor `usage.cache_creation_input_tokens` and `usage.cache_read_input_tokens` in responses.

---

## Vision

```python
import base64

image_data = base64.standard_b64encode(image_bytes).decode()

response = await client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": "image/jpeg",
                        "data": image_data,
                    },
                },
                {"type": "text", "text": "Extract the table as CSV."},
            ],
        }
    ],
)
```

For PDFs, rasterize pages — see [Vision and Multimodal Models](../vision-and-multimodal-models.md).

---

## Streaming

```python
async with client.messages.stream(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    messages=messages,
) as stream:
    async for text in stream.text_stream:
        yield text
```

Event types include `content_block_delta`, `message_stop`.
Normalize in your adapter for SSE — see [LLM Streaming](../llm-streaming.md).

---

## Structured Outputs

Use tool use with a single forced tool as a structured extraction pattern:

```python
extract_tool = {
    "name": "extract_invoice",
    "description": "Extract invoice fields",
    "input_schema": InvoiceSchema.model_json_schema(),
}

response = await client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    tools=[extract_tool],
    tool_choice={"type": "tool", "name": "extract_invoice"},
    messages=[{"role": "user", "content": ocr_text}],
)
```

Alternatively, prompt for JSON and validate with Pydantic — less reliable than schema-constrained tool use.

---

## Integration Patterns

1. **Cache-aware RAG** — cache document prefix, vary only the user question
2. **Haiku router → Sonnet worker** — cheap classification, expensive generation
3. **Tool use agents** — cap loops, timeout per tool execution
4. **Multi-provider fallback** — Claude secondary when OpenAI 503
5. **Bedrock deployment** — AWS-hosted Claude for enterprise compliance

---

## API Reference Summary

| Endpoint / Method | Purpose | Key Parameters |
|-------------------|---------|----------------|
| `POST /v1/messages` | Chat completion | `model`, `messages`, `max_tokens` |
| `POST /v1/messages` (stream) | Streaming | `stream=True` |
| Token counting | Budget check | `messages`, `system` |
| Batches API | Async bulk | 50% discount, 24h window |

> Full documentation: [Anthropic API Reference](https://docs.anthropic.com/en/api/messages)

---

## Pricing and Limits

| Tier | Cost | Rate Limits | Notes |
|------|------|-------------|-------|
| Standard | Per-token (model-dependent) | RPM/TPM tiers | Increases with spend |
| Prompt caching | Cache read discounted | — | Requires `cache_control` |
| Batches | ~50% discount | Separate | Non-real-time |

Opus > Sonnet > Haiku in per-token cost.
Cache reads dramatically change unit economics for RAG.

---

## Production Usage

> **Production Standard:** Required `max_tokens`, prompt caching for stable prefixes, tool loop caps, async SDK, usage logging including cache metrics.

### Error Handling

| Error | Action |
|-------|--------|
| 429 | Exponential backoff |
| 529 overloaded | Retry, fallback provider |
| `max_tokens` exceeded | Increase limit or summarize output |

### Safety

Claude has built-in refusals — handle gracefully in UX.
Do not attempt to bypass safety for user-facing products.

### Observability

```python
usage = response.usage
log.info(
    "claude_call",
    model=model,
    input_tokens=usage.input_tokens,
    output_tokens=usage.output_tokens,
    cache_read=usage.cache_read_input_tokens,
    cache_create=usage.cache_creation_input_tokens,
)
```

---

## Limitations

- No native OpenAI SDK compatibility without adapter
- Video requires frame extraction
- Extended context beta may have separate pricing
- Rate limits require tier planning at scale
- `max_tokens` must be set — omitting causes API errors
- Cache TTL is short — not a long-term KV store

---

## Alternatives

| Tool | Strengths | Weaknesses |
|------|-----------|------------|
| OpenAI GPT-4.1 | Broader ecosystem | Prompt caching model differs |
| Google Gemini | Native video, 1M context | Different API |
| Groq | Lower latency | No Claude on Groq (typically) |
| AWS Bedrock Claude | Enterprise AWS | Extra abstraction layer |

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Missing `max_tokens` | Always set explicitly |
| System prompt in messages | Use `system` parameter |
| Not using prompt caching | Cache stable prefixes |
| Unbounded tool loops | Max iterations + timeout |
| Ignoring cache metrics | Log cache read/create tokens |

---

## Navigation

### Prerequisites

- [LLM Streaming](../llm-streaming.md)

### Related Topics

- [OpenAI](openai.md)
- [Vision and Multimodal Models](../vision-and-multimodal-models.md)

---

## See Also

- [Software Engineering for AI](../../foundations/software-engineering-for-ai.md)
- [Error Handling for AI Backends](../../backend-engineering/error-handling-for-ai-backends.md)

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Initial version |
