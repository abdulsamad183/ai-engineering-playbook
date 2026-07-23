---
title: "Prompt Engineering Mistakes"
description: "Production reference for prompt engineering mistakes — vague prompts, conflicting instructions, missing or excessive context, duplication, poor examples, inconsistent formatting, weak constraints, prompt drift, and brittle prompts. Symptoms, root causes, diagnostics, fixes, and prevention for each."
domain: prompt-engineering
tags: [prompt, debugging, production, intermediate, mistakes]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - prompt-optimization.md
  - prompt-testing.md
  - prompt-evaluation.md
  - ../llm-engineering/llm-engineering-mistakes.md
keywords: [prompt mistakes, vague prompts, prompt drift, brittle prompts, few-shot errors, prompt debugging]
author: hp
---

# Prompt Engineering Mistakes

> Section 17 of this handbook — the gap between a clever prompt demo and a production prompt system is a graveyard of predictable mistakes. This document catalogs the prompt failures that recur across teams, with symptoms, root causes, diagnostics, fixes, and prevention for each.

## Table of Contents

- [How to Use This Guide](#how-to-use-this-guide)
- [Mistake Severity Matrix](#mistake-severity-matrix)
- [1. Vague Prompts](#1-vague-prompts)
- [2. Conflicting Instructions](#2-conflicting-instructions)
- [3. Missing Context](#3-missing-context)
- [4. Excessive Context](#4-excessive-context)
- [5. Duplication](#5-duplication)
- [6. Poor Examples](#6-poor-examples)
- [7. Inconsistent Formatting](#7-inconsistent-formatting)
- [8. Weak Constraints](#8-weak-constraints)
- [9. Prompt Drift](#9-prompt-drift)
- [10. Brittle Prompts](#10-brittle-prompts)
- [11. No Versioning or Testing](#11-no-versioning-or-testing)
- [12. Ignoring Model Differences](#12-ignoring-model-differences)
- [Pre-Production Checklist](#pre-production-checklist)
- [Interview Preparation](#interview-preparation)
- [Navigation](#navigation)

---

## How to Use This Guide

Each mistake follows a consistent diagnostic framework:

| Section | Purpose |
|---------|---------|
| **Symptoms** | What you observe in outputs, logs, or user reports |
| **Root Cause** | Why the mistake happens — the design failure, not the model |
| **Diagnose** | How to confirm this is the problem |
| **Fix** | Concrete remediation steps |
| **Prevention** | Practices that stop recurrence |

Cross-references point to detailed guides in this handbook.

> **Production Standard:** When a prompt fails in production, check this list before blaming the model. Most prompt incidents are design failures, not capability limits.

---

## Mistake Severity Matrix

| Mistake | User Impact | Cost Risk | Reliability Risk | Security Risk |
|---------|------------|-----------|-----------------|---------------|
| Vague prompts | High | Medium | **Critical** | Low |
| Conflicting instructions | High | Low | **Critical** | Medium |
| Missing context | **Critical** | Low | **Critical** | Low |
| Excessive context | Medium | **Critical** | High | Medium |
| Duplication | Low | **Critical** | Medium | Low |
| Poor examples | High | High | **Critical** | Low |
| Inconsistent formatting | Medium | Medium | **Critical** | Low |
| Weak constraints | High | Medium | **Critical** | High |
| Prompt drift | High | Medium | **Critical** | Medium |
| Brittle prompts | **Critical** | Medium | **Critical** | Medium |
| No versioning/testing | Medium | High | **Critical** | High |
| Ignoring model differences | High | High | **Critical** | Low |

---

## 1. Vague Prompts

### Symptoms

- Outputs vary wildly across similar inputs
- Model asks clarifying questions instead of completing the task
- Users report "the AI doesn't understand what I want"
- Quality scores have high variance (std dev > 1.0 on 5-point scale)
- Different team members get different results from the "same" prompt

### Root Cause

Instructions lack specificity about task, format, scope, and success criteria. The model fills ambiguity with its own assumptions, which vary by input and run.

### Diagnose

```python
VAGUENESS_CHECKLIST = [
  "Is the task verb specific? ('analyze' vs 'extract fields X, Y, Z as JSON')",
  "Is the output format defined? (free text vs schema)",
  "Are scope boundaries stated? (what to include AND exclude)",
  "Are edge cases addressed? (empty input, missing data)",
  "Is there a measurable success criterion?",
]

def audit_prompt_vagueness(prompt_text: str) -> list[str]:
  issues = []
  vague_verbs = ["analyze", "process", "handle", "help with", "look at", "deal with"]
  for verb in vague_verbs:
    if verb in prompt_text.lower():
      issues.append(f"Vague verb detected: '{verb}'")
  if "json" not in prompt_text.lower() and "format" not in prompt_text.lower():
    issues.append("No output format specified")
  if "only" not in prompt_text.lower() and "do not" not in prompt_text.lower():
    issues.append("No scope boundaries defined")
  return issues
```

Run the prompt on 10 similar inputs. If outputs differ structurally (not just in content), vagueness is likely.

### Fix

```python
# BEFORE — vague
VAGUE = "Analyze the customer feedback and provide insights."

# AFTER — specific
SPECIFIC = """
Classify the customer feedback into exactly one category:
  billing | technical | account | product | other

Return JSON:
{
  "category": "<category>",
  "sentiment": "<positive|neutral|negative>",
  "summary": "<one sentence, max 30 words>",
  "requires_escalation": <true|false>
}

Rules:
- requires_escalation = true if sentiment is negative AND category is billing or account
- If feedback is empty, return {"category": "other", "sentiment": "neutral", "summary": "Empty feedback", "requires_escalation": false}
"""
```

1. Replace vague verbs with specific actions
2. Define exact output format with schema
3. Add explicit scope boundaries (include/exclude)
4. Handle edge cases in the prompt itself
5. Add measurable criteria ("exactly 3 bullet points, each ≤ 20 words")

### Prevention

- Use a prompt review checklist before every deploy
- Require output schema for all structured tasks
- Peer review prompts like code reviews
- Test with edge cases during design, not after incidents

---

## 2. Conflicting Instructions

### Symptoms

- Model follows some instructions but ignores others unpredictably
- Output satisfies one rule while violating another
- Behavior changes depending on input phrasing (model "chooses" which rule to follow)
- Inconsistent handling of the same edge case across runs
- Reviewers disagree on whether output is correct

### Root Cause

Multiple instructions contradict each other, or system and user messages give opposing directives. The model has no deterministic way to resolve conflicts, so it arbitrarily prioritizes one instruction.

### Diagnose

```python
def find_conflicts(prompt_text: str) -> list[str]:
  conflicts = []
  pairs = [
    ("be concise", "be thorough"),
    ("be creative", "follow the format exactly"),
    ("use only provided context", "use your knowledge"),
    ("always answer", "say I don't know if unsure"),
    ("be friendly and casual", "be professional and formal"),
    ("include all details", "keep response under 100 words"),
    ("never refuse", "decline if out of scope"),
  ]
  lower = prompt_text.lower()
  for a, b in pairs:
    if a in lower and b in lower:
      conflicts.append(f"Conflict: '{a}' vs '{b}'")
  return conflicts
```

Review system prompt, user template, few-shot examples, and tool descriptions for contradictions.

### Fix

1. **Audit all instruction sources** — system, user template, examples, tool descriptions
2. **Establish priority hierarchy** — "If rules conflict, priority is: safety > format > style"
3. **Remove contradictions** — don't say "be concise" and "explain thoroughly"
4. **Align examples with rules** — examples must demonstrate all stated rules simultaneously

```python
# BEFORE — conflicting
CONFLICTING = """
Be concise — keep responses under 50 words.
Provide thorough analysis with supporting evidence for each point.
Always answer the question completely.
"""

# AFTER — resolved
RESOLVED = """
Provide analysis in exactly 3 bullet points.
Each bullet: one finding + one supporting data point. Max 25 words per bullet.
If you cannot answer from the provided context, respond:
{"answer": null, "reason": "insufficient_context"}
"""
```

### Prevention

- Single source of truth for instructions (no duplication across layers)
- Explicit conflict resolution rule in system prompt
- Automated conflict detection in CI
- Review examples against stated rules

---

## 3. Missing Context

### Symptoms

- Model hallucinates facts not in the source material
- Outputs are technically correct but useless ("I don't have enough information" on every query)
- Model makes wrong assumptions about domain-specific terms
- Classification categories don't match your business taxonomy
- Outputs use generic knowledge instead of company-specific rules

### Root Cause

The prompt assumes the model knows domain context, business rules, or terminology that was never provided. LLMs have general knowledge but not your specific business logic.

### Diagnose

Ask: "Could someone outside our team complete this task with only the prompt text?"

| Missing Context Type | Test |
|---------------------|------|
| Domain terminology | Does prompt define key terms? |
| Business rules | Are decision criteria explicit? |
| Output taxonomy | Are categories/enums listed? |
| Data format | Is input format explained? |
| User persona | Is the audience specified? |

```python
# Test: remove all context and see if prompt still makes sense
def test_context_completeness(prompt: str, required_context: list[str]) -> dict:
  missing = [ctx for ctx in required_context if ctx.lower() not in prompt.lower()]
  return {"complete": len(missing) == 0, "missing": missing}

result = test_context_completeness(prompt, [
  "billing", "escalation criteria", "category definitions", "company name"
])
```

### Fix

1. **Add domain glossary** — define terms the model must use correctly
2. **Include business rules** — explicit decision criteria
3. **Provide taxonomy** — list valid categories, statuses, enums
4. **Add input format description** — explain what the input contains
5. **Inject dynamic context** — RAG, user profile, session data

```python
# BEFORE — missing context
MISSING = "Classify the support ticket."

# AFTER — context provided
COMPLETE = """
Classify the support ticket into one of these categories:
- billing: payment, invoice, subscription, refund issues
- technical: bugs, errors, integration problems
- account: login, password, profile, permissions
- product: feature requests, how-to questions
- other: anything not matching above

Escalation rules:
- billing + negative sentiment → requires_escalation: true
- technical + contains "data loss" or "security" → requires_escalation: true
- All others → requires_escalation: false

Company: Acme Corp (SaaS project management tool)
"""
```

### Prevention

- Context completeness checklist in prompt review
- New team members review prompts (they spot missing context)
- Test with inputs from unfamiliar domains
- Document assumed knowledge explicitly

---

## 4. Excessive Context

### Symptoms

- High token costs with no quality improvement
- Latency increases linearly with prompt size
- Model ignores instructions buried in long context ("lost in the middle")
- Quality degrades when context exceeds ~4K tokens
- Important instructions at the end of long prompts are ignored

### Root Cause

Prompt includes unnecessary examples, redundant instructions, full documents when summaries suffice, or entire conversation histories. More context is assumed to be better.

### Diagnose

```python
def audit_context_bloat(prompt: str) -> dict:
  enc = tiktoken.encoding_for_model("gpt-4")
  tokens = len(enc.encode(prompt))
  sections = parse_sections(prompt)

  return {
    "total_tokens": tokens,
    "sections": {s.name: len(enc.encode(s.content)) for s in sections},
    "recommendations": [],
    "bloat_score": "high" if tokens > 3000 else "medium" if tokens > 1500 else "low",
  }

# Compare quality with full vs reduced context
async def test_context_necessity(prompt_full, prompt_reduced, eval_set):
  full_score = await evaluate(prompt_full, eval_set)
  reduced_score = await evaluate(prompt_reduced, eval_set)
  return {
    "full_tokens": count_tokens(prompt_full),
    "reduced_tokens": count_tokens(prompt_reduced),
    "full_quality": full_score,
    "reduced_quality": reduced_score,
    "quality_delta": full_score - reduced_score,
    "verdict": "reduce" if abs(full_score - reduced_score) < 0.02 else "keep",
  }
```

### Fix

| Bloat Source | Reduction Strategy | Typical Savings |
|-------------|-------------------|-----------------|
| Too many few-shot examples | Keep 1–3 best; use schema instead | 40–70% |
| Redundant instructions | Deduplicate across system/user | 20–30% |
| Full documents | Summarize or extract relevant sections | 50–80% |
| Long conversation history | Sliding window or summarization | 60–90% |
| Verbose role descriptions | One sentence role definition | 30–50% |

```python
# BEFORE — 2,400 tokens
BLOATED = """
You are an expert data analyst with 20 years of experience in...
[500 tokens of role description]

Here are 8 examples of how to classify tickets:
[1,500 tokens of examples]

Now classify this ticket: {ticket}
"""

# AFTER — 280 tokens
FOCUSED = """
Classify the ticket as JSON: {"category": "<billing|technical|account|other>", "priority": "<low|medium|high>"}

Rules:
- billing + amount > $1000 → priority: high
- contains "urgent" or "down" → priority: high
- default → priority: medium

Ticket: {ticket}
"""
```

### Prevention

- Token budget per prompt (set maximum)
- Token audit in CI — alert on prompts > threshold
- A/B test context reduction before adding more
- "Lost in the middle" test — place critical instructions at start AND end

---

## 5. Duplication

### Symptoms

- Token costs higher than expected for prompt complexity
- Instructions appear in system prompt, user message, AND examples
- Changing one instruction requires updating multiple places
- Inconsistent behavior when duplicated instructions subtly differ
- Model follows the most recent duplicate, ignoring earlier versions

### Root Cause

Same instructions repeated across system prompt, user template, few-shot examples, tool descriptions, and middleware. Often accumulates as multiple engineers add instructions without checking existing content.

### Diagnose

```python
def find_duplication(system_prompt: str, user_template: str, examples: str) -> list[dict]:
  """Find semantically similar instructions across prompt layers."""
  all_text = [("system", system_prompt), ("user", user_template), ("examples", examples)]
  duplicates = []

  for i, (layer_a, text_a) in enumerate(all_text):
    for layer_b, text_b in all_text[i + 1:]:
      similarity = compute_semantic_similarity(text_a, text_b)
      if similarity > 0.7:
        duplicates.append({
          "layers": (layer_a, layer_b),
          "similarity": similarity,
          "recommendation": f"Keep in {layer_a}, remove from {layer_b}",
        })
  return duplicates
```

Manual check: search for key instruction phrases across all prompt layers.

### Fix

1. **Assign each instruction to one layer** — system for rules, user for data, examples for demonstrations
2. **Remove duplicates** — keep the most authoritative version
3. **Use modular prompts** — single source of truth per instruction

```python
# BEFORE — duplicated across layers
SYSTEM = "Return JSON only. No commentary. Extract invoice fields."
USER = "Please extract the invoice fields and return as JSON without any commentary."
EXAMPLE_OUTPUT = '{"note": "Remember to return JSON only with no commentary"}'

# AFTER — single source of truth
SYSTEM = "Extract invoice fields as JSON. No commentary."
USER = "<document>{document}</document>"
# Examples demonstrate format, don't repeat rules
```

### Instruction Layer Assignment

| Layer | Contains | Does NOT Contain |
|-------|----------|-----------------|
| System | Rules, format, constraints | User data, examples |
| User template | Data, query | Rules (reference system) |
| Examples | Input/output demonstrations | Repeated rules |
| Tool descriptions | Tool-specific params | General task rules |

### Prevention

- Modular prompt architecture with shared rule modules
- Automated duplication detection in CI
- Prompt review checklist includes "no duplicated instructions"
- Single owner per prompt to prevent accumulation

---

## 6. Poor Examples

### Symptoms

- Model output format doesn't match expectations despite clear instructions
- Few-shot examples demonstrate wrong behavior (model copies mistakes)
- Examples are too similar — model fails on inputs unlike examples
- Examples contradict stated rules
- Adding more examples doesn't improve quality

### Root Cause

Few-shot examples are low quality, unrepresentative, inconsistent with rules, or poorly selected. The model learns from examples more strongly than from instructions in many cases.

### Diagnose

```python
def audit_examples(examples: list[dict], rules: str) -> list[str]:
  issues = []
  for i, ex in enumerate(examples):
    if not valid_json(ex.get("output", "")):
      issues.append(f"Example {i}: output is not valid JSON")
    if "no commentary" in rules.lower() and len(ex["output"]) > len(ex["input"]) * 2:
      issues.append(f"Example {i}: output too verbose for 'no commentary' rule")
  input_types = set(classify_input(ex["input"]) for ex in examples)
  if len(input_types) < len(examples) * 0.5:
    issues.append("Examples lack diversity — too many similar input types")
  return issues
```

Test: remove all examples and compare quality. If quality improves, examples are hurting.

### Fix

1. **Curate, don't accumulate** — 1–3 excellent examples beat 8 mediocre ones
2. **Examples must follow ALL stated rules** — if rules say "no commentary," examples must have no commentary
3. **Cover diverse input types** — edge cases, not just happy paths
4. **Match example difficulty to production** — don't only show easy cases
5. **Consider zero-shot + schema** — often outperforms poor few-shot

```python
# BEFORE — poor examples
POOR_EXAMPLES = """
Example 1:
Input: "Invoice #123"
Output: Sure! Here's the extracted data: {"invoice_number": "123"}
Note: I wasn't able to find the total.

Example 2:
Input: "Invoice #456, Total: $100"
Output: {"invoice_number": "456", "total": 100, "extra_field": "guessed"}
"""

# AFTER — clean examples (or remove and use schema)
GOOD_EXAMPLES = """
Example 1:
Input: "Invoice #123, Date: 2026-01-15"
Output: {"invoice_number": "123", "date": "2026-01-15", "total": null}

Example 2:
Input: "Invoice #456, Total: $100.00"
Output: {"invoice_number": "456", "date": null, "total": 100.00}
"""
```

### Example Selection Framework

| Criterion | Good Example | Bad Example |
|-----------|-------------|-------------|
| Rule compliance | Follows every stated rule | Violates "no commentary" rule |
| Format | Exact output schema match | Extra fields, wrong types |
| Diversity | Different input patterns | 3 nearly identical inputs |
| Edge cases | Includes null/missing fields | Only complete, easy inputs |
| Count | 1–3 targeted examples | 8+ bloated examples |

### Prevention

- Evaluate each example's contribution (remove one at a time, measure impact)
- Peer review examples against rules checklist
- Prefer JSON schema over few-shot when possible
- Update examples when rules change

---

## 7. Inconsistent Formatting

### Symptoms

- Output sometimes JSON, sometimes markdown, sometimes plain text
- Parsing failures in downstream code
- Model mixes XML tags, markdown headers, and plain text in same response
- Field names vary (`invoice_number` vs `invoiceNumber` vs `Invoice Number`)
- Intermittent markdown fences around JSON (` ```json ... ``` `)

### Root Cause

Prompt uses mixed formatting conventions, doesn't specify output format strictly enough, or examples demonstrate inconsistent formats. Different prompt sections use different delimiter styles.

### Diagnose

```python
async def test_format_consistency(prompt, test_inputs: list, n_runs: int = 5) -> dict:
  formats_seen = set()
  parse_failures = 0

  for input_data in test_inputs:
    for _ in range(n_runs):
      output = await invoke(prompt, input_data)
      fmt = classify_format(output)  # "json", "markdown", "plain", "json_in_fences"
      formats_seen.add(fmt)
      if fmt != "json":
        parse_failures += 1

  return {
    "formats_seen": formats_seen,
    "consistency": len(formats_seen) == 1,
    "parse_failure_rate": parse_failures / (len(test_inputs) * n_runs),
  }
```

If `formats_seen` has more than one entry, formatting is inconsistent.

### Fix

1. **Pick one format** — JSON, XML, or markdown; not a mix
2. **Use structured output mode** — `response_format: json_object` or tool schema
3. **Explicit negative constraints** — "No markdown fences. No preamble. No commentary."
4. **Consistent delimiters** — all XML or all markdown, not both
5. **Post-processing normalization** — strip fences, parse leniently as safety net

```python
# BEFORE — mixed formatting
MIXED = """
Analyze the data below.

<document>{doc}</document>

Return your analysis as JSON:
```json
{"findings": [...]}
```

Or use bullet points if JSON is too complex.
"""

# AFTER — consistent
CONSISTENT = """
Analyze the document and return findings as JSON.

<document>{doc}</document>

Output format (JSON only, no fences, no preamble):
{"findings": [{"issue": str, "severity": "low|medium|high", "evidence": str}]}
"""

API_CONFIG = {
  "temperature": 0.0,
  "response_format": {"type": "json_object"},
}
```

### Prevention

- Structured output API mode for all machine-parseable responses
- Format validation in CI (100% parse rate required)
- Single delimiter convention per prompt
- Post-processing as safety net, not primary strategy

---

## 8. Weak Constraints

### Symptoms

- Model generates verbose responses when conciseness is needed
- Outputs include preamble ("Sure! Here's your analysis...")
- Model answers out-of-scope questions instead of refusing
- Generated content includes disclaimers and hedging
- Safety-critical fields sometimes missing without error

### Root Cause

Constraints are stated as suggestions ("try to", "if possible", "preferably") rather than hard requirements. No enforcement mechanism (schema, validation, post-processing) backs up the constraints.

### Diagnose

Review prompt for weak language:

```python
WEAK_PHRASES = [
  "try to", "if possible", "preferably", "when appropriate",
  "if you can", "it would be nice", "consider", "might want to",
  "should probably", "if applicable",
]

def find_weak_constraints(prompt: str) -> list[str]:
  return [phrase for phrase in WEAK_PHRASES if phrase in prompt.lower()]
```

Test out-of-scope inputs — does the model refuse or comply?

### Fix

```python
# BEFORE — weak constraints
WEAK = """
Try to keep your response concise if possible.
If you can, return JSON format.
Please consider refusing if the question is outside your scope.
"""

# AFTER — strong constraints
STRONG = """
CONSTRAINTS (violations are failures):
1. Response MUST be valid JSON. No other format accepted.
2. Response MUST be under 200 tokens.
3. If the question is outside billing topics, MUST return:
   {"status": "refused", "reason": "out_of_scope"}
4. Do NOT include preamble, commentary, or disclaimers.
5. Do NOT answer questions about other companies, general knowledge, or coding.
"""
```

Enforce with validation:

```python
def enforce_constraints(raw_output: str) -> str:
  data = json.loads(raw_output)  # Fails if not JSON
  if len(raw_output) > 800:  # ~200 tokens
    raise ConstraintViolation("output_too_long")
  return raw_output
```

### Prevention

- Use imperative language: "MUST", "Do NOT", "ONLY"
- Back constraints with schema validation
- Test constraint violations explicitly
- Structured output mode for format constraints

---

## 9. Prompt Drift

### Symptoms

- Quality was good at launch but degrades over weeks
- Behavior changes after model provider updates
- Different behavior between environments using "the same" prompt
- Engineers modify prompts locally without updating the repository
- No one knows which prompt version is running in production

### Root Cause

Prompts change informally without versioning, testing, or deployment process. Model providers update models silently. Multiple prompt copies diverge across services.

### Diagnose

```python
def diagnose_prompt_drift(prompt_id: str) -> dict:
  repo_version = get_repo_version(prompt_id)
  prod_version = get_production_version(prompt_id)
  quality_trend = get_quality_trend(prompt_id, days=30)
  model_version = get_current_model_version()

  return {
    "version_mismatch": repo_version != prod_version,
    "repo_version": repo_version,
    "prod_version": prod_version,
    "quality_trend": quality_trend,  # "declining", "stable", "improving"
    "model_changed_recently": model_version.changed_within(days=30),
    "untracked_copies": find_prompt_copies_in_codebase(prompt_id),
  }
```

Check: quality trend declining? Version mismatch? Model updated recently?

### Fix

1. **Version control all prompts** — git repository, semantic versioning
2. **Pin model versions** — explicit model ID in config
3. **Automated eval on model updates** — re-run golden set when provider announces changes
4. **Single source of truth** — no prompt copies in application code
5. **Deployment pipeline** — prompts deploy through CI, not manual edits

```python
# Track prompt lineage
PROMPT_REGISTRY = {
  "invoice-extraction": {
    "current": "2.3.0",
    "model": "gpt-4.1-mini-2026-04-14",
    "deployed_at": "2026-07-01",
    "eval_score": 0.94,
    "history": [
      {"version": "2.2.0", "eval_score": 0.91, "retired": "2026-07-01"},
      {"version": "2.1.0", "eval_score": 0.88, "retired": "2026-06-01"},
    ],
  }
}
```

### Prevention

- Prompt repository with mandatory CI
- Model version pinning and change alerts
- Weekly quality trend monitoring
- Quarterly prompt audit across all services

See [Production Prompt Engineering](production-prompt-engineering.md).

---

## 10. Brittle Prompts

### Symptoms

- Small input variations cause completely different output quality
- Adding one word to the prompt breaks behavior
- Works on test inputs but fails on production data distribution
- Slight rephrasing of user input changes classification
- Prompt works with one model but fails with another

### Root Cause

Prompt is overfitted to specific test cases, relies on fragile phrasing, or uses tricks that don't generalize. No robustness testing across input variations.

### Diagnose

```python
async def test_brittleness(prompt, base_input: str, eval_fn) -> dict:
  variations = [
    base_input,
    base_input.upper(),
    base_input + " ",  # trailing space
    base_input.replace(".", "!"),  # punctuation change
    f"Please {base_input}",  # politeness wrapper
    base_input + "\n\nThanks!",  # appended text
    rewrite_slightly(base_input),  # paraphrase
  ]

  results = [await eval_fn(prompt, v) for v in variations]
  scores = [r.score for r in results]

  return {
    "base_score": scores[0],
    "min_score": min(scores),
    "max_score": max(scores),
    "variance": statistics.variance(scores),
    "brittle": max(scores) - min(scores) > 0.15,
  }
```

If quality varies > 15% across minor input changes, the prompt is brittle.

### Fix

1. **Test input variations** — paraphrases, casing, punctuation, appended text
2. **Use schema constraints** — reduce dependence on phrasing
3. **Diversify eval set** — include natural production variation
4. **Avoid prompt hacks** — "IMPORTANT!!!" and trick phrasing don't generalize
5. **Temperature 0** — reduce random brittleness

```python
# BEFORE — brittle (overfitted to specific phrasing)
BRITTLE = """
When you see "Invoice #" followed by a number, extract it.
When you see "Total:" followed by a dollar amount, extract it.
If the invoice says "Amount Due" instead of "Total", extract that.
If it says "Balance", extract that too.
[50 more specific pattern matches...]
"""

# AFTER — robust (general principles)
ROBUST = """
Extract invoice fields from the document.
Identify fields by their meaning, not exact labels.
Common label variations:
  total: "Total", "Amount Due", "Balance", "Grand Total"
  date: "Date", "Invoice Date", "Issued", "Due Date"
Return JSON matching the schema. Missing fields → null.
"""
```

### Prevention

- Variation testing in eval pipeline
- Diverse golden set from real production distribution
- Schema-based extraction over pattern matching
- Cross-model testing before deploy

---

## 11. No Versioning or Testing

### Symptoms

- "Which prompt version is in production?" — nobody knows
- Prompt changes deployed without testing
- No way to compare current vs previous prompt quality
- Rollback requires manual reconstruction from memory
- Multiple engineers overwrite each other's prompt changes

### Root Cause

Prompts treated as disposable configuration rather than versioned software. No CI pipeline, no golden dataset, no deployment process.

### Diagnose

| Question | Healthy Answer | Unhealthy Answer |
|----------|---------------|-----------------|
| Where are prompts stored? | Git repository | "In the code" / "In a Google Doc" |
| How do you test prompt changes? | CI with golden set | "I tried a few examples" |
| Can you rollback in < 5 min? | Yes, via feature flag | "We'd have to redeploy" |
| Do you know the production version? | Yes, in manifest | "I think it's the latest" |
| When was last eval? | This week | "We haven't evaluated" |

### Fix

1. Create prompt repository with semantic versioning
2. Build golden dataset from production samples
3. Add CI regression tests on every prompt change
4. Implement feature flag rollout
5. Maintain manifest with current versions and eval scores

See [Prompt Testing](prompt-testing.md) and [Production Prompt Engineering](production-prompt-engineering.md).

### Prevention

- Prompts are code — apply same engineering practices
- CI blocks merges without eval pass
- Manifest registry updated on every deploy
- On-call runbook includes prompt rollback procedure

---

## 12. Ignoring Model Differences

### Symptoms

- Prompt works on GPT but fails on Claude (or vice versa)
- Switching models causes format or quality regression
- Instructions tuned for one model's quirks break on another
- Token counts differ significantly across models for same prompt
- Structured output behavior varies by provider

### Root Cause

Prompts designed and tested on a single model, then deployed with a different model without re-evaluation. Each model family has different instruction-following patterns, tokenization, and capabilities.

### Diagnose

```python
async def compare_models(prompt, eval_set, models: list[str]) -> dict:
  results = {}
  for model in models:
    scores = [await evaluate(prompt, case, model=model) for case in eval_set]
    results[model] = {
      "accuracy": mean(s.accuracy for s in scores),
      "format_pass": mean(s.format_ok for s in scores),
      "avg_tokens": mean(s.total_tokens for s in scores),
      "p95_latency": percentile([s.latency for s in scores], 95),
    }
  return results
```

### Fix

1. **Test on target model** — eval on the model you'll deploy
2. **Model-specific prompt variants** — if needed, not one-size-fits-all
3. **Abstract model config** — model selection in config, not in prompt text
4. **Re-evaluate on model changes** — treat model switch as prompt change

```yaml
# Model-specific config, shared prompt content
prompt: invoice-extraction@2.3.0

models:
  gpt-4.1-mini:
  temperature: 0.0
    response_format: {type: json_object}
  claude-sonnet-4:
    temperature: 0.0
    # Claude uses different structured output mechanism
  gemini-2.5-flash:
    temperature: 0.0
    response_mime_type: application/json
```

### Prevention

- Model pinned in config with explicit version
- Multi-model eval for critical prompts before deploy
- Model-specific config layer, shared prompt content
- Alert on model version changes from provider

See [Model Comparison Guide](../llm-engineering/model-comparison-guide.md).

---

## Pre-Production Checklist

- [ ] Prompt is specific — task, format, scope, and edge cases defined
- [ ] No conflicting instructions across layers
- [ ] All required domain context included
- [ ] Token count within budget (< 2K for most tasks)
- [ ] No duplicated instructions
- [ ] Few-shot examples follow all stated rules (or removed in favor of schema)
- [ ] Consistent formatting with structured output mode
- [ ] Strong constraints with validation enforcement
- [ ] Versioned in repository with semantic versioning
- [ ] Golden dataset eval passes with no regression
- [ ] Tested on target model (not just development model)
- [ ] Variation testing shows low brittleness
- [ ] Adversarial injection tests pass
- [ ] Rollback plan documented and tested

---

## Interview Preparation

**Q: What are the most common prompt engineering mistakes?**

> Vague instructions, conflicting rules, missing domain context, excessive context bloat, poor few-shot examples, inconsistent output formatting, and no versioning/testing. Most failures are design issues, not model limitations.

**Q: How do you diagnose a failing prompt in production?**

> Check this mistake catalog: Is it vague? Conflicting? Missing context? Format inconsistent? Then compare version in prod vs repo, check model version, run against golden set, and check quality trend for drift.

**Q: How do you prevent prompt drift?**

> Version control, semantic versioning, CI eval on every change, model version pinning, weekly quality monitoring, single source of truth, and feature flag rollout with rollback capability.

**Scenario:** A classification prompt was 95% accurate at launch but is now 78% after three months.

> **Discussion points:**
> - **Prompt drift:** Informal changes without versioning
> - **Model update:** Provider updated model silently
> - **Data drift:** Production inputs changed distribution
> - **Brittleness:** Prompt overfitted to original test cases
> - **Fix:** Pin model version, re-evaluate on current production sample, rebuild golden set, version and test prompt changes

---

## Navigation

### Prerequisites

- Sections 1–12 of this handbook — see [Introduction](introduction-to-prompt-engineering.md)
- [LLM Engineering Mistakes](../llm-engineering/llm-engineering-mistakes.md)

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
| 17 | Prompt Engineering Mistakes | **You are here** |
| 18 | Production Prompt Engineering | [production-prompt-engineering.md](production-prompt-engineering.md) |
| — | Comparison Guides (supplementary) | [prompt-comparison-guides.md](prompt-comparison-guides.md) |

### Related Topics

- [LLM Engineering Mistakes](../llm-engineering/llm-engineering-mistakes.md) — broader LLM pitfalls
- [Common Engineering Mistakes](../common-mistakes/common-engineering-mistakes.md)

### Next Topics

- [Production Prompt Engineering](production-prompt-engineering.md) — prevent these mistakes at scale
- [Prompt Testing](prompt-testing.md) — catch mistakes before deploy

---

## See Also

- [Prompt Testing](prompt-testing.md)
- [Prompt Optimization](prompt-optimization.md)
- [Production Prompt Engineering](production-prompt-engineering.md)
- [LLM Engineering Mistakes](../llm-engineering/llm-engineering-mistakes.md)

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Initial release — Section 17 |
