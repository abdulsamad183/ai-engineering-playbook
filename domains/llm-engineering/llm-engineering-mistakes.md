---
title: "LLM Engineering Mistakes"
description: "Production reference for the LLM engineering mistakes that sink demos — poor model selection, excessive prompts, token limits, hallucinations, unstructured outputs, temperature misuse, context management, cost explosions, latency, streaming, and API misuse."
domain: llm-engineering
tags: [llm, debugging, production, intermediate, mistakes]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - llm-cost-optimization.md
  - llm-performance-optimization.md
  - llm-security-fundamentals.md
  - ../common-mistakes/common-engineering-mistakes.md
keywords: [LLM mistakes, hallucinations, model selection, token limits, temperature, context management, cost explosion]
author: hp
---

# LLM Engineering Mistakes

> Section 20 of Phase 4 — the gap between a working demo and a production LLM system is a graveyard of predictable mistakes. This document catalogs the failures that recur across teams, with symptoms, root causes, diagnostics, fixes, and prevention for each.

## Table of Contents

- [How to Use This Guide](#how-to-use-this-guide)
- [Mistake Severity Matrix](#mistake-severity-matrix)
- [1. Poor Model Selection](#1-poor-model-selection)
- [2. Excessive Prompts](#2-excessive-prompts)
- [3. Ignoring Token Limits](#3-ignoring-token-limits)
- [4. Hallucinations Untreated](#4-hallucinations-untreated)
- [5. Unstructured Outputs](#5-unstructured-outputs)
- [6. Temperature Misuse](#6-temperature-misuse)
- [7. Context Management Failures](#7-context-management-failures)
- [8. Cost Explosions](#8-cost-explosions)
- [9. Latency Blindness](#9-latency-blindness)
- [10. Streaming Neglect](#10-streaming-neglect)
- [11. API Misuse](#11-api-misuse)
- [12. No Observability](#12-no-observability)
- [Pre-Production Checklist](#pre-production-checklist)
- [Interview Preparation](#interview-preparation)
- [Navigation](#navigation)

---

## How to Use This Guide

Each mistake follows a consistent diagnostic framework:

| Section | Purpose |
|---------|---------|
| **Symptoms** | What you observe in production, logs, or user reports |
| **Root Cause** | Why the mistake happens — the engineering failure, not the model |
| **Diagnose** | How to confirm this is the problem |
| **Fix** | Concrete remediation steps |
| **Prevention** | Practices that stop recurrence |

Cross-references point to detailed guides in Phase 4.

> **Production Standard:** When an LLM feature fails in production, check this list before blaming the model. Most incidents are system design failures.

---

## Mistake Severity Matrix

| Mistake | User Impact | Cost Risk | Reliability Risk | Security Risk |
|---------|------------|-----------|-----------------|---------------|
| Poor model selection | Medium | **Critical** | Medium | Low |
| Excessive prompts | Low | **Critical** | Low | Low |
| Ignoring token limits | High | High | **Critical** | Low |
| Hallucinations untreated | **Critical** | Low | **Critical** | Medium |
| Unstructured outputs | High | Medium | **Critical** | Medium |
| Temperature misuse | Medium | Low | High | Low |
| Context management failures | High | High | **Critical** | Medium |
| Cost explosions | Low | **Critical** | Medium | Low |
| Latency blindness | **Critical** | Medium | High | Low |
| Streaming neglect | High | Medium | Medium | Low |
| API misuse | High | High | **Critical** | High |
| No observability | Medium | High | **Critical** | Medium |

---

## 1. Poor Model Selection

### Symptoms

- Simple classification tasks take 3+ seconds
- Monthly API bill 5–20× higher than projected
- Quality is excellent but users complain about speed
- Quality is poor but team keeps upgrading to larger models

### Root Cause

Teams pick models by benchmark hype, team preference, or "always use the best" defaults instead of task-specific evaluation. No eval harness exists to test whether a cheaper model suffices.

### Diagnose

```python
# Compare models on your actual data
EVAL_PROMPTS = load_golden_set("eval/classification.json")  # 50–100 examples

for model in ["gpt-4.1-nano", "gpt-4.1-mini", "gpt-4.1"]:
  results = await run_eval(model, EVAL_PROMPTS)
  print(f"{model}: accuracy={results.accuracy:.2%}, "
        f"avg_latency={results.latency_ms}ms, "
        f"cost_per_1k=${results.cost_per_1k:.4f}")
```

Check: is the premium model's accuracy gain worth the cost/latency increase?

### Fix

1. Build a 50–100 example golden eval set from real production data
2. Test smallest model first; escalate only if accuracy below threshold
3. Implement tiered routing by task complexity
4. Pin model versions in config

```python
MODEL_ROUTING = {
  "classification": "gpt-4.1-nano",
  "extraction": "gpt-4.1-mini",
  "generation": "gpt-4.1-mini",
  "reasoning": "o4-mini",
}
```

### Prevention

- Eval-driven model selection before every launch
- Quarterly model audit against new releases
- Cost-per-successful-request metric, not cost-per-request

See [Model Comparison Guide](model-comparison-guide.md).

---

## 2. Excessive Prompts

### Symptoms

- Input tokens consistently 4K–10K+ for simple tasks
- System prompt alone exceeds 2,000 tokens
- Few-shot examples duplicated across every request
- Same instructions repeated in system and user messages

### Root Cause

Prompts grow organically — each bug fix adds another instruction line. Few-shot examples accumulate. Brand guidelines and edge case handling bloat the system prompt. Nobody audits token count.

### Diagnose

```python
import tiktoken

enc = tiktoken.encoding_for_model("gpt-4")
system_tokens = len(enc.encode(SYSTEM_PROMPT))
print(f"System prompt: {system_tokens} tokens")  # if > 500, investigate
```

Log `input_tokens` per request. Alert when input exceeds 2× the expected baseline.

### Fix

1. Audit system prompt — remove redundant instructions
2. Replace few-shot examples with JSON Schema constraints
3. Externalize and version prompts; review on each change
4. Split mega-prompts into task-specific prompts
5. Enable prompt caching for static prefixes

```python
# BEFORE: 1,200 tokens
BLOATED = "You are helpful... [brand guide] ... [20 few-shot examples] ..."

# AFTER: 120 tokens
FOCUSED = "Extract invoice fields as JSON per schema. Missing fields → null."
```

### Prevention

- Token budget per prompt template (max 500 tokens system)
- Prompt review in PR process with token count
- A/B test prompt changes against eval set

See [LLM Cost Optimization](llm-cost-optimization.md#prompt-optimization).

---

## 3. Ignoring Token Limits

### Symptoms

- Truncated responses mid-sentence
- `context_length_exceeded` errors in production
- Model "forgets" conversation after 10+ turns
- RAG answers miss information from middle chunks

### Root Cause

No pre-flight token counting. Full conversation history sent every turn. RAG injects all retrieved chunks without budget. `max_tokens` set too low for expected output or not set at all.

### Diagnose

```python
# Log truncation events
if response.choices[0].finish_reason == "length":
  log.warning("output_truncated", max_tokens=kwargs.get("max_tokens"),
              output_tokens=response.usage.completion_tokens)

# Check if input nears context limit
if response.usage.prompt_tokens > CONTEXT_LIMIT * 0.9:
  log.warning("near_context_limit", prompt_tokens=response.usage.prompt_tokens)
```

### Fix

1. Count tokens before every API call
2. Implement sliding window (last 6–10 turns) for chat history
3. Rolling summarization for long conversations
4. RAG: rerank to top 3–5 chunks, not 10+
5. Set `max_tokens` per endpoint based on expected output

```python
def build_messages_with_budget(
  system: str, history: list, user_msg: str, budget: int
) -> list[dict]:
  messages = [{"role": "system", "content": system}]
  messages.extend(history[-6:])
  messages.append({"role": "user", "content": user_msg})
  # validate total tokens < budget before sending
  return messages
```

### Prevention

- Token budget enforced in context builder
- Truncation logging and alerting
- Test with 30+ turn conversations in CI

See [Context Windows](context-windows.md) and [Tokens and Tokenization](tokens-and-tokenization.md).

---

## 4. Hallucinations Untreated

### Symptoms

- Model cites non-existent sources, laws, or statistics
- Product details, prices, or features are fabricated
- Code references functions that don't exist
- Users report "the AI lied to me"

### Root Cause

LLMs are trained to produce plausible text, not truthful text. No grounding (RAG), no output verification, no confidence thresholds, and no user-facing disclaimers for uncertain domains.

### Diagnose

- Run eval set with known-answer questions; measure factual accuracy
- Check if responses include citations — are cited sources real?
- Review user complaints tagged "wrong" or "made up"
- Test edge cases: obscure facts, recent events, specific numbers

### Fix

| Strategy | When to Use |
|----------|------------|
| RAG grounding | Domain-specific knowledge |
| Structured output with source fields | Force citation of retrieved chunks |
| Confidence scoring | Flag low-confidence answers |
| Retrieval-only mode | High-stakes factual queries |
| Human review queue | Medical, legal, financial |
| "I don't know" prompting | Instruct model to decline when uncertain |

```python
SYSTEM_GROUNDED = """
Answer ONLY using the provided reference documents.
If the answer is not in the documents, say "I don't have that information."
Cite document IDs for every claim.
"""
```

### Prevention

- Eval harness with factual accuracy metrics
- RAG for domain knowledge; never rely on parametric memory alone
- User-facing confidence indicators
- Feedback loop: users can flag incorrect answers

---

## 5. Unstructured Outputs

### Symptoms

- `JSONDecodeError` in production logs
- Regex parsing breaks on format variations
- Downstream services receive malformed data
- Retry loops on parse failures

### Root Cause

Teams prompt "return JSON" without schema constraints. Free-form text is parsed with regex or string splitting. No Pydantic validation on output.

### Diagnose

```python
# Track parse failure rate
parse_failures = sum(1 for r in results if not try_parse_json(r))
failure_rate = parse_failures / len(results)
print(f"Parse failure rate: {failure_rate:.1%}")  # > 5% is a problem
```

### Fix

1. Use schema-constrained generation (`response_format.json_schema`)
2. Validate with Pydantic after generation
3. Retry with error feedback (2–3 attempts max)
4. Fallback to secondary provider on persistent failure

```python
from pydantic import BaseModel


class ExtractionResult(BaseModel):
  name: str
  amount: float
  date: str


response = await client.chat.completions.create(
  model="gpt-4.1-mini",
  messages=messages,
  response_format={
    "type": "json_schema",
    "json_schema": {
      "name": "extraction",
      "schema": ExtractionResult.model_json_schema(),
    },
  },
  temperature=0,
)
result = ExtractionResult.model_validate_json(response.choices[0].message.content)
```

### Prevention

- Never parse business-critical data from free-form text
- Schema + Pydantic on every extraction endpoint
- Monitor validation failure rate

See [Structured Outputs](structured-outputs.md).

---

## 6. Temperature Misuse

### Symptoms

- Same prompt gives different results on every call (extraction)
- Creative writing is repetitive and bland
- Classification labels vary between identical inputs
- Non-deterministic test failures in CI

### Root Cause

Default temperature (often 1.0) used for all tasks. Teams don't understand that temperature controls randomness. Extraction uses temperature=0.8; creative tasks use temperature=0.

### Diagnose

Run the same prompt 10 times. If results vary for a task that should be deterministic, temperature is too high.

```python
# Quick temperature audit
for temp in [0, 0.3, 0.7, 1.0]:
  results = [await classify(prompt, temperature=temp) for _ in range(10)]
  unique = len(set(results))
  print(f"temp={temp}: {unique}/10 unique results")
```

### Fix

| Task Type | Temperature | Top-P |
|-----------|------------|-------|
| Classification / extraction | 0 | — |
| Summarization | 0–0.3 | 0.9 |
| Chat / Q&A | 0.3–0.7 | 0.95 |
| Creative writing | 0.7–1.0 | 0.95 |
| Code generation | 0–0.2 | 0.95 |

```python
TASK_PARAMS = {
  "extract": {"temperature": 0, "max_tokens": 300},
  "summarize": {"temperature": 0.2, "max_tokens": 500},
  "chat": {"temperature": 0.5, "max_tokens": 1000},
  "creative": {"temperature": 0.8, "max_tokens": 2000},
}
```

### Prevention

- Temperature per endpoint in config, not hardcoded
- Document expected temperature in prompt registry
- CI tests use temperature=0 for reproducibility

See [Sampling and Decoding](sampling-and-decoding.md).

---

## 7. Context Management Failures

### Symptoms

- Chatbot "forgets" information from early in conversation
- RAG answers ignore relevant middle chunks
- Context window exceeded errors after long sessions
- Quality degrades as conversation grows

### Root Cause

No context management strategy. Full history sent until it breaks. No summarization. RAG dumps all chunks without relevance filtering. "Lost in the middle" effect unaddressed.

### Diagnose

- Log what messages are sent per request (count and token total)
- Test 30+ turn conversation — does the bot remember turn 3?
- Check RAG: are all chunks used or only first/last?

### Fix

```python
async def build_chat_context(
  user_id: str,
  new_message: str,
  db,
  token_budget: int = 6000,
) -> list[dict]:
  history = await db.get_recent_messages(user_id, limit=20)
  summary = await db.get_conversation_summary(user_id)

  messages = [{"role": "system", "content": SYSTEM_PROMPT}]
  if summary:
    messages.append({"role": "system", "content": f"Summary: {summary}"})
  messages.extend(history[-6:])
  messages.append({"role": "user", "content": new_message})

  # trigger summarization when history > 12 turns
  if len(history) > 12:
    asyncio.create_task(summarize_and_store(user_id, history[:-6]))

  return messages
```

### Prevention

- Sliding window + rolling summary as default chat pattern
- RAG: rerank to top 3–5; place critical chunks at start/end
- Token budget enforced pre-flight
- Test long conversations in eval

See [Context Windows](context-windows.md).

---

## 8. Cost Explosions

### Symptoms

- Monthly bill 5–50× over budget
- Finance escalation
- A single endpoint accounts for 80%+ of spend
- Retry loops multiplying costs

### Root Cause

Combination of: premium model for all tasks, bloated prompts, unbounded history, no `max_tokens`, no rate limiting, no per-user budgets, RAG over-injection, and retry without caps.

### Diagnose

```sql
-- If using structured logs in a warehouse
SELECT endpoint, model,
       AVG(input_tokens) as avg_input,
       AVG(output_tokens) as avg_output,
       COUNT(*) as requests,
       SUM(estimated_cost_usd) as total_cost
FROM llm_completions
WHERE date >= CURRENT_DATE - 7
GROUP BY 1, 2
ORDER BY total_cost DESC;
```

Identify the top 3 cost drivers. Fix the biggest first.

### Fix

1. Model routing (nano/mini for simple tasks)
2. Prompt audit and compression
3. Context reduction (sliding window, RAG top-3)
4. `max_tokens` per endpoint
5. Per-user daily budget caps
6. Prompt caching for static prefixes
7. Retry cap (max 2–3)
8. Stream disconnect handling

### Prevention

- Cost dashboard with daily alerts at 80% of budget
- Per-request cost logging
- Monthly model tier audit
- Load test cost projection before launch

See [LLM Cost Optimization](llm-cost-optimization.md).

---

## 9. Latency Blindness

### Symptoms

- Users complain the app is "slow" but metrics show "fine"
- P95 latency 5–10× higher than P50
- No decomposition of where time is spent
- Team optimizes the wrong component

### Root Cause

Only measuring total request time. Not decomposing TTFT, TPOT, queue wait, network RTT. Not setting per-endpoint SLOs. Optimizing decode when prefill is the bottleneck.

### Diagnose

```python
tracker = LatencyTracker()
tracker.mark("request_start")
# ... build context ...
tracker.mark("context_ready")
# ... LLM call (streaming) ...
tracker.mark("first_token")
# ... stream complete ...
tracker.mark("complete")
print(tracker.report())
# context_ready→first_token = TTFT (usually the problem)
```

### Fix

| Bottleneck | Fix |
|-----------|-----|
| High TTFT | Shorter prompts, prompt caching, smaller context |
| High TPOT | Smaller model, fewer output tokens |
| High queue wait | Scale replicas, rate limit |
| High network RTT | Regional endpoints, connection pooling |
| High post-processing | Async validation, stream parsing |

### Prevention

- Decomposed latency dashboards (TTFT, TPOT, queue, total)
- Per-endpoint SLOs with P95 alerts
- Load test at 2× expected traffic

See [LLM Performance Optimization](llm-performance-optimization.md) and [LLM Inference](llm-inference.md).

---

## 10. Streaming Neglect

### Symptoms

- Chat UI shows blank screen for 3–8 seconds
- Users refresh or abandon during generation
- Full response buffered before display
- Tokens wasted on disconnected clients

### Root Cause

Non-streaming API calls for chat UIs. Backend buffers entire response before sending to client. No disconnect handling — generation continues after user leaves.

### Diagnose

- Check if `stream=True` is set on chat endpoints
- Measure time-to-first-byte at the client
- Check logs for completed generations after client disconnect

### Fix

```python
from fastapi.responses import StreamingResponse


@app.post("/chat")
async def chat(request: ChatRequest):
  async def event_generator():
    stream = await client.chat.completions.create(
      model="gpt-4.1-mini",
      messages=request.messages,
      stream=True,
    )
    try:
      async for chunk in stream:
        if await request.is_disconnected():
          break  # stop generating
        delta = chunk.choices[0].delta.content
        if delta:
          yield f"data: {json.dumps({'content': delta})}\n\n"
    finally:
      yield "data: [DONE]\n\n"

  return StreamingResponse(event_generator(), media_type="text/event-stream")
```

### Prevention

- Streaming by default for all chat endpoints
- Client disconnect cancels upstream
- TTFT SLO monitoring

See [LLM Streaming](llm-streaming.md).

---

## 11. API Misuse

### Symptoms

- `429 Too Many Requests` under moderate load
- Connection timeouts and `ConnectionError`
- Inconsistent error handling across endpoints
- New `AsyncOpenAI()` client created per request

### Root Cause

No connection pooling. No retry with backoff. No timeout configuration. Synchronous SDK in async handlers. Hardcoded model names. No error classification (retryable vs fatal).

### Diagnose

- Check if client is singleton or per-request
- Review error logs for 429, 500, timeout patterns
- Profile connection establishment overhead

### Fix

```python
import httpx
from openai import AsyncOpenAI, RateLimitError, APIStatusError

http_client = httpx.AsyncClient(
  limits=httpx.Limits(max_connections=100, max_keepalive_connections=20),
  timeout=httpx.Timeout(connect=5.0, read=60.0, write=10.0, pool=5.0),
)
client = AsyncOpenAI(http_client=http_client)


async def call_with_retry(messages: list[dict], model: str, max_retries: int = 3):
  for attempt in range(max_retries):
    try:
      return await client.chat.completions.create(
        model=model, messages=messages, timeout=30.0,
      )
    except RateLimitError:
      await asyncio.sleep(2 ** attempt)
    except APIStatusError as e:
      if e.status_code >= 500:
        await asyncio.sleep(2 ** attempt)
      else:
        raise
  raise RuntimeError(f"Failed after {max_retries} retries")
```

### Prevention

- Singleton async client with connection pooling
- Retry only on 429 and 5xx with exponential backoff
- Timeouts on every call
- Model names in config, not code
- Error classification in middleware

See provider guides: [OpenAI](providers/openai.md), [Anthropic Claude](providers/anthropic-claude.md).

---

## 12. No Observability

### Symptoms

- "The AI is wrong sometimes" — no data to investigate
- Cannot answer "what model was used?" for a specific request
- No cost attribution per user or endpoint
- Incidents discovered by users, not alerts

### Root Cause

No structured logging of LLM calls. No metrics on tokens, latency, errors, or cost. No tracing across the request pipeline. Debugging requires reproducing in dev.

### Diagnose

Can you answer these for any production request in the last 24 hours?
- What model was used?
- How many input/output tokens?
- What was the latency breakdown?
- Did validation pass?
- What did it cost?

If no → observability gap.

### Fix

```python
import structlog

log = structlog.get_logger()


async def instrumented_completion(client, **kwargs):
  import time
  start = time.perf_counter()

  response = await client.chat.completions.create(**kwargs)
  elapsed_ms = (time.perf_counter() - start) * 1000

  log.info(
    "llm_completion",
    model=kwargs.get("model"),
    input_tokens=response.usage.prompt_tokens,
    output_tokens=response.usage.completion_tokens,
    cached_tokens=getattr(response.usage, "prompt_tokens_details", {})
      .get("cached_tokens", 0),
    latency_ms=round(elapsed_ms, 1),
    finish_reason=response.choices[0].finish_reason,
  )
  return response
```

### Prevention

- Structured logging on every LLM call (model, tokens, latency, cost)
- Dashboards: cost, latency P50/P95, error rate, validation failure rate
- Alerts on anomaly thresholds
- Request ID tracing across the pipeline

---

## Pre-Production Checklist

Before shipping any LLM feature:

- [ ] Model selected via eval, not default
- [ ] System prompt under 500 tokens
- [ ] Token budget enforced pre-flight
- [ ] `max_tokens` set per endpoint
- [ ] Temperature appropriate per task type
- [ ] Structured outputs with Pydantic validation
- [ ] Hallucination mitigation (RAG, grounding, or disclaimers)
- [ ] Context management (sliding window or summary)
- [ ] Streaming enabled for chat
- [ ] Client disconnect handling
- [ ] Singleton async client with pooling
- [ ] Retry with backoff (max 2–3)
- [ ] Rate limiting per user
- [ ] Cost logging and budget caps
- [ ] Latency decomposition in metrics
- [ ] Security review (no secrets in prompts, tool auth)

---

## Interview Preparation

### Frequently Asked Questions

**Q1: What are the most common LLM production failures?**

> **Strong answer:** Cost explosions from wrong model tier and bloated context. Reliability failures from unstructured outputs and no validation. Latency issues from no streaming and oversized context. Security failures from trusting LLM tool arguments. Most trace to system design, not model quality.

**Q2: How do you debug a sudden 10× cost increase?**

> **Strong answer:** Query per-endpoint cost breakdown. Check for: model tier change, prompt bloat, unbounded history, RAG over-injection, retry loops, new high-traffic endpoint. Fix highest-impact driver first. Usually context reduction or model routing resolves 80% of overspend.

**Q3: A user says the chatbot "forgot" their name after 20 minutes. What's wrong?**

> **Strong answer:** Context management failure. Full history likely exceeded the context window and early messages were truncated. Fix: rolling summarization that preserves key facts, structured memory (extract entities to DB), sliding window with summary. Test with 30+ turn conversations.

**Q4: How do you prevent hallucinations in a customer-facing Q&A bot?**

> **Strong answer:** RAG grounding with retrieved documents. Instruct model to answer only from provided context and say "I don't know" otherwise. Structured output with source citations. Eval harness with factual accuracy metrics. Human review queue for high-stakes queries.

**Q5: Your extraction endpoint has 15% JSON parse failures. How do you fix it?**

> **Strong answer:** Switch from "return JSON" prompting to schema-constrained generation. Add Pydantic validation. Retry with error feedback (max 2–3). Set temperature=0. Monitor validation failure rate. If still failing, simplify schema or split into multi-step extraction.

### Real-World Scenario

**Scenario:** Your team shipped a RAG chatbot. Week 1: great feedback. Week 3: users report wrong answers, slow responses, and a $8K API bill (budget was $1K).

> **Discussion points:**
> - **Wrong answers:** RAG retrieving irrelevant chunks; no grounding instruction; hallucination on out-of-scope questions
> - **Slow:** 8 chunks × 500 tokens = 4K extra prefill; no streaming; large model for simple queries
> - **Cost:** Premium model + bloated context + no caching + full history every turn
> - **Fix priority:** Rerank to top 3 chunks, switch to mini model, enable streaming, add sliding window, set per-user budgets, add "I don't know" prompting

---

## Navigation

### Prerequisites

- Sections 1–12 of Phase 4 (foundational LLM engineering)
- [Common Engineering Mistakes](../common-mistakes/common-engineering-mistakes.md) — general AI app mistakes

### Phase 4 — LLM Engineering

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
| 17 | LLM Cost Optimization | [llm-cost-optimization.md](llm-cost-optimization.md) |
| 18 | LLM Performance Optimization | [llm-performance-optimization.md](llm-performance-optimization.md) |
| 19 | LLM Security Fundamentals | [llm-security-fundamentals.md](llm-security-fundamentals.md) |
| 20 | LLM Engineering Mistakes | **You are here** |

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

- [LLM Cost Optimization](llm-cost-optimization.md) — Section 17
- [LLM Performance Optimization](llm-performance-optimization.md) — Section 18
- [LLM Security Fundamentals](llm-security-fundamentals.md) — Section 19
- [Common Engineering Mistakes](../common-mistakes/common-engineering-mistakes.md)

### Next Topics (Phase 5+)

- [Prompt Engineering](../prompt-engineering/README.md)
- [RAG](../rag/README.md)
- [AI Evaluation](../ai-evaluation/README.md)

---

## See Also

- [Common Engineering Mistakes in AI Applications](../common-mistakes/common-engineering-mistakes.md)
- [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- [LLM Cost Optimization](llm-cost-optimization.md)
- [LLM Performance Optimization](llm-performance-optimization.md)

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Initial Phase 4 release — Section 20 |
