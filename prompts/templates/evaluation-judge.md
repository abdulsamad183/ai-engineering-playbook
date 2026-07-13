---
title: "Evaluation Judge Prompt Template"
description: "Reusable prompt for LLM-as-judge evaluation of outputs against rubrics and reference answers."
domain: prompt-engineering
tags: [prompt, evaluation, llm-judge, quality-assurance]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
id: evaluation-judge-v1
task: evaluation
models:
  recommended: [gpt-4o, claude-sonnet-4]
  min_capability: advanced
token_budget:
  system: 400
  user_per_evaluation: 400
variables:
  required: [input, output, rubric]
  optional: [reference_answer, task_description, scoring_scale]
output:
  format: json
  schema: evaluation_result
related:
  - question-answering.md
  - code-review.md
  - ../../domains/prompt-engineering/prompt-templates-guide.md
keywords: [LLM judge, evaluation, rubric scoring, quality metrics]
---

# Evaluation Judge Prompt Template

> Score model outputs against a defined rubric. Return structured scores, pass/fail verdict, and cited rationale.

## Pattern Overview

| Attribute | Value |
|-----------|-------|
| Use Case | Automated eval pipelines, A/B testing prompts, regression gates, human-eval augmentation |
| Best Models | gpt-4o, claude-sonnet-4 |
| Complexity | Moderate |
| Token Budget | ~600–1200 tokens (system + user) |
| Expected Output | JSON with per-criterion scores and overall verdict |

## When to Use

- Scoring QA faithfulness, summarization quality, or classification rationale
- Comparing two prompt versions on a golden dataset
- CI regression gates for prompt changes
- Filtering outputs for human review (score below threshold)

## When Not to Use

- High-stakes decisions without human oversight (bias, position effects)
- Evaluating the judge model with itself (use human labels for calibration)
- Subjective creative tasks without clear rubric criteria

## System Prompt

```
You are an impartial evaluator for {{task_description}}.

Score the candidate output against each criterion in the rubric below.
Be strict, consistent, and cite specific evidence from the input and output.

Rubric:
{{rubric}}

Scoring scale: {{scoring_scale}}

Rules:
- Base scores only on the provided input, output, and reference (if any).
- Do not assume unstated context or give benefit of the doubt.
- Quote or paraphrase specific phrases when explaining deductions.
- If output is empty or off-topic, score 0 on all applicable criteria.
- Overall pass requires all mandatory criteria to meet their thresholds.

Output format (valid JSON only):
{{output_format}}
```

## User Prompt

```
<input>
{{input}}
</input>

<candidate_output>
{{output}}
</candidate_output>

<reference_answer>
{{reference_answer}}
</reference_answer>

Evaluate the candidate output.
```

## Variables

| Name | Required | Default | Description |
|------|----------|---------|-------------|
| `input` | Yes | — | Original prompt input or question |
| `output` | Yes | — | Model output to evaluate |
| `rubric` | Yes | — | Criteria with descriptions and pass thresholds |
| `task_description` | No | general LLM output quality | Task type for calibration |
| `reference_answer` | No | (none) | Gold answer for comparison |
| `scoring_scale` | No | 1-5 integer per criterion | Scale definition |
| `output_format` | No | see below | JSON result schema |

Default `output_format`: `{"criteria_scores": [{"criterion": "...", "score": 4, "max_score": 5, "passed": true, "rationale": "..."}], "overall_score": 4.2, "overall_passed": true, "summary": "..."}`

## Complete Example

### Input

```yaml
input: "Context: [doc_01] Refunds take 5-7 business days. Question: How long?"
output: "Refunds typically take 2-3 weeks."
reference_answer: "Refunds take 5-7 business days [doc_01]."
rubric: "faithfulness (mandatory, pass>=4), citation (mandatory, pass>=4)"
```

### Expected Output

```json
{"criteria_scores": [{"criterion": "faithfulness", "score": 1, "passed": false, "rationale": "Claims 2-3 weeks; context says 5-7 days."}], "overall_passed": false, "summary": "Contradicts context. Fail."}
```

## Evaluation Criteria

| Metric | Target | How to Measure |
|--------|--------|----------------|
| Judge-human agreement | > 85% | Cohen's kappa vs. human labels |
| Inter-judge consistency | > 90% | Same output scored twice |
| Discrimination | Clear separation | Failing outputs score below passing |
| Format compliance | 100% | JSON schema validation |
| Position bias | Monitor | Swap A/B order in pairwise mode |

## Tips and Pitfalls

- Use a stronger model as judge; define rubric criteria with observable pass/fail signals.
- Include `{{reference_answer}}` when available; swap A/B order in pairwise mode to reduce bias.
- Avoid vague rubrics and using the same model as both judge and subject.
