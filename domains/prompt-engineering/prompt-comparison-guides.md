---
title: "Prompt Comparison Guides"
description: "Decision reference for prompt engineering tradeoffs — zero-shot vs few-shot, XML vs JSON, chain-of-thought vs ReAct, ReAct vs tree-of-thought, chaining vs single prompt, static vs dynamic prompts, template vs generated prompts."
domain: prompt-engineering
tags: [prompt, patterns, production, intermediate, comparison]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - prompt-optimization.md
  - prompt-evaluation.md
  - production-prompt-engineering.md
keywords: [zero-shot, few-shot, chain-of-thought, ReAct, tree of thought, prompt chaining, XML, JSON]
author: hp
---

# Prompt Comparison Guides

> supplementary guide — every prompt engineering decision is a tradeoff. These comparison tables help you choose the right pattern for your task, model, and production constraints instead of defaulting to the most popular approach.

## Table of Contents

- [How to Use This Guide](#how-to-use-this-guide)
- [Zero-Shot vs Few-Shot](#zero-shot-vs-few-shot)
- [XML vs JSON](#xml-vs-json)
- [Chain-of-Thought vs ReAct](#chain-of-thought-vs-react)
- [ReAct vs Tree-of-Thought](#react-vs-tree-of-thought)
- [Chaining vs Single Prompt](#chaining-vs-single-prompt)
- [Static vs Dynamic Prompts](#static-vs-dynamic-prompts)
- [Template vs Generated Prompts](#template-vs-generated-prompts)
- [Decision Flowchart](#decision-flowchart)
- [Interview Preparation](#interview-preparation)
- [Navigation](#navigation)

---

## How to Use This Guide

Each comparison follows a consistent structure:

| Section | Contents |
|---------|----------|
| **Overview** | What each approach is |
| **Comparison Table** | Side-by-side across key dimensions |
| **When to Choose** | Decision heuristics |
| **Production Considerations** | Cost, latency, reliability |
| **Example** | Minimal code or prompt snippet |

> **Production Standard:** No pattern is universally best. Choose by task requirements, eval results, and SLOs — not by blog post popularity.

---

## Zero-Shot vs Few-Shot

### Overview

| Approach | Definition |
|----------|-----------|
| **Zero-shot** | Instructions only — no examples in the prompt |
| **Few-shot** | Instructions plus 1–N input/output examples |

### Comparison Table

| Dimension | Zero-Shot | Few-Shot |
|-----------|-----------|----------|
| **Token cost** | Low | High (scales with examples) |
| **Latency** | Fast (shorter prefill) | Slower (more prefill tokens) |
| **Format reliability** | Moderate — needs schema enforcement | High — model mimics examples |
| **Task complexity** | Simple classification, extraction with schema | Nuanced tasks, unusual formats |
| **Maintenance** | Easy — update instructions only | Hard — update examples when rules change |
| **Overfitting risk** | Low | High — model copies example patterns |
| **Model dependence** | Works well on capable models | Helps weaker models more |
| **Consistency** | Moderate | High (if examples are consistent) |
| **Best with** | Structured output mode, JSON schema | Complex reasoning, style matching |

### When to Choose

```text
Choose ZERO-SHOT when:
  → Task has clear schema (JSON mode + Pydantic validation)
  → Model is capable (GPT-4.1+, Claude Sonnet+)
  → Token budget is tight
  → Output format is standard (classification, extraction)

Choose FEW-SHOT when:
  → Zero-shot quality below threshold after schema optimization
  → Task requires style/tone matching
  → Output format is unusual or hard to describe
  → Weaker/cheaper model needs guidance
  → 1–3 carefully curated examples (not 8+)
```

### Production Considerations

| Factor | Zero-Shot | Few-Shot |
|--------|-----------|----------|
| Caching | Better — smaller static prefix | Worse — examples bloat cache key |
| Testing | Test instruction changes | Test instruction AND example changes |
| Drift risk | Lower | Higher — examples may become stale |
| Cost at scale | 1× | 2–5× depending on example count |

### Example

```python
# Zero-shot with schema enforcement
ZERO_SHOT = {
  "system": "Classify the ticket as JSON: {\"category\": \"billing|technical|account|other\"}",
  "config": {"response_format": {"type": "json_object"}, "temperature": 0.0},
}

# Few-shot (use sparingly)
FEW_SHOT = {
  "system": """Classify tickets as JSON.

Example 1: "Can't log in" → {"category": "account"}
Example 2: "Invoice is wrong" → {"category": "billing"}
Example 3: "API returns 500" → {"category": "technical"}""",
}
```

---

## XML vs JSON

### Overview

| Format | Role in Prompting |
|--------|------------------|
| **XML tags** | Structure prompt sections and delimit data |
| **JSON** | Define output schemas and structured responses |

These are not alternatives — they serve different purposes. XML structures the prompt input; JSON structures the model output.

### Comparison Table

| Dimension | XML (in prompts) | JSON (for outputs) |
|-----------|-----------------|-------------------|
| **Purpose** | Section delimitation, data wrapping | Structured output, parsing |
| **Readability** | High — clear section boundaries | Moderate — nested structures |
| **Model compliance** | High — models handle XML tags well | High with `json_object` mode |
| **Parsing** | Regex or XML parser | `json.loads()` / Pydantic |
| **Security** | Risk of delimiter escape attacks | Risk of malformed JSON |
| **Token efficiency** | Moderate — tags add overhead | Efficient for flat structures |
| **Nesting** | Good for hierarchical content | Good for typed data |
| **Best for** | Separating instructions from data | API responses, database writes |

### XML for Prompt Structure

| Use Case | XML Pattern |
|----------|------------|
| Separate instructions from data | `<instructions>` / `<data>` |
| Multi-document context | `<doc id="1">` / `<doc id="2">` |
| Conversation turns | `<user>` / `<assistant>` |
| RAG chunks | `<context source="...">` |

### JSON for Output Structure

| Use Case | JSON Pattern |
|----------|-------------|
| API response | `{"field": "value"}` |
| Classification | `{"category": "billing"}` |
| Extraction | `{"name": "...", "amount": 123}` |
| Agent action | `{"tool": "search", "args": {...}}` |

### When to Choose

```text
Use XML in prompts when:
  → Separating trusted instructions from untrusted data
  → Multiple data sections need clear boundaries
  → RAG context from multiple sources
  → Security: delimiter isolation (with random tokens)

Use JSON for outputs when:
  → Downstream code parses the response
  → Database writes or API calls depend on structure
  → Validation with Pydantic/Zod
  → Any machine-readable response
```

### Combined Pattern (Recommended)

```xml
<instructions>
  Extract invoice fields as JSON. Missing fields → null.
</instructions>

<document>
  {untrusted_user_content}
</document>
```

Expected output:

```json
{"invoice_number": "1234", "total": 500.00, "date": "2026-01-15"}
```

See [Prompt Security — Delimiter Attacks](prompt-security.md#delimiter-attacks) for secure delimiter patterns.

---

## Chain-of-Thought vs ReAct

### Overview

| Approach | Definition |
|----------|-----------|
| **Chain-of-Thought (CoT)** | Model reasons step-by-step in text before answering |
| **ReAct** | Model interleaves reasoning (Thought) with actions (Action/Observation) using tools |

### Comparison Table

| Dimension | Chain-of-Thought | ReAct |
|-----------|-----------------|-------|
| **Reasoning** | Internal text reasoning | Reasoning + external tool use |
| **Tool access** | None — pure text | API calls, search, code execution |
| **Output** | Final answer after reasoning | Answer after tool observations |
| **Latency** | 1 LLM call (longer output) | Multiple LLM calls (tool loop) |
| **Cost** | Moderate (longer output tokens) | Higher (multiple calls + tool costs) |
| **Accuracy on math/logic** | High | High (with calculator tools) |
| **Accuracy on factual** | Moderate (may hallucinate) | High (with search tools) |
| **Complexity** | Low — add "think step by step" | High — tool orchestration loop |
| **Reliability** | Moderate — reasoning may have errors | Higher — grounded in tool results |
| **Best for** | Analysis, classification reasoning | Agents, research, multi-step tasks |

### When to Choose

```text
Choose CoT when:
  → Task needs reasoning but no external data
  → Classification with explanation ("why this category")
  → Math/logic that model handles well
  → Single LLM call required (latency constraint)
  → Cost-sensitive

Choose ReAct when:
  → Task requires real-time data (search, APIs, DB)
  → Multi-step workflows with external actions
  → Factual accuracy is critical (ground in tools)
  → Building an agent, not a single-shot task
  → Tool results reduce hallucination
```

### Production Considerations

| Factor | CoT | ReAct |
|--------|-----|-------|
| Latency | 1 call, but long output | 3–10+ calls |
| Cost | Output token cost | Call cost + tool cost |
| Failure modes | Reasoning errors | Tool failures, loops, timeouts |
| Observability | Read reasoning in output | Trace tool calls |
| Testing | Eval final answer | Eval tool selection + final answer |

### Example

```python
# Chain-of-Thought
COT_PROMPT = """
Classify this support ticket. Think step by step:
1. Identify the main topic
2. Check for urgency signals
3. Determine category

Ticket: "My payment failed but I was still charged"

Step 1: ...
Step 2: ...
Step 3: ...

Final answer: {"category": "billing", "priority": "high"}
"""

# ReAct
REACT_PROMPT = """
Answer the user's question using available tools.

Question: "What's the status of order #12345?"

Thought: I need to look up the order status.
Action: lookup_order(order_id="12345")
Observation: {"status": "shipped", "tracking": "1Z999..."}
Thought: I have the information needed.
Answer: Your order #12345 has been shipped. Tracking: 1Z999...
"""
```

---

## ReAct vs Tree-of-Thought

### Overview

| Approach | Definition |
|----------|-----------|
| **ReAct** | Linear loop: think → act → observe → think → ... → answer |
| **Tree-of-Thought (ToT)** | Explore multiple reasoning branches, evaluate, prune, continue |

### Comparison Table

| Dimension | ReAct | Tree-of-Thought |
|-----------|-------|----------------|
| **Search strategy** | Single path (greedy) | Multi-path (branching) |
| **LLM calls** | 3–10 per task | 10–50+ per task |
| **Cost** | Moderate | High (3–10× ReAct) |
| **Latency** | Seconds | Minutes |
| **Solution quality** | Good for most tasks | Better for hard problems |
| **Implementation** | Tool loop | Branch generation + evaluation + pruning |
| **Failure recovery** | Retry or replan | Explore alternative branches |
| **Best for** | Production agents | Research, optimization, puzzles |
| **Production readiness** | High | Low — mostly experimental |

### When to Choose

```text
Choose ReAct when:
  → Building production agents
  → Task has clear sequential steps
  → Latency budget < 30 seconds
  → Cost per task < $0.10
  → 90%+ of tasks solvable with single path

Choose ToT when:
  → ReAct fails on complex planning tasks
  → Multiple valid approaches exist
  → Quality matters more than cost/latency
  → Offline/batch processing (not real-time)
  → Research or optimization problems
```

### Production Considerations

| Factor | ReAct | ToT |
|--------|-------|-----|
| Production use | Standard for agents | Rare — mostly research |
| Cost at scale | Manageable with routing | Prohibitive for high traffic |
| Complexity | Well-understood patterns | Custom implementation |
| Alternatives | ReAct + retry + human fallback | ReAct + stronger model |

> **Practical advice:** Start with ReAct. Escalate to ToT only when eval shows ReAct fails on > 10% of tasks AND the task justifies 5–10× cost increase. For most production systems, a stronger model with ReAct outperforms ToT with a weaker model.

---

## Chaining vs Single Prompt

### Overview

| Approach | Definition |
|----------|-----------|
| **Single prompt** | One LLM call handles the entire task |
| **Chaining** | Multiple LLM calls, each handling one step, output fed to next |

### Comparison Table

| Dimension | Single Prompt | Chaining |
|-----------|--------------|----------|
| **LLM calls** | 1 | 2–5+ |
| **Latency** | Lowest | Higher (sequential calls) |
| **Cost** | Lowest | Higher (multiple calls) |
| **Task complexity** | Simple to moderate | Moderate to complex |
| **Debuggability** | Hard — black box | Easy — inspect each step |
| **Error isolation** | All-or-nothing | Fail at specific step |
| **Prompt complexity** | High (many instructions) | Low per step (focused) |
| **Parallelization** | N/A | Some steps can parallelize |
| **Caching** | One cache key | Per-step caching |
| **Best for** | Classification, extraction | Multi-stage pipelines |

### When to Choose

```text
Choose SINGLE PROMPT when:
  → Task is atomic (classify, extract, summarize)
  → Latency SLO < 2 seconds
  → Cost per request matters
  → Task fits in one set of instructions

Choose CHAINING when:
  → Task has distinct stages (retrieve → analyze → format)
  → Different stages need different models
  → Debugging requires step visibility
  → Stages can be tested independently
  → Some stages are cacheable
```

### Common Chain Patterns

| Pattern | Steps | Example |
|---------|-------|---------|
| Extract → Validate | 2 | Extract JSON → validate with Pydantic |
| Classify → Route | 2 | Classify intent → route to specialist prompt |
| Retrieve → Generate | 2 | RAG retrieval → answer generation |
| Plan → Execute → Review | 3 | Plan steps → execute → self-review |
| Translate → Process → Translate | 3 | Translate to EN → process → translate back |

### Production Considerations

```python
# Single prompt — fast, simple
async def single_shot(document: str) -> dict:
  return await llm_call(SINGLE_PROMPT.format(document=document))


# Chain — debuggable, flexible
async def chained(document: str) -> dict:
  # Step 1: Extract (fast, cheap model)
  raw = await llm_call(EXTRACT_PROMPT.format(document=document), model="mini")

  # Step 2: Validate (no LLM — deterministic)
  validated = InvoiceSchema.model_validate_json(raw)

  # Step 3: Enrich (only if needed, expensive model)
  if validated.total is None:
    validated = await llm_call(ENRICH_PROMPT.format(document=document), model="standard")

  return validated.model_dump()
```

| Factor | Single | Chain |
|--------|--------|-------|
| Model routing | One model for all | Different models per step |
| Failure handling | Retry entire call | Retry failed step only |
| Testing | End-to-end eval | Per-step + end-to-end eval |
| Caching | Cache full response | Cache intermediate steps |

---

## Static vs Dynamic Prompts

### Overview

| Approach | Definition |
|----------|-----------|
| **Static** | Prompt text is fixed at deploy time |
| **Dynamic** | Prompt assembled at runtime from variables, context, and rules |

### Comparison Table

| Dimension | Static | Dynamic |
|-----------|--------|---------|
| **Content** | Fixed text | Template + runtime variables |
| **Caching** | Fully cacheable | Partial — static prefix cacheable |
| **Personalization** | None | User-specific, context-aware |
| **Complexity** | Low | Medium — template engine needed |
| **Testing** | Test once | Test across variable combinations |
| **Security** | Low risk | Injection risk via variables |
| **Use case** | Standard tasks | Personalized, context-dependent tasks |
| **Versioning** | Simple | Template version + variable schema |

### When to Choose

```text
Choose STATIC when:
  → Task is identical for all users
  → Maximum caching benefit needed
  → Simple deployment and testing
  → Classification with fixed categories

Choose DYNAMIC when:
  → User-specific context (name, plan, history)
  → RAG with retrieved documents
  → Multi-tenant with different rules per tenant
  → Language/locale-specific assembly
  → Conditional instructions based on input type
```

### Dynamic Prompt Assembly

```python
def assemble_dynamic_prompt(
  template: str,
  user: User,
  context: str,
  locale: str,
) -> str:
  return template.format(
    user_name=user.name,
    user_plan=user.plan,
    context=wrap_untrusted(context),
    language=locale,
    current_date=date.today().isoformat(),
    categories=get_categories_for_plan(user.plan),
  )
```

### Production Considerations

| Factor | Static | Dynamic |
|--------|--------|---------|
| Cache hit rate | ~100% for prefix | Depends on static portion ratio |
| Test matrix | 1 test | N tests across variable combos |
| Security | Minimal | Validate and sanitize all variables |
| Debugging | Easy | Log variable values (redacted) |

See [Production Prompt Engineering — Configuration](production-prompt-engineering.md#configuration-management).

---

## Template vs Generated Prompts

### Overview

| Approach | Definition |
|----------|-----------|
| **Template** | Human-written prompt with variable placeholders |
| **Generated** | LLM or algorithm creates the prompt automatically |

### Comparison Table

| Dimension | Template | Generated |
|-----------|----------|-----------|
| **Author** | Human engineer | LLM or optimization algorithm |
| **Quality control** | Human review + eval | Requires validation pipeline |
| **Iteration speed** | Manual — hours/days | Fast — minutes |
| **Predictability** | High | Variable |
| **Cost to create** | Engineer time | LLM API calls |
| **Maintenance** | Manual updates | May need regeneration |
| **Best for** | Production systems | Prompt optimization, DSPy |
| **Reliability** | High (when tested) | Moderate (needs verification) |

### When to Choose

```text
Choose TEMPLATE when:
  → Production system with reliability requirements
  → Task is well-understood
  → Human expertise available
  → Compliance/audit requires human authorship
  → Default for 95% of production use cases

Choose GENERATED when:
  → Exploring prompt space (research, optimization)
  → Using frameworks like DSPy for auto-optimization
  → Meta-prompting (LLM writes prompts for sub-tasks)
  → Rapid prototyping before human refinement
  → A/B testing many variants at scale
```

### Generated Prompt Workflow

```text
1. Human writes seed template
2. Optimization framework generates variants
3. Automated eval ranks variants
4. Human reviews top candidates
5. Winner becomes new template (human-edited)
6. Template deployed to production (no longer "generated")
```

### Production Considerations

| Factor | Template | Generated |
|--------|----------|-----------|
| Auditability | Full human trace | Requires generation log |
| Reproducibility | Git version | Seed + algorithm version |
| Trust | High | Requires validation gate |
| DSPy integration | Export as template | Native optimization |

```python
# Template (production)
TEMPLATE = "Classify as JSON: {categories}\n\nTicket: {ticket}"

# Generated (optimization phase only)
# DSPy or similar generates optimized prompt
optimized = dspy_optimizer.compile(classifier, trainset=golden_set)
# Export to template for production
production_prompt = export_to_template(optimized)
```

> **Production Standard:** Generated prompts are for optimization, not deployment. Always export to a human-reviewed template before production.

---

## Decision Flowchart

```text
START: What kind of task?
│
├─ Simple classification/extraction?
│   ├─ Yes → Zero-shot + JSON schema + temperature 0
│   └─ No ↓
│
├─ Needs external data/tools?
│   ├─ Yes → ReAct agent loop
│   └─ No ↓
│
├─ Needs multi-step reasoning?
│   ├─ Yes, latency-sensitive → CoT in single prompt
│   ├─ Yes, quality-critical → Chain (2-3 focused prompts)
│   └─ No ↓
│
├─ Needs user-specific context?
│   ├─ Yes → Dynamic template with variables
│   └─ No → Static prompt
│
└─ Output format?
    ├─ Machine-parseable → JSON output + structured mode
    └─ Human-readable → XML-structured prompt, free text output
```

---

## Interview Preparation

**Q: When do you use few-shot vs zero-shot prompting?**

> Zero-shot with JSON schema for most production tasks — cheaper, faster, easier to maintain. Few-shot only when zero-shot quality is below threshold and 1–3 curated examples provide measurable improvement. Never default to few-shot.

**Q: What is the difference between CoT and ReAct?**

> CoT is internal text reasoning in a single call — good for analysis and logic. ReAct interleaves reasoning with tool actions across multiple calls — good for agents needing real-time data. CoT is cheaper and simpler; ReAct is more capable but more complex.

**Q: When should you chain prompts vs use a single prompt?**

> Single prompt for atomic tasks with tight latency SLOs. Chain when task has distinct stages that benefit from different models, independent testing, or intermediate caching. Chain adds latency and cost but improves debuggability and reliability.

**Q: Should you use generated prompts in production?**

> No. Use generation for optimization (DSPy, meta-prompting), then export the winner as a human-reviewed template. Production requires auditability, reproducibility, and reliability that generated prompts don't guarantee without validation.

---

## Navigation

### Prerequisites

- Sections 1–12 of this handbook (prompt design fundamentals)

### — Prompt Engineering

| # | Topic | Document |
|---|-------|----------|
| 1 | Introduction to Prompt Engineering | [introduction-to-prompt-engineering.md](introduction-to-prompt-engineering.md) |
| 2 | Prompt Anatomy | [prompt-anatomy.md](prompt-anatomy.md) |
| 3 | Message Types | [message-types.md](message-types.md) |
| 4 | Prompt Design Principles | [prompt-design-principles.md](prompt-design-principles.md) |
| 5 | Prompt Patterns | [prompt-patterns.md](prompt-patterns.md) |
| 6 | Prompt Templates Guide | [prompt-templates-guide.md](prompt-templates-guide.md) |
| 7 | Structured Prompting | [structured-prompting.md](structured-prompting.md) |
| 8 | Prompting Strategies | [prompting-strategies.md](prompting-strategies.md) |
| 9 | Advanced Reasoning Strategies | [advanced-reasoning-strategies.md](advanced-reasoning-strategies.md) |
| 10 | Prompt Chaining | [prompt-chaining.md](prompt-chaining.md) |
| 11 | Prompt Lifecycle | [prompt-lifecycle.md](prompt-lifecycle.md) |
| 12 | Prompt Versioning | [prompt-versioning.md](prompt-versioning.md) |
| 13 | Prompt Testing | [prompt-testing.md](prompt-testing.md) |
| 14 | Prompt Evaluation | [prompt-evaluation.md](prompt-evaluation.md) |
| 15 | Prompt Optimization | [prompt-optimization.md](prompt-optimization.md) |
| 16 | Prompt Security | [prompt-security.md](prompt-security.md) |
| 17 | Prompt Engineering Mistakes | [prompt-engineering-mistakes.md](prompt-engineering-mistakes.md) |
| 18 | Production Prompt Engineering | [production-prompt-engineering.md](production-prompt-engineering.md) |
| — | Comparison Guides (supplementary) | **You are here** |

### Related Topics

- [Function Calling and Tools](../llm-engineering/function-calling-and-tools.md) — ReAct implementation
- [Structured Outputs](../llm-engineering/structured-outputs.md) — JSON output mode
- [Prompt Optimization](prompt-optimization.md) — token and cost tradeoffs

---

## See Also

- [Prompt Optimization](prompt-optimization.md)
- [Structured Outputs](../llm-engineering/structured-outputs.md)
- [Function Calling and Tools](../llm-engineering/function-calling-and-tools.md)

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Initial release — supplementary comparison guide |
