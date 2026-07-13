---
title: "Brainstorming Prompt Template"
description: "Reusable prompt for structured ideation with constraints, diversity, and evaluation criteria."
domain: prompt-engineering
tags: [prompt, brainstorming, ideation, creativity]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
id: brainstorming-v1
task: brainstorming
models:
  recommended: [gpt-4o, claude-sonnet-4]
  min_capability: intermediate
token_budget:
  system: 300
  user_per_input: 150
variables:
  required: [problem_statement, num_ideas]
  optional: [constraints, audience, evaluation_criteria, domain_context]
output:
  format: markdown
  schema: null
related:
  - ../../domains/prompt-engineering/advanced-reasoning-strategies.md
  - ../../domains/prompt-engineering/prompt-templates-guide.md
keywords: [brainstorming, ideation, product discovery, design thinking]
---

# Brainstorming Prompt Template

> Generate diverse, constraint-aware ideas with brief rationale and self-evaluation against stated criteria.

## Pattern Overview

| Attribute | Value |
|-----------|-------|
| Use Case | Product features, solution exploration, workshop prep, design alternatives |
| Best Models | gpt-4o, claude-sonnet-4 |
| Complexity | Simple to Moderate |
| Token Budget | ~400–800 tokens |
| Expected Output | Numbered ideas with rationale and trade-off notes |

## When to Use

- Early-stage product discovery before committing engineering resources
- Generating alternative approaches to a technical problem
- Workshop warm-up with structured output for team discussion
- Exploring edge cases or failure modes for a proposed design

## When Not to Use

- Final product decisions without human stakeholder review
- Domains requiring proprietary data the model cannot access
- Regulated decisions (medical, legal, financial) without expert validation

## System Prompt

```
You are a creative strategist facilitating structured brainstorming for {{audience}}.

Rules:
- Generate exactly {{num_ideas}} distinct ideas.
- Each idea must be meaningfully different — avoid minor variations of the same concept.
- Respect all constraints: {{constraints}}
- For each idea provide: title, 2–3 sentence description, key benefit, main risk.
- Rate each idea 1–5 against: {{evaluation_criteria}}
- Flag ideas that violate constraints as [INVALID] with reason.
- Do not claim market data or user research you do not have.

Output format (Markdown):
## Idea 1: {title}
**Description:** ...
**Benefit:** ...
**Risk:** ...
**Scores:** criterion1: N/5, criterion2: N/5
```

## User Prompt

```
<problem>
{{problem_statement}}
</problem>

<domain_context>
{{domain_context}}
</domain_context>

Prior ideas to avoid duplicating:
{{exclude_ideas}}
```

## Variables

| Name | Required | Default | Description |
|------|----------|---------|-------------|
| `problem_statement` | Yes | — | Problem or opportunity to brainstorm |
| `num_ideas` | Yes | 5 | Number of distinct ideas to generate |
| `constraints` | No | budget and timeline realistic for a startup | Hard limits on solutions |
| `audience` | No | product and engineering leads | Who will evaluate ideas |
| `evaluation_criteria` | No | feasibility, impact, time-to-value | Scoring dimensions |
| `domain_context` | No | (none) | Industry, tech stack, user segment |
| `exclude_ideas` | No | (none) | Ideas already considered |

## Complete Example

### Input Variables

```yaml
problem_statement: Reduce customer support ticket volume for a B2B SaaS billing product
num_ideas: 3
constraints: No new headcount; ship within one quarter; must integrate with existing Zendesk
evaluation_criteria: feasibility, user impact, engineering effort
```

### Expected Output

Structured markdown with 3 ideas, each with description, benefit, risk, and scores — no invented user research statistics.

## Evaluation Criteria

| Metric | Target | How to Measure |
|--------|--------|----------------|
| Diversity | High | Ideas address problem from different angles |
| Constraint compliance | 100% | No [INVALID] ideas or all flagged correctly |
| Actionability | Subjective | Team can discuss without clarifying questions |
| Hallucination | 0% | No fabricated metrics or citations |

## Tips and Pitfalls

- Set explicit `num_ideas` and `constraints` — vague brainstorming produces generic lists.
- Use higher temperature (0.7–0.9) for diversity; lower for feasibility-focused sessions.
- Run a second pass with an evaluation prompt to rank ideas for production planning.
