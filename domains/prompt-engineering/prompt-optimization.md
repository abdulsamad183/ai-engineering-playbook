---
title: "Prompt Optimization"
description: "Production guide to prompt optimization — reducing tokens and latency, improving consistency, reducing hallucinations, strengthening structure, lowering cost, managing variables, and building modular prompts."
domain: prompt-engineering
tags: [prompt, optimization, production, intermediate, cost, latency]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - prompt-evaluation.md
  - prompt-testing.md
  - ../llm-engineering/llm-cost-optimization.md
  - ../llm-engineering/llm-performance-optimization.md
keywords: [prompt optimization, token reduction, modular prompts, hallucination reduction, prompt structure]
author: hp
---

# Prompt Optimization

> Section 15 of this handbook — prompt optimization is not about writing shorter prompts for aesthetics. It is about systematically improving the quality-cost-latency triangle: better outputs, fewer tokens, faster responses, and lower spend — without sacrificing reliability.

## Table of Contents

- [Optimization Framework](#optimization-framework)
- [Reducing Tokens](#reducing-tokens)
- [Reducing Latency](#reducing-latency)
- [Improving Consistency](#improving-consistency)
- [Reducing Hallucinations](#reducing-hallucinations)
- [Improving Structure](#improving-structure)
- [Reducing Cost](#reducing-cost)
- [Managing Variables](#managing-variables)
- [Modular Prompts](#modular-prompts)
- [Optimization Workflow](#optimization-workflow)
- [Optimization Checklist](#optimization-checklist)
- [Common Mistakes](#common-mistakes)
- [Interview Preparation](#interview-preparation)
- [Navigation](#navigation)

---

## Optimization Framework

Optimize prompts using measured iteration, not intuition.

```text
Baseline → Identify bottleneck → Hypothesize → Change one variable → Evaluate → Ship or revert
```

| Optimization Target | Primary Lever | Measurement |
|--------------------|---------------|-------------|
| Tokens | Prompt compression, modularization | Token count per request |
| Latency | Shorter prompts, caching, model routing | P95 TTFT + total latency |
| Consistency | Temperature, schema, explicit format | Multi-run variance |
| Hallucinations | Grounding instructions, abstention | Faithfulness score |
| Structure | Delimiters, sections, output schema | Parse success rate |
| Cost | All above + model selection | Cost per 1K requests |

> **Production Standard:** Change one variable per experiment. Measure on golden dataset before and after. Never ship optimization that trades > 2% quality for cost savings without explicit approval.

---

## Reducing Tokens

Token reduction is the highest-leverage optimization — it cuts input cost, output cost, and latency simultaneously.

### Token Audit Process

```python
def audit_prompt_tokens(prompt_template: str, sample_variables: dict) -> dict:
  rendered = prompt_template.format(**sample_variables)
  enc = tiktoken.encoding_for_model("gpt-4")
  tokens = enc.encode(rendered)

  sections = parse_sections(rendered)  # split by headers/delimiters
  section_tokens = {s.name: len(enc.encode(s.content)) for s in sections}

  return {
    "total": len(tokens),
    "sections": section_tokens,
    "largest_section": max(section_tokens, key=section_tokens.get),
    "recommendations": generate_recommendations(section_tokens),
  }
```

### Compression Techniques

| Technique | Typical Savings | Risk |
|-----------|----------------|------|
| Remove redundant instructions | 10–30% | Low |
| Replace few-shot with schema | 20–60% | Medium — test quality |
| Abbreviate internal labels | 5–15% | Low for non-user-facing |
| Summarize examples | 30–50% | Medium |
| Remove low-value examples | 20–40% | Medium — eval each example |
| Externalize static content to cache | 0% tokens, latency ↓ | Low |

### Before and After

```python
# BEFORE — 650 tokens
BLOATED = """
You are a helpful assistant. You should always be polite and professional.
When extracting data from invoices, please make sure to carefully read the
entire document and extract all relevant fields. If you are unsure about
a field, you can leave it as null. Please format your response as JSON.

Here are some examples of how to extract invoice data:

Example 1:
Input: "Invoice #1234 from Acme Corp dated Jan 15, 2026. Total: $500."
Output: {"invoice_number": "1234", "vendor": "Acme Corp", ...}

Example 2:
[... 400 more tokens of examples ...]
"""

# AFTER — 120 tokens
FOCUSED = """
Extract invoice fields as JSON matching the schema below.
Missing fields → null. No commentary.

Schema: {schema}
"""
```

### Token Budget Allocation

| Segment | Budget (% of context) | Optimization Priority |
|---------|----------------------|----------------------|
| System instructions | 5–15% | High — often bloated |
| Few-shot examples | 10–40% | High — often over-provided |
| RAG context | 40–70% | Medium — rerank, don't truncate blindly |
| User input | Variable | Low — don't compress user data |
| Reserved for output | 10–20% | Set via `max_tokens` |

---

## Reducing Latency

Latency optimization targets the prefill and generation phases.

### Latency Optimization Levers

| Lever | Impact | Effort |
|-------|--------|--------|
| Shorter input prompts | High (prefill) | Low |
| Prompt caching (static prefix) | High (prefill) | Medium |
| Lower `max_tokens` | Medium (generation) | Low |
| Smaller model for simple tasks | High (both) | Medium |
| Streaming | Perceived latency ↓ | Low |
| Parallel tool calls | Wall-clock ↓ | Medium |
| Remove unnecessary few-shot | High (prefill) | Low |

### Prompt Caching Strategy

```python
def build_cached_messages(system_prompt: str, dynamic_context: str, user_input: str) -> list:
  """Static prefix cached; dynamic suffix computed fresh."""
  return [
    {"role": "system", "content": system_prompt},       # CACHED — stable across requests
    {"role": "user", "content": f"<context>{dynamic_context}</context>\n\n{user_input}"},
  ]
```

Place stable content first (system prompt, tool definitions, few-shot examples). Append dynamic content (RAG chunks, user input) last.

### Latency-Aware Prompt Design

```text
# Slow — model generates verbose reasoning before answer
"Think step by step about each field, explain your reasoning, then extract."

# Fast — direct extraction
"Extract fields as JSON. Missing → null."
```

For tasks that need reasoning, use a two-stage approach: reason in stage 1 (can be async), extract in stage 2 (fast).

---

## Improving Consistency

Consistency optimization reduces output variance without sacrificing quality.

### Consistency Techniques

| Technique | Mechanism |
|-----------|-----------|
| `temperature=0.0` | Greedy decoding |
| Structured output / JSON schema | Constrains format |
| Explicit format examples | Reduces ambiguity |
| Enum constraints | Limits valid values |
| Deterministic field ordering | "Return fields in this order: ..." |
| Post-processing normalization | Sort keys, strip whitespace |

### Format Locking

```python
SYSTEM = """
Return ONLY valid JSON matching this schema. No markdown fences. No preamble.

{
  "category": "<one of: billing, technical, account, other>",
  "priority": "<one of: low, medium, high, critical>",
  "summary": "<one sentence>"
}
"""

API_CONFIG = {
  "temperature": 0.0,
  "response_format": {"type": "json_object"},
  # or tool/schema mode for stricter enforcement
}
```

### Reducing Instruction Ambiguity

```text
# Ambiguous — model chooses interpretation
"Summarize the document appropriately."

# Explicit — model has one interpretation
"Summarize in exactly 3 bullet points. Each bullet ≤ 20 words.
Focus on: decisions made, action items, deadlines."
```

---

## Reducing Hallucinations

Hallucination optimization strengthens grounding and abstention behavior.

### Anti-Hallucination Prompt Patterns

| Pattern | Instruction | Effect |
|---------|------------|--------|
| Scope limitation | "Only use provided context" | Reduces fabrication |
| Abstention | "Say 'I don't know' if not in context" | Reduces confabulation |
| Citation requirement | "Quote the source for each claim" | Enables verification |
| Confidence gating | "Only state facts you can cite" | Reduces overconfidence |
| Negative examples | "Do NOT invent names, dates, or numbers" | Explicit prohibition |

### Layered Grounding

```python
def build_grounded_prompt(context: str, question: str) -> list[dict]:
  return [
    {
      "role": "system",
      "content": (
        "Answer ONLY using the context below. "
        "If the context does not contain the answer, respond: "
        '{"answer": null, "reason": "not_in_context"}. '
        "Never use outside knowledge."
      ),
    },
    {
      "role": "user",
      "content": f"<context>\n{context}\n</context>\n\n<question>\n{question}\n</question>",
    },
  ]
```

### Hallucination Optimization Workflow

1. Measure baseline hallucination rate on golden set
2. Add grounding instruction → measure
3. Add abstention instruction → measure
4. Add citation requirement → measure
5. Add post-processing validation → measure
6. Stop when rate meets target; don't over-constrain (may cause refusals)

---

## Improving Structure

Structured prompts produce more parseable, consistent outputs.

### Structural Patterns

| Pattern | Use Case | Example |
|---------|----------|---------|
| XML tags | Clear section boundaries | `<context>...</context>` |
| Markdown headers | Human-readable sections | `## Instructions`, `## Examples` |
| Numbered steps | Sequential tasks | `1. Read 2. Extract 3. Format` |
| Role blocks | Multi-role prompts | `System: ... User: ...` |
| JSON schema | Output structure | `response_format` or inline schema |

### Optimal Structure Template

```xml
<system>
  <role>You are an invoice data extractor.</role>
  <rules>
    <rule>Return JSON only</rule>
    <rule>Missing fields → null</rule>
    <rule>Do not invent data</rule>
  </rules>
  <output_schema>{schema}</output_schema>
</system>

<user>
  <document>{document_text}</document>
</user>
```

### Structure Optimization Rules

1. **Most important instructions first** — models attend more to early context
2. **Separate instructions from data** — use delimiters to prevent confusion
3. **One task per prompt** — multi-task prompts degrade all tasks
4. **Explicit output format** — never assume the model knows your schema
5. **Consistent delimiter style** — don't mix XML and markdown arbitrarily

See [Prompt Comparison Guides](prompt-comparison-guides.md) for XML vs JSON format decisions.

---

## Reducing Cost

Cost optimization combines token reduction, model selection, and infrastructure strategies.

### Cost Optimization Hierarchy

```text
1. Fix prompt bloat (highest ROI)
2. Right-size model for task
3. Enable prompt caching
4. Reduce output tokens (max_tokens, concise instructions)
5. Batch non-real-time workloads
```

### Cost Impact Calculator

```python
def optimization_roi(
  current_tokens: int,
  optimized_tokens: int,
  requests_per_day: int,
  input_rate_per_m: float = 0.40,
) -> dict:
  daily_savings = (current_tokens - optimized_tokens) * requests_per_day * input_rate_per_m / 1_000_000
  return {
    "token_reduction_pct": (current_tokens - optimized_tokens) / current_tokens,
    "daily_savings_usd": daily_savings,
    "monthly_savings_usd": daily_savings * 30,
  }
```

### Model Tier Optimization

| Task Complexity | Model Tier | Cost Multiplier |
|----------------|-----------|-----------------|
| Classification, routing | Nano/mini | 1× |
| Extraction, summarization | Mini/small | 3–5× |
| Complex reasoning | Standard | 10–15× |
| Agent planning | Reasoning tier | 20–50× |

Route by task, not by default. See [Model Comparison Guide](../llm-engineering/model-comparison-guide.md).

---

## Managing Variables

Variables make prompts dynamic but introduce complexity and injection risk.

### Variable Design Principles

| Principle | Rationale |
|-----------|-----------|
| Minimal variables | Each variable is a failure point |
| Type and validate | Pydantic models for all inputs |
| Default values | Graceful handling of missing data |
| Sanitize user-provided | Prevent injection via variables |
| Document each variable | Name, type, source, example |

### Variable Template Pattern

```python
from pydantic import BaseModel, Field


class InvoicePromptVars(BaseModel):
  document_text: str = Field(max_length=50_000)
  schema: str = Field(description="JSON schema for output")
  language: str = Field(default="en", pattern="^[a-z]{2}$")


PROMPT_TEMPLATE = """
Extract invoice data from the document below.
Return JSON matching the schema. Language: {language}.

<schema>{schema}</schema>

<document>
{document_text}
</document>
"""


def render_prompt(vars: InvoicePromptVars) -> str:
  validated = InvoicePromptVars.model_validate(vars)
  return PROMPT_TEMPLATE.format(**validated.model_dump())
```

### Variable Injection Prevention

```python
def safe_format(template: str, variables: dict) -> str:
  """Prevent format string injection and escape user content."""
  for key, value in variables.items():
    if not isinstance(value, str):
      value = str(value)
    variables[key] = value.replace("{", "{{").replace("}", "}}")
  return template.format(**variables)
```

---

## Modular Prompts

Modular prompts decompose monolithic instructions into composable, reusable components.

### Why Modularize

| Benefit | Explanation |
|---------|-------------|
| Reuse | Share role definitions across prompts |
| Testability | Test each module independently |
| Versioning | Update one module without touching others |
| A/B testing | Swap modules to compare variants |
| Localization | Translate modules independently |

### Module Architecture

```text
prompts/
├── modules/
│   ├── roles/
│   │   ├── data_extractor.md
│   │   ├── support_agent.md
│   │   └── code_reviewer.md
│   ├── rules/
│   │   ├── json_only.md
│   │   ├── grounding.md
│   │   └── abstention.md
│   ├── formats/
│   │   ├── invoice_schema.json
│   │   └── triage_schema.json
│   └── examples/
│       ├── invoice_few_shot.md
│       └── triage_few_shot.md
├── composed/
│   ├── invoice_extraction_v2.md  # assembled from modules
│   └── support_triage_v1.md
└── assembler.py
```

### Prompt Assembler

```python
from pathlib import Path


class PromptAssembler:
  def __init__(self, modules_dir: Path):
    self.modules_dir = modules_dir

  def load_module(self, category: str, name: str) -> str:
    path = self.modules_dir / category / f"{name}.md"
    return path.read_text()

  def compose(self, config: dict) -> str:
    sections = []
    for module_ref in config["modules"]:
      content = self.load_module(module_ref["category"], module_ref["name"])
      sections.append(content)
    return "\n\n".join(sections)


# Usage
config = {
  "modules": [
    {"category": "roles", "name": "data_extractor"},
    {"category": "rules", "name": "json_only"},
    {"category": "rules", "name": "grounding"},
    {"category": "formats", "name": "invoice_schema"},
  ]
}
prompt = assembler.compose(config)
```

### Composition Patterns

| Pattern | Modules Combined | Use Case |
|---------|-----------------|----------|
| Role + Rules + Format | extractor + json_only + schema | Structured extraction |
| Role + Rules + Examples | support + grounding + few_shot | Classification |
| Role + Rules + Context | agent + tool_usage + dynamic | Agent prompts |
| Base + Overlay | core_rules + domain_specific | Multi-domain from shared base |

### Module Versioning

```yaml
# modules/manifest.yaml
modules:
  roles/data_extractor:
    version: "1.2.0"
    hash: "a3f8c2..."
  rules/grounding:
    version: "2.0.0"
    hash: "b7d1e4..."

compositions:
  invoice_extraction_v2:
    modules:
      - roles/data_extractor@1.2.0
      - rules/json_only@1.0.0
      - rules/grounding@2.0.0
    composed_hash: "c9e2f1..."
```

---

## Optimization Workflow

### Step-by-Step Process

```text
1. BASELINE
   Run eval pipeline on current prompt → record all metrics

2. IDENTIFY BOTTLENECK
   Which dimension is worst? Quality? Cost? Latency? Consistency?

3. HYPOTHESIZE
   "Removing 3 few-shot examples will cut tokens 40% with < 1% quality loss"

4. EXPERIMENT
   Change ONE variable → run eval → compare to baseline

5. DECIDE
   Quality within threshold? → Ship
   Quality regressed? → Revert or iterate

6. DOCUMENT
   Log change, metrics delta, decision rationale
```

### Experiment Log Template

```markdown
## Experiment: PE-2026-0042

**Prompt:** invoice-extraction
**Hypothesis:** Remove few-shot examples; rely on JSON schema
**Changed:** Removed 3 examples (480 tokens)

| Metric | Before | After | Delta |
|--------|--------|-------|-------|
| Quality | 4.3 | 4.1 | -0.2 |
| F1 | 0.94 | 0.93 | -0.01 |
| Avg tokens | 820 | 340 | -58% |
| P95 latency | 1200ms | 680ms | -43% |
| Cost/1K | $1.40 | $0.58 | -59% |

**Decision:** SHIP — quality within 2% threshold; massive cost/latency win
```

---

## Optimization Checklist

- [ ] Baseline metrics recorded before any changes
- [ ] Token audit completed with section breakdown
- [ ] One variable changed per experiment
- [ ] Quality evaluated on golden set after each change
- [ ] Static prompt prefix eligible for caching
- [ ] Temperature and schema configured for consistency
- [ ] Grounding and abstention instructions for RAG prompts
- [ ] Variables validated and sanitized
- [ ] Modular architecture for reusable components
- [ ] Experiment log with before/after metrics

---

## Common Mistakes

| Mistake | Consequence | Fix |
|---------|-------------|-----|
| Optimize without measuring | Break quality silently | Baseline first, eval after |
| Change multiple variables | Can't attribute results | One change per experiment |
| Over-compress prompts | Quality collapse | Find minimum viable prompt via eval |
| Remove all examples blindly | Format inconsistency | Test zero-shot vs few-shot |
| Monolithic prompts | Hard to maintain and test | Modularize |
| Ignore caching placement | Miss latency wins | Static content first |

---

## Interview Preparation

**Q: How do you optimize a prompt for production?**

> Measure baseline on golden set. Token audit to find bloat. Change one variable, re-evaluate. Prioritize: remove redundancy, enable caching, add schema constraints, right-size model. Never ship without quality regression check.

**Q: What is a modular prompt architecture?**

> Decompose prompts into reusable modules (roles, rules, formats, examples). Compose per task via assembler. Enables independent testing, versioning, A/B testing, and localization without duplicating content.

**Q: How do you reduce hallucinations through prompt design?**

> Scope limitation, abstention instructions, citation requirements, negative examples, structured output for "I don't know" responses. Measure faithfulness before and after each addition.

---

## Navigation

### Prerequisites

- [Prompt Evaluation](prompt-evaluation.md) — Section 14
- [Prompt Testing](prompt-testing.md) — Section 13

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
| 15 | Prompt Optimization | **You are here** |
| 16 | Prompt Security | [prompt-security.md](prompt-security.md) |
| 17 | Prompt Engineering Mistakes | [prompt-engineering-mistakes.md](prompt-engineering-mistakes.md) |
| 18 | Production Prompt Engineering | [production-prompt-engineering.md](production-prompt-engineering.md) |
| — | Comparison Guides (supplementary) | [prompt-comparison-guides.md](prompt-comparison-guides.md) |

### Related Topics

- [LLM Cost Optimization](../llm-engineering/llm-cost-optimization.md)
- [LLM Performance Optimization](../llm-engineering/llm-performance-optimization.md)

### Next Topics

- [Prompt Security](prompt-security.md) — secure optimized prompts
- [Production Prompt Engineering](production-prompt-engineering.md) — deploy and manage

---

## See Also

- [Prompt Evaluation](prompt-evaluation.md)
- [LLM Cost Optimization](../llm-engineering/llm-cost-optimization.md)
- [Prompt Comparison Guides](prompt-comparison-guides.md)

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Initial release — Section 15 |
