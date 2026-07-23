---
title: "LLM Cost Optimization"
description: "Production guide to reducing LLM spend — prompt optimization, token reduction, model selection, caching, batch processing, context reduction, cost monitoring, and production cost control strategies."
domain: llm-engineering
tags: [llm, cost, production, intermediate, optimization]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - tokens-and-tokenization.md
  - context-windows.md
  - model-comparison-guide.md
  - llm-performance-optimization.md
keywords: [cost optimization, token reduction, prompt caching, batch API, model selection, cost monitoring]
author: hp
---

# LLM Cost Optimization

> Section 17 of this handbook — LLM costs scale with tokens × price × traffic. Unlike traditional compute, a single prompt design mistake can multiply spend overnight. Cost optimization is continuous engineering, not a one-time model downgrade.

## Table of Contents

- [Cost Anatomy](#cost-anatomy)
- [Prompt Optimization](#prompt-optimization)
- [Token Reduction](#token-reduction)
- [Model Selection](#model-selection)
- [Caching Strategies](#caching-strategies)
- [Batch Processing](#batch-processing)
- [Context Reduction](#context-reduction)
- [Cost Monitoring](#cost-monitoring)
- [Production Strategies](#production-strategies)
- [Cost Optimization Checklist](#cost-optimization-checklist)
- [Common Mistakes](#common-mistakes)
- [Interview Preparation](#interview-preparation)
- [Navigation](#navigation)

---

## Cost Anatomy

Every LLM bill decomposes into measurable components.

```text
Total Cost = Σ (input_tokens × input_rate + output_tokens × output_rate)
           + tool_call_overhead
           + embedding_cost
           + retry_waste
           + failed_request_waste
```

| Cost Driver | Typical Share | Primary Lever |
|-------------|--------------|---------------|
| Input tokens (system + context) | 40–70% | Prompt design, context reduction |
| Output tokens | 20–50% | `max_tokens`, concise prompts |
| Model tier | Multiplier | Model routing |
| Retries | 5–15% | Structured outputs, validation |
| Wasted streams | 2–10% | Disconnect handling |

```python
def estimate_cost(
  input_tokens: int,
  output_tokens: int,
  input_rate_per_m: float = 0.40,
  output_rate_per_m: float = 1.60,
) -> float:
  """Estimate USD cost for a single request."""
  return (input_tokens * input_rate_per_m + output_tokens * output_rate_per_m) / 1_000_000
```

> **Production Standard:** Instrument every request with `input_tokens`, `output_tokens`, `model`, and `estimated_cost_usd`. Alert on daily spend anomalies before finance does.

See [Tokens and Tokenization](tokens-and-tokenization.md) for counting mechanics.

---

## Prompt Optimization

Prompts are the highest-leverage cost knob — they affect both input and output tokens.

### Principles

| Principle | Savings | Example |
|-----------|---------|---------|
| Shorter system prompts | 10–40% input | Remove redundant instructions |
| Few-shot → zero-shot | 20–60% input | Use schema constraints instead |
| Output format constraints | 20–50% output | "Return JSON only, no explanation" |
| Task-specific prompts | 10–30% overall | Don't use one mega-prompt for all tasks |
| External prompt storage | Indirect | Version and A/B test without redeploying |

### Before and After

```python
# BAD — bloated system prompt (800+ tokens)
BLOATED_SYSTEM = """
You are a helpful AI assistant created by our company. You should always
be polite, professional, and thorough. When answering questions, make sure
to consider all aspects of the user's request. If you are unsure, say so.
Always format your response in a clear and organized manner with headers
and bullet points. Remember our company values: integrity, innovation...
[200 more lines of brand guidelines]
"""

# GOOD — focused system prompt (80 tokens)
FOCUSED_SYSTEM = """
Extract invoice fields as JSON matching the provided schema.
If a field is missing, use null. No commentary.
"""
```

### Prompt Compression Techniques

1. **Remove duplicate instructions** across system and user messages
2. **Replace few-shot examples** with JSON Schema constraints
3. **Use abbreviations** in internal prompts (not user-facing)
4. **Split prompts by task** — classification prompt ≠ generation prompt
5. **Cache static prefixes** — see [Caching Strategies](#caching-strategies)

---

## Token Reduction

| Technique | Where Applied | Typical Reduction |
|-----------|--------------|-------------------|
| Trim conversation history | Context builder | 30–70% input |
| Summarize old turns | Memory layer | 50–80% on long chats |
| RAG chunk limit | Retrieval pipeline | 40–60% input |
| Lower `max_tokens` | API call | Caps output waste |
| Strip whitespace / metadata | Preprocessing | 5–15% input |
| Compact tool schemas | Agent definitions | 10–30% input |

```python
import tiktoken


def truncate_to_token_budget(text: str, max_tokens: int, model: str = "gpt-4") -> str:
  enc = tiktoken.encoding_for_model(model)
  tokens = enc.encode(text)
  if len(tokens) <= max_tokens:
    return text
  return enc.decode(tokens[:max_tokens])
```

### Output Token Control

```python
response = await client.chat.completions.create(
  model="gpt-4.1-mini",
  messages=messages,
  max_tokens=256,          # hard cap on output
  temperature=0,           # reduce rambling
  response_format={"type": "json_object"},  # no prose wrapper
)
```

---

## Model Selection

The cheapest model that passes your eval is the right model.

### Tiered Routing

```python
from enum import Enum


class ModelTier(str, Enum):
  NANO = "gpt-4.1-nano"       # ~$0.10/$0.40 per 1M
  MINI = "gpt-4.1-mini"       # ~$0.40/$1.60 per 1M
  STANDARD = "gpt-4.1"        # ~$2.00/$8.00 per 1M
  REASONING = "o4-mini"       # higher, but cheaper than o3


async def route_by_complexity(classifier_result: str) -> str:
  mapping = {
    "simple": ModelTier.NANO,
    "standard": ModelTier.MINI,
    "complex": ModelTier.STANDARD,
    "reasoning": ModelTier.REASONING,
  }
  return mapping.get(classifier_result, ModelTier.MINI)
```

### Model Selection Matrix

| Task | Recommended Tier | Avoid |
|------|-----------------|-------|
| Intent classification | Nano / Flash-Lite | GPT-4.1 |
| Entity extraction | Mini + schema | Opus |
| Long-form writing | Standard | Reasoning models |
| Math / planning | Reasoning (o4-mini) | Largest model always |
| Embeddings | text-embedding-3-small | Large embedding model |

See [Model Comparison Guide](model-comparison-guide.md) for family-level comparison.

---

## Caching Strategies

### Prompt Caching (Provider-Native)

Providers cache identical prompt prefixes across requests. You pay reduced rates on cached tokens.

| Provider | Feature | Best For |
|----------|---------|----------|
| OpenAI | Automatic prompt caching | Repeated system prompts |
| Anthropic | Explicit `cache_control` | Long system prompts, tool defs |
| Gemini | Context caching | Large document context |

```python
# Anthropic — mark cacheable blocks
messages = [
  {
    "role": "user",
    "content": [
      {
        "type": "text",
        "text": LARGE_SYSTEM_CONTEXT,
        "cache_control": {"type": "ephemeral"},
      },
      {"type": "text", "text": user_query},
    ],
  }
]
```

### Application-Level Caching

| Cache Type | Key | TTL | Savings |
|------------|-----|-----|---------|
| Exact match | hash(prompt + model + params) | 1h–24h | 100% on hit |
| Semantic | embedding similarity > 0.95 | 1h–6h | 80–100% on near-duplicates |
| Embedding cache | hash(text) | 7d | Avoid re-embedding |
| RAG retrieval cache | hash(query) | 15m–1h | Skip retrieval + generation |

```python
import hashlib
import json


def cache_key(prompt: str, model: str, params: dict) -> str:
  payload = json.dumps({"prompt": prompt, "model": model, **params}, sort_keys=True)
  return hashlib.sha256(payload.encode()).hexdigest()
```

> **Caution:** Never cache responses containing user-specific PII without scoping the cache key to `user_id`.

---

## Batch Processing

Batch APIs offer 50% discounts for non-real-time workloads.

| Workload | Batch Fit | Latency Tolerance |
|----------|-----------|-------------------|
| Nightly document processing | Excellent | Hours |
| Evaluation runs | Excellent | Minutes–hours |
| Email classification backlog | Good | Minutes |
| Interactive chat | Poor | Milliseconds |

```python
# OpenAI Batch API pattern (conceptual)
batch_request = {
  "custom_id": "invoice-001",
  "method": "POST",
  "url": "/v1/chat/completions",
  "body": {
    "model": "gpt-4.1-mini",
    "messages": [{"role": "user", "content": "Extract fields from: ..."}],
    "max_tokens": 200,
  },
}
```

### When Batch Beats Real-Time

```text
If: volume > 1000 requests/day AND latency SLO > 1 hour
Then: batch API (50% off)
Else: real-time with caching and model routing
```

---

## Context Reduction

Context is the silent cost killer — especially in RAG and long chat sessions.

### Strategies

| Strategy | Mechanism | Savings |
|----------|-----------|---------|
| Sliding window | Keep last N turns | Linear with history length |
| Rolling summary | Compress old turns to summary | 60–90% on long chats |
| RAG top-K reduction | 10 chunks → 3 chunks | 50–70% input |
| Relevance threshold | Drop low-score chunks | 20–40% input |
| Tool result pruning | Summarize tool outputs before re-injection | 30–60% per agent turn |

```python
def build_context(
  system_prompt: str,
  recent_messages: list[dict],
  summary: str | None,
  rag_chunks: list[str],
  token_budget: int,
) -> list[dict]:
  messages = [{"role": "system", "content": system_prompt}]

  if summary:
    messages.append({"role": "system", "content": f"Prior conversation summary: {summary}"})

  messages.extend(recent_messages[-6:])  # sliding window

  if rag_chunks:
    # inject only top 3 after reranking
    context = "\n---\n".join(rag_chunks[:3])
    messages.insert(1, {"role": "system", "content": f"Reference:\n{context}"})

  return messages  # always validate token count before sending
```

See [Context Windows](context-windows.md) for truncation and budgeting.

---

## Cost Monitoring

### Metrics to Track

| Metric | Granularity | Alert Threshold |
|--------|-------------|-----------------|
| Daily spend (USD) | Global | > 120% of budget |
| Cost per request | Per endpoint | > 2× baseline |
| Cost per user | Per user_id | > daily cap |
| Token utilization | Per request | input > 8K unexpectedly |
| Retry rate | Per endpoint | > 5% |
| Cache hit rate | Per cache layer | < 30% (investigate) |
| Model tier distribution | Global | > 20% premium tier |

### Dashboard Structure

```python
# Structured log fields for cost observability
COST_LOG_FIELDS = {
  "event": "llm_completion",
  "model": "gpt-4.1-mini",
  "input_tokens": 1240,
  "output_tokens": 186,
  "cached_tokens": 800,
  "estimated_cost_usd": 0.0008,
  "user_id": "usr_abc",
  "endpoint": "/api/chat",
  "latency_ms": 890,
  "cache_hit": False,
  "retry_count": 0,
}
```

### Budget Enforcement

```python
class BudgetExceeded(Exception):
  pass


async def check_user_budget(user_id: str, estimated_cost: float, redis) -> None:
  key = f"budget:daily:{user_id}"
  current = float(await redis.get(key) or 0)
  daily_cap = 0.50  # $0.50 per user per day

  if current + estimated_cost > daily_cap:
    raise BudgetExceeded(f"Daily budget exceeded for {user_id}")

  await redis.incrbyfloat(key, estimated_cost)
  await redis.expire(key, 86400)
```

---

## Production Strategies

### Strategy 1: Tiered Model Routing

Route simple queries to cheap models; escalate only on failure or low confidence.

```text
Request → classifier (nano) → route to mini/standard/reasoning
                           → on validation failure, escalate one tier
```

### Strategy 2: Pre-Generation Filters

Use rules or lightweight models to avoid LLM calls entirely.

| Filter | Example |
|--------|---------|
| Regex | FAQ with known answers |
| Keyword match | Route to static response |
| Classifier (nano) | Skip LLM for "hello", "thanks" |
| Cache lookup | Exact or semantic match |

### Strategy 3: Response Length Budgets

| Use Case | max_tokens | Rationale |
|----------|-----------|-----------|
| Classification | 10–50 | Label only |
| Extraction | 200–500 | JSON fields |
| Summary | 300–800 | Bounded output |
| Chat | 500–1500 | UX vs cost tradeoff |

### Strategy 4: Offline vs Online Split

| Online (real-time) | Offline (batch) |
|-------------------|-----------------|
| User chat | Document indexing |
| Interactive agents | Bulk classification |
| Live extraction | Eval runs |
| Streaming responses | Report generation |

### Strategy 5: Cost-Aware Retry

```python
MAX_RETRIES = 2
ESCALATION_TIERS = ["gpt-4.1-mini", "gpt-4.1"]


async def extract_with_budget(data: str, tier_index: int = 0) -> dict:
  model = ESCALATION_TIERS[min(tier_index, len(ESCALATION_TIERS) - 1)]
  # try extraction; on validation failure, escalate only if tier_index < max
  ...
```

---

## Cost Optimization Checklist

Use before launch and monthly in production.

- [ ] Token counting on every request path
- [ ] Model routing by task complexity
- [ ] `max_tokens` set per endpoint
- [ ] System prompt audited for bloat
- [ ] Conversation history bounded (sliding window or summary)
- [ ] RAG chunk count limited and reranked
- [ ] Prompt caching enabled for static prefixes
- [ ] Response caching for repeated queries
- [ ] Batch API for offline workloads
- [ ] Per-user and global budget caps
- [ ] Cost dashboard with daily alerts
- [ ] Retry budget (max 2–3 per request)
- [ ] Stream disconnect cancels upstream
- [ ] Monthly model tier audit against eval results

---

## Common Mistakes

| Mistake | Cost Impact | Fix |
|---------|------------|-----|
| Full history on every turn | Linear cost growth | Sliding window + summary |
| 10K-token system prompt | Every request pays full price | Compress; cache |
| Premium model for all tasks | 5–20× overspend | Tiered routing |
| No `max_tokens` | Unbounded output bills | Set per endpoint |
| Retry without limit | 2–5× on failures | Cap retries; escalate model |
| Ignoring cached token metrics | Miss 50%+ savings | Enable prompt caching |
| No batch for offline jobs | Pay real-time rates | Batch API |
| RAG over-injection | Massive input tokens | Top-3 reranked chunks |

---

## Interview Preparation

### Frequently Asked Questions

**Q1: Your LLM costs are 10× over budget after launch. How do you diagnose?**

> **Strong answer:** Pull per-request token breakdown: input vs output, by endpoint and model. Check for system prompt bloat, unbounded history, RAG over-injection, retry loops, and premium model overuse. Compare cost per successful request vs raw request count. Fix highest-impact lever first — usually context reduction or model routing.

**Q2: How does prompt caching reduce costs?**

> **Strong answer:** Providers cache KV states for identical prompt prefixes. Subsequent requests with the same prefix skip recomputing those tokens, billed at a reduced cached rate. Structure prompts with static content first (system prompt, tool definitions, documents) and dynamic content last (user query).

**Q3: When is self-hosting cheaper than APIs?**

> **Strong answer:** When sustained token volume exceeds the break-even point where GPU amortization + ops cost beats API pricing — typically millions of tokens per day on consistent workloads. Also when data residency mandates it. Factor in engineering cost for vLLM ops, monitoring, and model updates.

**Q4: How do you implement per-user cost controls?**

> **Strong answer:** Estimate cost pre-request from token budget. Track cumulative spend in Redis per user per day. Reject or downgrade model when cap exceeded. Log all spend. Alert on anomalies. Offer tiered plans with different caps.

### Real-World Scenario

**Scenario:** A RAG chatbot costs $12,000/month. Finance wants it under $3,000 without quality loss.

> **Discussion points:** Audit token distribution — likely 60%+ is RAG context. Reduce chunks from 10 to 3 with reranking. Switch generation from GPT-4.1 to mini. Enable prompt caching on system prompt and document context. Add semantic cache for frequent queries. Summarize conversation history after 6 turns. Measure quality on eval set after each change.

---

## Navigation

### Prerequisites

- [Tokens and Tokenization](tokens-and-tokenization.md) — Section 3
- [Context Windows](context-windows.md) — Section 4
- [LLM Inference](llm-inference.md) — Section 9
- [Model Comparison Guide](model-comparison-guide.md) — Section 16

### — LLM Engineering

| # | Topic | Document |
|---|-------|----------|
| 1 | Introduction to LLM Engineering | [introduction-to-llm-engineering.md](introduction-to-llm-engineering.md) |
| 2 | How LLMs Work | [how-llms-work.md](how-llms-work.md) |
| 3 | Tokens and Tokenization | [tokens-and-tokenization.md](tokens-and-tokenization.md) |
| 4 | Context Windows | [context-windows.md](context-windows.md) |
| 5 | Embeddings — LLM Perspective | [embeddings-llm-perspective.md](embeddings-llm-perspective.md) |
| 6 | Transformer Intuition | [transformer-intuition.md](transformer-intuition.md) |
| 7 | Attention Mechanism | [attention-mechanism.md](attention-mechanism.md) |
| 8 | KV Cache | [kv-cache.md](kv-cache.md) |
| 9 | LLM Inference | [llm-inference.md](llm-inference.md) |
| 10 | Sampling and Decoding | [sampling-and-decoding.md](sampling-and-decoding.md) |
| 11 | Structured Outputs | [structured-outputs.md](structured-outputs.md) |
| 12 | Function Calling and Tools | [function-calling-and-tools.md](function-calling-and-tools.md) |
| — | LLM Streaming (supplementary) | [llm-streaming.md](llm-streaming.md) |
| — | Vision and Multimodal Models (supplementary) | [vision-and-multimodal-models.md](vision-and-multimodal-models.md) |
| 16 | Model Comparison Guide | [model-comparison-guide.md](model-comparison-guide.md) |
| 17 | LLM Cost Optimization | **You are here** |
| 18 | LLM Performance Optimization | [llm-performance-optimization.md](llm-performance-optimization.md) |
| 19 | LLM Security Fundamentals | [llm-security-fundamentals.md](llm-security-fundamentals.md) |
| 20 | LLM Engineering Mistakes | [llm-engineering-mistakes.md](llm-engineering-mistakes.md) |

### Provider Guides

| Provider | Document |
|----------|----------|
| OpenAI | [providers/openai.md](providers/openai.md) |
| Anthropic Claude | [providers/anthropic-claude.md](providers/anthropic-claude.md) |
| Google Gemini | [providers/google-gemini.md](providers/google-gemini.md) |
| Groq | [providers/groq.md](providers/groq.md) |
| OpenRouter | [providers/openrouter.md](providers/openrouter.md) |
| Ollama | [providers/ollama.md](providers/ollama.md) |

### Related Topics

- [LLM Performance Optimization](llm-performance-optimization.md) — Section 18
- [LLM Engineering Mistakes](llm-engineering-mistakes.md) — Section 20
- [Backend Engineering](../backend-engineering/README.md) — observability patterns

### Next Topics

- [LLM Performance Optimization](llm-performance-optimization.md) — latency tuning complements cost work
- [LLM Security Fundamentals](llm-security-fundamentals.md) — secure cost controls

---

## See Also

- [OpenAI Pricing](https://platform.openai.com/docs/pricing)
- [Anthropic Pricing](https://docs.anthropic.com/en/docs/about-claude/pricing)
- [OpenAI Batch API](https://platform.openai.com/docs/guides/batch)
- [Anthropic Prompt Caching](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching)

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Initial release — Section 17 |
