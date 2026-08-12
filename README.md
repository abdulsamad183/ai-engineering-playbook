# AI Engineering Playbook

> A production handbook for **building, shipping, and operating** AI systems — from Python foundations through LLMs, RAG, agents, and production ops.

Click any topic to open its handbook. Each hub includes definitions, a learning path, diagrams, and linked deep dives.

---

## Start here

New to the playbook? Follow this path, then build. Check items off as you go.

### Progress checklist

- [ ] **Foundations:** [Python](domains/python-engineering/README.md) → [Frameworks](domains/python-frameworks-libraries/README.md) → [Math & Stats](domains/mathematics-statistics/README.md)
- [ ] **Models:** [ML](domains/machine-learning/README.md) → [DL](domains/deep-learning/README.md) → [NLP](domains/natural-language-processing/README.md) → [Transformers](domains/transformers/README.md) → [LLMs](domains/llm-engineering/README.md)
- [ ] **Build theory:** [Prompt Engineering](domains/prompt-engineering/README.md) → [LLM App Dev](domains/llm-application-development/README.md) → [RAG](domains/rag/README.md)
- [ ] **Offline demos:** [Examples quick start](examples/README.md) (RAG / agent / chat / GenAI)
- [ ] **Graduate to starters:** [RAG path](examples/rag/FROM_MINI_TO_STARTER.md) · [Agent path](examples/agents/FROM_MINI_TO_STARTER.md) · [API path](examples/llm-applications/FROM_MINI_TO_STARTER.md)
- [ ] **Capstone:** [RAG Chat API walkthrough](meta/capstone-walkthrough.md)
- [ ] **Harden:** [Evaluation](domains/ai-evaluation/README.md) → [Deployment](domains/ai-deployment/README.md) → [Security](domains/ai-security-guardrails/README.md)
- [ ] **Interview track:** [Interview prep path](meta/interview-path.md)

| Step | Do this |
|------|---------|
| 1 | Foundations: Python → Frameworks → Math |
| 2 | Models: ML → DL → NLP → Transformers → LLMs |
| 3 | Build: Prompts → App Dev → RAG |
| 4 | Run offline demos, then starters |
| 5 | Capstone RAG Chat API |
| 6 | Eval → Deploy → Security |

---

## Topics

```mermaid
flowchart TB
  subgraph foundations [Foundations]
    P[Python]
    PF[Python Frameworks]
    MS[Math & Stats]
    ML[Machine Learning]
    DL[Deep Learning]
    NLP[NLP]
  end
  subgraph models [Models]
    TR[Transformers]
    LLM[LLMs]
    GEN[Generative AI]
  end
  subgraph apps [Applications]
    PE[Prompt Engineering]
    APP[LLM App Dev]
    CB[Chatbots]
    EMB[Embeddings & VDB]
    RAG[RAG]
    FT[Fine-Tuning]
    EV[Evaluation]
  end
  subgraph agents [Agents]
    AG[AI Agents]
    AA[Agentic AI]
    MCP[MCP]
    MAS[Multi-Agent]
  end
  subgraph prod [Production]
    SD[System Design]
    OPS[MLOps & LLMOps]
    DEP[Deployment]
    SEC[Security]
    RES[Research]
  end
  foundations --> models --> apps --> agents --> prod
```

| # | Topic | What you will learn |
|---|-------|---------------------|
| 1 | [Python](domains/python-engineering/README.md) | Production Python for AI — expanded topics with AI angles |
| 2 | [Python Frameworks & Libraries](domains/python-frameworks-libraries/README.md) | NumPy, Pandas, Matplotlib, FastAPI, Pydantic — deepened lessons |
| 3 | [Mathematics & Statistics](domains/mathematics-statistics/README.md) | Linear algebra, probability, stats for ML — deepened lessons |
| 4 | [Machine Learning](domains/machine-learning/README.md) | Classical ML — deepened lessons across basics, models, eval, ensembles |
| 5 | [Deep Learning](domains/deep-learning/README.md) | Neural nets — deepened CNNs, sequences, training, deployment |
| 6 | [Natural Language Processing](domains/natural-language-processing/README.md) | Text to tasks to attention — deepened NLP curriculum |
| 7 | [Transformers](domains/transformers/README.md) | Attention to inference — deepened architecture, families, efficiency |
| 8 | [Large Language Models (LLMs)](domains/llm-engineering/README.md) | Pretrain to serve — deepened thin LLM sections |
| 9 | [Generative AI](domains/generative-ai/README.md) | Full deep lessons across 14 sections (GANs, VAEs, diffusion, multimodal, safety) |
| 10 | [Prompt Engineering](domains/prompt-engineering/README.md) | 5 sections · 19 topics — craft → ops → production |
| 11 | [LLM Application Development](domains/llm-application-development/README.md) | App architecture, orchestration, APIs, reliability — nested curriculum |
| 12 | [Chatbots](domains/chatbots/README.md) | Dialogue, memory, grounding, channels, ops — nested curriculum |
| 13 | [Embeddings & Vector Databases](domains/embeddings-vector-databases/README.md) | Embeddings, ANN, VDBs, providers, ops — nested curriculum |
| 14 | [RAG](domains/rag/README.md) | Ingestion, retrieval, grounding, eval — nested handbook |
| 15 | [LLM Fine-Tuning](domains/llm-fine-tuning/README.md) | Decision, data, LoRA/DPO, serving — nested curriculum |
| 16 | [LLM Evaluation](domains/ai-evaluation/README.md) | Metrics, surfaces, online eval, frameworks — nested handbook |
| 17 | [AI Agents](domains/ai-agents/README.md) | Cognition, tools, frameworks, production — nested handbook |
| 18 | [Agentic AI](domains/agentic-ai/README.md) | Autonomy, product patterns, governance — nested curriculum |
| 19 | [MCP](domains/mcp/README.md) | MCP primitives, clients/servers, production — nested handbook |
| 20 | [Multi-Agent Systems](domains/multi-agent-systems/README.md) | Coordination, communication, reliability — nested curriculum |
| 21 | [AI System Design](domains/ai-system-design/README.md) | Product designs and interview craft — nested handbook |
| 22 | [MLOps & LLMOps](domains/mlops-llmops/README.md) | Artifacts, pipelines, LLMOps governance — nested curriculum |
| 23 | [AI Deployment & Infrastructure](domains/ai-deployment/README.md) | Deploy, observe, reliability — nested handbook |
| 24 | [AI Security & Guardrails](domains/ai-security-guardrails/README.md) | Threats, guardrails, secure tools — nested handbook |
| 25 | [Advanced AI Research](domains/advanced-ai-research/README.md) | Papers and research-to-prod — nested handbook |

---

## Suggested learning order

Follow this path if you are building the skill stack from scratch. Jump anywhere if you already know what you need.

```mermaid
flowchart LR
  A[1–6 Foundations] --> B[7–9 Models]
  B --> C[10–16 Apps]
  C --> D[17–20 Agents]
  D --> E[21–25 Production & research]
```

| Stage | Topics |
|-------|--------|
| Foundations | 1 → 6 |
| Models | 7 → 9 |
| Applications | 10 → 16 |
| Agents | 17 → 20 |
| Production & research | 21 → 25 |

Hands-on path: **[Capstone: RAG Chat API](meta/capstone-walkthrough.md)** · Full curriculum notes: **[Learning Roadmap](meta/roadmap.md)**

---

## Also in this repo

| Need | Go to |
|------|-------|
| Starters (FastAPI, RAG, agent, MCP) | [templates/engineering/](templates/engineering/README.md) |
| Runnable snippets | [Examples](examples/README.md) |
| Prompt files | [Prompts](prompts/README.md) |
| One-page cards | [Cheat Sheets](cheat-sheets/README.md) |
| Term definitions | [Glossary](meta/glossary.md) |
| Every document | [Master Index](meta/indexes/MASTER-INDEX.md) |
| Extra domains (backend, FastAPI, debugging, interviews, …) | [Domains overview](domains/README.md) |
| Site how-to | [Docs site guide](docs-site.md) |

---

## Contributing

1. Choose a [domain](domains/README.md) and a [document template](meta/templates/).
2. Follow the [style guide](meta/style-guide.md).
3. Register the doc in the domain README and [master index](meta/indexes/MASTER-INDEX.md).

---

## License

[MIT License](LICENSE)
