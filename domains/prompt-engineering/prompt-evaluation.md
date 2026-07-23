---
title: "Prompt Evaluation"
description: "Production reference for prompt evaluation — quality, consistency, faithfulness, relevance, completeness, correctness, latency, token usage, cost, user satisfaction, and high-level automated evaluation pipelines."
domain: prompt-engineering
tags: [prompt, evaluation, production, intermediate, metrics, quality]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - prompt-testing.md
  - prompt-optimization.md
  - ../ai-evaluation/README.md
  - ../llm-engineering/llm-cost-optimization.md
keywords: [prompt evaluation, faithfulness, relevance, LLM-as-judge, automated evaluation, quality metrics]
author: hp
---

# Prompt Evaluation

> Section 14 of this handbook — testing tells you whether a prompt breaks; evaluation tells you whether it is good. Prompt evaluation quantifies output quality across dimensions that matter to users and business outcomes, enabling data-driven iteration instead of subjective debate.

## Table of Contents

- [Evaluation Framework](#evaluation-framework)
- [Quality](#quality)
- [Consistency](#consistency)
- [Faithfulness](#faithfulness)
- [Relevance](#relevance)
- [Completeness](#completeness)
- [Correctness](#correctness)
- [Latency](#latency)
- [Token Usage](#token-usage)
- [Cost](#cost)
- [User Satisfaction](#user-satisfaction)
- [Automated Evaluation Pipeline](#automated-evaluation-pipeline)
- [LLM-as-Judge](#llm-as-judge)
- [Evaluation Dashboards](#evaluation-dashboards)
- [Evaluation Checklist](#evaluation-checklist)
- [Common Mistakes](#common-mistakes)
- [Interview Preparation](#interview-preparation)
- [Navigation](#navigation)

---

## Evaluation Framework

Prompt evaluation operates at three levels:

```text
Unit Eval (single output) → Batch Eval (golden set) → Production Eval (live traffic)
```

| Level | Frequency | Data Source | Purpose |
|-------|-----------|-------------|---------|
| Unit | Every test run | Golden dataset | Regression detection |
| Batch | Weekly / on prompt change | Golden + holdout | Quality benchmarking |
| Production | Continuous | Sampled live traffic | Drift detection |

### Evaluation Dimensions Map

| Dimension | Question Answered | Primary Method |
|-----------|-------------------|----------------|
| Quality | Is the output good overall? | LLM-as-judge, human review |
| Consistency | Same input → same output? | Multi-run variance |
| Faithfulness | Is it grounded in context? | Claim verification |
| Relevance | Does it address the query? | Semantic similarity |
| Completeness | Are all parts answered? | Checklist / rubric |
| Correctness | Is it factually right? | Ground truth comparison |
| Latency | How fast? | Instrumentation |
| Tokens | How long? | Token counting |
| Cost | How expensive? | Token × rate |
| User satisfaction | Do users approve? | Thumbs, CSAT, retention |

> **Production Standard:** Define a **scorecard** per prompt with weighted dimensions, pass thresholds, and alert rules. No dimension should be optimized in isolation — improving faithfulness at the cost of latency may be the wrong tradeoff.

---

## Quality

Overall quality is a composite judgment of how well the prompt produces useful outputs.

### Quality Rubric Template

| Score | Label | Criteria |
|-------|-------|----------|
| 5 | Excellent | Fully correct, well-structured, no unnecessary content |
| 4 | Good | Correct with minor formatting or verbosity issues |
| 3 | Acceptable | Mostly correct; minor errors or omissions |
| 2 | Poor | Significant errors or missing key information |
| 1 | Unacceptable | Wrong, harmful, or completely off-topic |

### Measuring Quality

```python
QUALITY_RUBRIC = """
Rate the response 1-5 on overall quality for the task: {task_description}

Input: {input}
Expected: {expected}
Actual: {output}

Consider: accuracy, clarity, format compliance, and usefulness.
Return JSON: {"score": int, "reasoning": str}
"""


async def evaluate_quality(case: dict, judge_model: str = "gpt-4.1") -> dict:
  prompt = QUALITY_RUBRIC.format(**case)
  result = await llm_judge(prompt, model=judge_model)
  return result
```

### Quality Aggregation

| Metric | Formula | Use |
|--------|---------|-----|
| Mean quality score | avg(scores) | Overall health |
| Pass rate | % scores ≥ 4 | Gate for deploy |
| Quality@k | % in top k scores | Ranking prompt variants |
| Worst-case | min(scores) | Safety floor |

---

## Consistency

Consistency measures output stability across repeated invocations with identical inputs.

### Why Consistency Matters

| Inconsistency Impact | Example |
|---------------------|---------|
| User confusion | Same question, different answers on refresh |
| Downstream breakage | Parsing fails when format varies |
| Trust erosion | "The AI keeps changing its mind" |
| Automation failure | RPA expects deterministic extraction |

### Measuring Consistency

```python
import hashlib
from collections import Counter


async def measure_consistency(
  prompt_fn, input_data: dict, n_runs: int = 5, temperature: float = 0.0
) -> dict:
  outputs = [await prompt_fn(input_data, temperature=temperature) for _ in range(n_runs)]

  exact_match_rate = len(set(outputs)) == 1

  # Semantic consistency via embedding similarity
  embeddings = [await embed(o) for o in outputs]
  pairwise_sim = cosine_similarity_matrix(embeddings)
  avg_semantic_consistency = pairwise_sim.mean()

  # Structural consistency (for JSON)
  schemas_match = len(set(extract_keys(o) for o in outputs)) == 1

  return {
    "exact_match": exact_match_rate,
    "semantic_consistency": avg_semantic_consistency,
    "structural_consistency": schemas_match,
    "unique_outputs": len(set(outputs)),
    "outputs": outputs,
  }
```

### Consistency Targets

| Task Type | Temperature | Target Consistency |
|-----------|-------------|-------------------|
| Extraction / classification | 0.0 | ≥ 99% exact or structural match |
| Summarization | 0.0–0.3 | ≥ 95% semantic similarity |
| Creative generation | 0.7+ | Intentional variance; evaluate quality not consistency |
| Structured JSON | 0.0 + schema | 100% parseable; ≥ 98% field match |

---

## Faithfulness

Faithfulness measures whether the output is grounded in the provided context and does not introduce unsupported claims.

### Faithfulness vs Correctness

| Dimension | Measures | Requires Ground Truth? |
|-----------|----------|----------------------|
| Faithfulness | Claims supported by context | No — checks against provided context |
| Correctness | Claims match reality | Yes — requires external ground truth |

A response can be faithful but wrong (accurately quotes a wrong document) or correct but unfaithful (right answer from wrong reasoning).

### Faithfulness Evaluation

```python
async def evaluate_faithfulness(context: str, output: str) -> dict:
  claims = await extract_claims(output)
  results = []
  for claim in claims:
    supported = await check_entailment(context, claim)
    results.append({"claim": claim, "supported": supported})

  supported_count = sum(1 for r in results if r["supported"])
  return {
    "faithfulness_score": supported_count / max(len(results), 1),
    "unsupported_claims": [r["claim"] for r in results if not r["supported"]],
    "total_claims": len(results),
  }
```

### Faithfulness Metrics

| Metric | Definition | Target (RAG) |
|--------|-----------|--------------|
| Claim support rate | % claims entailed by context | ≥ 95% |
| Hallucination rate | % claims not in context | ≤ 5% |
| Attribution accuracy | % citations that support claims | ≥ 98% |
| Abstention accuracy | % unanswerable correctly refused | ≥ 90% |

---

## Relevance

Relevance measures whether the output addresses the user's actual query without tangents or missing the point.

### Relevance Signals

| Signal | Strong Relevance | Weak Relevance |
|--------|-----------------|----------------|
| Topic alignment | Directly answers question | Partially related tangent |
| Scope adherence | Stays within task boundaries | Over-explains or under-explains |
| Intent match | Addresses underlying need | Literal but unhelpful answer |
| Conciseness | Appropriate length for task | Verbose filler or too terse |

### Measuring Relevance

```python
RELEVANCE_PROMPT = """
Context: {context}
Question: {question}
Answer: {answer}

Rate relevance 1-5:
5 = Directly and fully addresses the question
3 = Partially relevant with useful content
1 = Off-topic or ignores the question

Return JSON: {"score": int, "missing_aspects": [str]}
"""
```

### Relevance vs Faithfulness

```text
High relevance + low faithfulness = Answers the question but fabricates
Low relevance + high faithfulness = Quotes context but misses the point
High both = Production quality
```

---

## Completeness

Completeness measures whether all required parts of the task are addressed.

### Completeness Checklist Pattern

```python
COMPLETENESS_CHECKS = {
  "support_response": [
    "acknowledges_the_issue",
    "provides_solution_or_next_step",
    "offers_contact_if_unresolved",
  ],
  "invoice_extraction": [
    "invoice_number",
    "date",
    "total",
    "line_items",
    "vendor_name",
  ],
  "meeting_summary": [
    "key_decisions",
    "action_items_with_owners",
    "open_questions",
  ],
}


def evaluate_completeness(output: dict, task: str) -> dict:
  required = COMPLETENESS_CHECKS[task]
  present = [field for field in required if field_present(output, field)]
  return {
    "completeness_score": len(present) / len(required),
    "missing": [f for f in required if f not in present],
    "present": present,
  }
```

### Partial Credit Scoring

| Approach | When to Use |
|----------|-------------|
| Binary (all or nothing) | Safety-critical fields |
| Weighted partial | Some fields more important |
| Tiered | Must-have vs nice-to-have fields |

---

## Correctness

Correctness compares output against known ground truth labels.

### Correctness Metrics by Task

| Task | Metric | Formula |
|------|--------|---------|
| Classification | Accuracy | correct / total |
| Multi-label | F1 | harmonic mean of precision, recall |
| Extraction | Field-level F1 | per-field exact match |
| Generation | ROUGE / BLEU | n-gram overlap (weak for semantics) |
| Generation | BERTScore | semantic similarity to reference |
| Q&A | Exact match / F1 | token overlap with answer |

```python
def field_level_f1(predictions: list[dict], ground_truth: list[dict]) -> dict:
  tp = fp = fn = 0
  for pred, truth in zip(predictions, ground_truth):
    for field in truth:
      if field in pred and pred[field] == truth[field]:
        tp += 1
      elif field in pred:
        fp += 1
      else:
        fn += 1
  precision = tp / (tp + fp) if (tp + fp) > 0 else 0
  recall = tp / (tp + fn) if (tp + fn) > 0 else 0
  f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0
  return {"precision": precision, "recall": recall, "f1": f1}
```

### Correctness Caveats

- Exact match is too strict for generation tasks — use semantic metrics
- Multiple valid answers exist for many questions — accept alternates
- Ground truth labels may themselves be wrong — audit labels periodically

---

## Latency

Latency evaluation ensures prompts meet performance SLOs.

### Latency Components

```text
Total Latency = Queue + Prefill (input tokens) + Generation (output tokens) + Post-processing
```

| Component | Driven By | Optimization Lever |
|-----------|-----------|-------------------|
| Prefill | Input token count | Shorter prompts, less context |
| Generation | Output token count | `max_tokens`, concise instructions |
| Queue | Provider load | Routing, caching |
| Post-processing | Parsing, validation | Async processing |

### Latency Metrics

| Metric | Definition | Typical SLO |
|--------|-----------|-------------|
| TTFT | Time to first token | < 500ms (chat) |
| TPS | Tokens per second | > 30 tps |
| P50 latency | Median end-to-end | Task-dependent |
| P95 latency | 95th percentile | 2–3× P50 |
| P99 latency | Tail latency | Alert threshold |

```python
@dataclass
class LatencyEval:
  prompt_version: str
  p50_ms: float
  p95_ms: float
  p99_ms: float
  avg_input_tokens: int
  avg_output_tokens: int

  def meets_slo(self, slo_p95_ms: float) -> bool:
    return self.p95_ms <= slo_p95_ms
```

See [LLM Performance Optimization](../llm-engineering/llm-performance-optimization.md) for optimization techniques.

---

## Token Usage

Token evaluation tracks prompt efficiency and identifies bloat.

### Token Breakdown

| Segment | What to Measure |
|---------|----------------|
| System prompt | Static instruction tokens |
| Few-shot examples | Example tokens (often largest segment) |
| Dynamic context | RAG chunks, user data |
| Conversation history | Prior turns |
| Output | Generated tokens |

```python
def analyze_token_budget(messages: list[dict], model: str = "gpt-4") -> dict:
  enc = tiktoken.encoding_for_model(model)
  breakdown = {}
  for i, msg in enumerate(messages):
    tokens = len(enc.encode(msg["content"]))
    breakdown[f"{msg['role']}_{i}"] = tokens
  breakdown["total_input"] = sum(breakdown.values())
  return breakdown
```

### Token Efficiency Metrics

| Metric | Formula | Target |
|--------|---------|--------|
| Tokens per task | avg input + output tokens | Minimize without quality loss |
| Output/input ratio | output / input | Task-dependent |
| Prompt overhead | system tokens / total input | < 30% for RAG |
| Example efficiency | quality gain per example token | Remove low-value examples |

---

## Cost

Cost evaluation translates token usage into financial impact.

### Cost Per Evaluation Run

```python
def eval_run_cost(
  cases: int,
  avg_input_tokens: int,
  avg_output_tokens: int,
  input_rate_per_m: float = 0.40,
  output_rate_per_m: float = 1.60,
) -> float:
  total_input = cases * avg_input_tokens
  total_output = cases * avg_output_tokens
  return (total_input * input_rate_per_m + total_output * output_rate_per_m) / 1_000_000
```

### Cost-Quality Tradeoff Matrix

| Prompt Variant | Accuracy | Cost/1K requests | Decision |
|---------------|----------|-----------------|----------|
| A (verbose few-shot) | 96% | $4.20 | Too expensive |
| B (zero-shot + schema) | 94% | $1.10 | **Ship** — 2% loss not worth 4× cost |
| C (minimal) | 87% | $0.60 | Too low quality |

### Cost Evaluation in CI

- Estimate cost per eval run before executing
- Set monthly eval budget caps
- Use cheaper models for format-only checks
- Cache eval results for unchanged prompts

See [LLM Cost Optimization](../llm-engineering/llm-cost-optimization.md).

---

## User Satisfaction

User satisfaction is the ultimate evaluation signal — but it is noisy, lagging, and expensive to collect at scale.

### Satisfaction Signals

| Signal | Collection | Latency | Reliability |
|--------|-----------|---------|-------------|
| Thumbs up/down | In-app button | Immediate | Noisy |
| CSAT survey | Post-interaction | Minutes | Moderate |
| Task completion | Behavioral | Minutes–hours | Strong |
| Return rate | Analytics | Days | Strong |
| Support tickets | Escalation | Hours–days | Strong but lagging |
| Edit rate | User modifies output | Immediate | Strong for generation |

### Bridging Automated and User Metrics

```text
Automated Eval (fast, cheap) → Correlated Proxy Metrics → User Satisfaction (slow, ground truth)
```

Build correlation between automated scores and user satisfaction:

```python
# Quarterly analysis
correlation = pearsonr(automated_quality_scores, user_thumbs_ratio)
# If correlation < 0.6, automated eval needs recalibration
```

### Satisfaction Targets

| Product Type | Target CSAT | Target Thumbs Up |
|-------------|------------|-----------------|
| Customer support bot | ≥ 4.2/5 | ≥ 75% |
| Internal copilot | ≥ 3.8/5 | ≥ 65% |
| Content generation | ≥ 4.0/5 | ≥ 70% |

---

## Automated Evaluation Pipeline

### Pipeline Architecture

```text
Trigger (PR / schedule / deploy)
  → Load golden dataset
  → Invoke prompt at pinned model + config
  → Run deterministic assertions
  → Run LLM-as-judge for quality dimensions
  → Aggregate scorecard
  → Compare to baseline
  → Report + gate
```

### Implementation

```python
@dataclass
class EvalScorecard:
  prompt_id: str
  version: str
  model: str
  n_cases: int
  quality_mean: float
  consistency: float
  faithfulness: float
  relevance: float
  completeness: float
  correctness_f1: float
  p95_latency_ms: float
  avg_cost_per_request: float
  pass: bool


async def run_eval_pipeline(prompt_id: str, version: str) -> EvalScorecard:
  cases = load_golden_set(prompt_id)
  results = [await evaluate_case(prompt_id, version, case) for case in cases]

  scorecard = EvalScorecard(
    prompt_id=prompt_id,
    version=version,
    model=PINNED_MODEL,
    n_cases=len(cases),
    quality_mean=mean(r.quality for r in results),
    consistency=mean(r.consistency for r in results),
    faithfulness=mean(r.faithfulness for r in results),
    relevance=mean(r.relevance for r in results),
    completeness=mean(r.completeness for r in results),
    correctness_f1=compute_f1(results),
    p95_latency_ms=percentile([r.latency_ms for r in results], 95),
    avg_cost_per_request=mean(r.cost for r in results),
    pass=check_thresholds(results),
  )
  save_scorecard(scorecard)
  return scorecard
```

### Pass/Fail Thresholds

```yaml
thresholds:
  quality_mean: { min: 4.0 }
  faithfulness: { min: 0.95 }
  correctness_f1: { min: 0.90, regression_max_drop: 0.02 }
  consistency: { min: 0.98 }
  p95_latency_ms: { max: 2000 }
  format_pass_rate: { min: 1.0 }
```

---

## LLM-as-Judge

LLM-as-judge uses a capable model to evaluate outputs at scale when human review is impractical.

### Judge Design Principles

| Principle | Rationale |
|-----------|-----------|
| Use a stronger model than the one evaluated | Judge must be at least as capable |
| Provide clear rubrics | Reduces judge variance |
| Use structured output for scores | Parseable, consistent |
| Include the ground truth when available | Anchors scoring |
| Calibrate against human labels | Validate judge accuracy quarterly |

### Judge Prompt Template

```python
JUDGE_TEMPLATE = """
You are an expert evaluator for {task_name}.

## Rubric
{rubrik}

## Input
{input}

## Reference Answer (if available)
{expected}

## Response to Evaluate
{output}

## Instructions
Score each dimension 1-5. Be strict but fair.
Cite specific evidence from the response.

Return JSON:
{
  "quality": int,
  "relevance": int,
  "completeness": int,
  "faithfulness": int,
  "reasoning": str
}
"""
```

### Judge Reliability

| Issue | Mitigation |
|-------|-----------|
| Position bias | Swap answer order in pairwise comparisons |
| Leniency bias | Anchor with calibration examples |
| Self-preference | Use different model family as judge |
| Variance | Run 3× and take median |

### Pairwise vs Pointwise Evaluation

| Method | Best For | Cost |
|--------|----------|------|
| Pointwise (score 1–5) | Absolute quality tracking | 1 judge call per output |
| Pairwise (A vs B) | Comparing prompt variants | 1 judge call per pair |
| Listwise (rank N) | Ranking multiple variants | 1 judge call per set |

---

## Evaluation Dashboards

### Dashboard Components

| Panel | Metrics | Alert |
|-------|---------|-------|
| Quality trend | Mean quality over time | Drop > 5% week-over-week |
| Dimension radar | All dimensions for current version | Any below threshold |
| Version comparison | Side-by-side scorecards | Regression on deploy |
| Cost trend | Cost per request over time | Increase > 20% |
| Latency trend | P50/P95 over time | P95 > SLO |
| User satisfaction | Thumbs ratio, CSAT | Below target |
| Failure analysis | Top failure categories | New category emerges |

### Example Scorecard Output

```text
Prompt: invoice-extraction v2.3.0 | Model: gpt-4.1-mini | Eval: 2026-07-13

  Quality:       4.3 / 5.0  ✓
  Consistency:   0.99       ✓
  Faithfulness:  0.97       ✓
  Relevance:     4.5 / 5.0  ✓
  Completeness:  0.94       ✓
  Correctness:   F1 0.93    ✓
  P95 Latency:   1,150 ms   ✓
  Avg Cost:      $0.0012    ✓

  VERDICT: PASS (8/8 thresholds met)
```

---

## Evaluation Checklist

- [ ] Scorecard defined with weighted dimensions and thresholds
- [ ] Golden dataset labeled and version-controlled
- [ ] Automated pipeline runs on every prompt change
- [ ] LLM-as-judge calibrated against human labels (≥ 0.7 correlation)
- [ ] Faithfulness and correctness measured separately
- [ ] Latency and cost tracked alongside quality
- [ ] User satisfaction correlated with automated metrics
- [ ] Dashboard with trend lines and regression alerts
- [ ] Holdout set evaluated only at release gates

---

## Common Mistakes

| Mistake | Consequence | Fix |
|---------|-------------|-----|
| Single metric optimization | Good F1, terrible UX | Multi-dimensional scorecard |
| No human calibration | Misleading automated scores | Quarterly human audit |
| Ignoring cost/latency | Quality at unsustainable price | Include in scorecard |
| Evaluating on training data | Overfit prompts | Holdout set |
| Weak judge model | Inaccurate evaluations | Use stronger model as judge |
| No production eval | Silent drift after deploy | Sample live traffic |

---

## Interview Preparation

**Q: How do you evaluate prompt quality in production?**

> Multi-dimensional scorecard: quality, faithfulness, relevance, completeness, correctness on a golden dataset. LLM-as-judge for scale, human calibration quarterly. Track latency, cost, and user satisfaction. Gate deploys on regression thresholds.

**Q: What is the difference between faithfulness and correctness?**

> Faithfulness checks claims against provided context — did the model stick to its sources? Correctness checks against ground truth — is the answer actually right? A model can be faithful to a wrong document or correct via hallucination.

**Q: When do you use LLM-as-judge vs human evaluation?**

> LLM-as-judge for scale and regression testing on every change. Human evaluation for calibration, subjective quality, new prompt design, and quarterly audits. Always validate judge against human labels.

---

## Navigation

### Prerequisites

- [Prompt Testing](prompt-testing.md) — Section 13
- [Prompt Lifecycle](prompt-lifecycle.md) — Section 11

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
| 14 | Prompt Evaluation | **You are here** |
| 15 | Prompt Optimization | [prompt-optimization.md](prompt-optimization.md) |
| 16 | Prompt Security | [prompt-security.md](prompt-security.md) |
| 17 | Prompt Engineering Mistakes | [prompt-engineering-mistakes.md](prompt-engineering-mistakes.md) |
| 18 | Production Prompt Engineering | [production-prompt-engineering.md](production-prompt-engineering.md) |
| — | Comparison Guides (supplementary) | [prompt-comparison-guides.md](prompt-comparison-guides.md) |

### Related Topics

- [AI Evaluation](../ai-evaluation/README.md) — system-level evaluation
- [LLM Cost Optimization](../llm-engineering/llm-cost-optimization.md) — cost metrics

### Next Topics

- [Prompt Optimization](prompt-optimization.md) — improve scores systematically
- [Prompt Testing](prompt-testing.md) — tests that protect eval baselines

---

## See Also

- [Prompt Testing](prompt-testing.md)
- [LLM Cost Optimization](../llm-engineering/llm-cost-optimization.md)
- [LLM Performance Optimization](../llm-engineering/llm-performance-optimization.md)
- [Ragas Documentation](https://docs.ragas.io/) — RAG evaluation framework

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Initial release — Section 14 |
