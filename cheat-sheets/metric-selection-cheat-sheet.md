# Metric Selection Cheat Sheet

| Task | Primary metrics |
|------|-----------------|
| Classification | Precision, recall, F1 |
| Short answer | Exact match + semantic |
| RAG | Faithfulness, context precision, answer relevance |
| Agent | Task completion, tool accuracy |
| Chat | Helpfulness, safety, coherence |
| Ops | P95 latency, cost/request |

Avoid BLEU/ROUGE alone for open-ended LLM tasks.

See [LLM Evaluation Metrics](../domains/ai-evaluation/llm-evaluation-metrics.md).
