---
title: "Interview Prep Path"
description: "A focused path through the playbook for AI engineering interviews — system design, coding, RAG, agents, and eval."
status: published
created: 2026-08-12
updated: 2026-08-12
version: "1.0"
---

# Interview Prep Path

> Use the handbooks as an interview study plan — not only as a reading list.

## One-week sprint

| Day | Focus | Read | Practice |
|-----|-------|------|----------|
| 1 | Python + APIs | [Python](../domains/python-engineering/README.md), [Frameworks/FastAPI](../domains/python-frameworks-libraries/fastapi/README.md) | Offline [mini chat API](../examples/llm-applications/FROM_MINI_TO_STARTER.md) |
| 2 | ML/DL refresh | [ML](../domains/machine-learning/README.md), [DL](../domains/deep-learning/README.md) | Explain bias-variance + backprop on a whiteboard |
| 3 | Transformers/LLMs | [Transformers](../domains/transformers/README.md), [LLMs](../domains/llm-engineering/README.md) | Attention + decoding tradeoffs |
| 4 | RAG | [RAG](../domains/rag/README.md), [Embeddings](../domains/embeddings-vector-databases/README.md) | [mini RAG](../examples/rag/FROM_MINI_TO_STARTER.md) |
| 5 | Agents | [AI Agents](../domains/ai-agents/README.md), [MCP](../domains/mcp/README.md) | [mini ReAct](../examples/agents/FROM_MINI_TO_STARTER.md) |
| 6 | Eval + production | [Evaluation](../domains/ai-evaluation/README.md), [Deployment](../domains/ai-deployment/README.md), [Security](../domains/ai-security-guardrails/README.md) | Design an eval gate |
| 7 | System design | [AI System Design](../domains/ai-system-design/README.md) | One full design: ChatGPT-like or Cursor-like |

## Cheat sheets to keep open

- [Cheat Sheets hub](../cheat-sheets/README.md)
- RAG: retrieval, chunking, hallucination checklists under `cheat-sheets/rag-*`
- Agents: `cheat-sheets/agent-*`
- Eval: `cheat-sheets/*evaluation*`

## Interview drills

1. **Design RAG for a support bot** — ingestion, hybrid retrieval, citations, eval, abuse.
2. **Design an agent with tools** — budgets, HITL, observability, MCP.
3. **Debug a quality regression** — leakage, prompt change, index drift, judge bias.
4. **Cost/latency** — KV cache, smaller routers, caching embeddings, canary rollback.

## Capstone as portfolio

Ship [Capstone: RAG Chat API](capstone-walkthrough.md) and keep notes on tradeoffs — that is a stronger artifact than slides alone.

## See also

- [Start here](../README.md#start-here)
- [Interview preparation domain](../domains/interview-preparation/README.md) (Reference)
