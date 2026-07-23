---
title: "Research Evolution"
description: "Timeline of AI research from Transformers through prompting, reasoning, RAG, agents, and MCP — how each era built on the last."
domain: papers
tags: [papers, timeline, evolution, transformers, agents, mcp]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - attention-is-all-you-need.md
  - research-comparison-guides.md
  - future-research.md
keywords: [AI research timeline, transformers, RAG, agents, MCP, evolution]
author: hp
---

# Research Evolution

> One-sentence takeaway: AI engineering evolved in layers — each research wave solved the previous layer's limitations, from parallel sequence modeling to autonomous tool-using agents.

## Timeline Overview

```mermaid
timeline
    title AI Research → Engineering Evolution
    2017 : Transformers
         : Parallel attention replaces RNNs
    2020 : Scaling + Few-Shot
         : GPT-3 in-context learning
    2022 : Alignment + CoT + ReAct
         : Instruction following, reasoning, tool use
    2023 : RAG + Agents + Multi-Agent
         : Grounding, autonomy, role specialization
    2024 : Advanced RAG + Coding Agents
         : Self-RAG, GraphRAG, SWE-Agent, DSPy
    2025 : Protocols + Optimization
         : MCP standardization, agent interop
    2026+ : Compound Systems
         : Multi-agent orchestration, eval-driven dev
```

---

## Era 1: Transformers (2017–2019)

**Problem solved:** Sequential processing bottleneck in RNNs/LSTMs.

| Year | Milestone | Engineering Impact |
|------|-----------|-------------------|
| 2017 | [Attention Is All You Need](attention-is-all-you-need.md) | Foundation architecture |
| 2018 | BERT (encoder-only) | Embeddings, classification, reranking |
| 2019 | GPT-2 (decoder-only) | Text generation at scale |

```mermaid
flowchart LR
    RNN[RNN/LSTM] -->|replaced by| TRANS[Transformer]
    TRANS --> ENC[Encoder: BERT]
    TRANS --> DEC[Decoder: GPT]
    TRANS --> ENC_DEC[Encoder-Decoder: T5]
```

**Engineering unlock:** LLM APIs, embedding services, fine-tuning infrastructure.

**Limitation:** Models know only training data — no external knowledge, no actions.

---

## Era 2: Scale + Prompting (2020–2021)

**Problem solved:** How to use one model for many tasks without retraining.

| Year | Milestone | Engineering Impact |
|------|-----------|-------------------|
| 2020 | GPT-3 + [Few-Shot](prompt-engineering-papers.md) | Prompt engineering as discipline |
| 2021 | FLAN (instruction tuning) | Zero-shot task generalization |
| 2021 | Codex | Code generation from prompts |

```mermaid
flowchart TD
    SCALE[Scale to 100B+ params] --> ICL[In-Context Learning]
    ICL --> FS[Few-Shot Examples]
    ICL --> INST[Instructions]
    FS --> PROMPT[Prompt Engineering]
    INST --> PROMPT
```

**Engineering unlock:** Prompt templates, system prompts, API-based AI products.

**Limitation:** Hallucination, no grounding, no multi-step reasoning, no tool use.

---

## Era 3: Alignment + Reasoning (2022)

**Problem solved:** Models that follow instructions, reason step-by-step, and use tools.

| Year | Milestone | Engineering Impact |
|------|-----------|-------------------|
| 2022 | InstructGPT / RLHF | ChatGPT, aligned assistants |
| 2022 | [Chain-of-Thought](prompt-engineering-papers.md) | Step-by-step reasoning |
| 2022 | [ReAct](agent-reasoning-papers.md) | Tool-using agent loop |
| 2022 | Self-Consistency | Majority vote over reasoning paths |

```mermaid
flowchart LR
    ALIGN[RLHF Alignment] --> CHAT[Chat Models]
    COT[Chain-of-Thought] --> REASON[Multi-Step Reasoning]
    REACT[ReAct] --> TOOLS[Tool Use]
    CHAT --> AGENT[Agent Foundation]
    REASON --> AGENT
    TOOLS --> AGENT
```

**Engineering unlock:** Chatbots, function calling, agent frameworks (LangChain).

**Limitation:** Still no external knowledge retrieval, single-agent, no memory across sessions.

---

## Era 4: RAG + Agents (2023)

**Problem solved:** Grounding in external knowledge and autonomous multi-step task execution.

| Year | Milestone | Engineering Impact |
|------|-----------|-------------------|
| 2023 | RAG (Lewis et al., 2020; production adoption) | Vector DBs, retrieval pipelines |
| 2023 | [Tree of Thoughts](agent-reasoning-papers.md) | Deliberate search |
| 2023 | [Reflexion](agent-reasoning-papers.md) | Learning from failure |
| 2023 | [Voyager](agent-reasoning-papers.md) | Skill libraries |
| 2023 | [CAMEL](agent-reasoning-papers.md) | Multi-agent role play |
| 2023 | AutoGPT / BabyAGI | Agent hype cycle begins |

```mermaid
flowchart TD
    RAG[RAG Pipelines] --> GROUND[Grounded Generation]
    REACT2[ReAct + Tools] --> AUTO[Autonomous Agents]
    CAMEL[CAMEL] --> MULTI[Multi-Agent Systems]
    GROUND --> PROD[Production AI Apps]
    AUTO --> PROD
    MULTI --> PROD
```

**Engineering unlock:** Production RAG, agent frameworks (LangGraph, CrewAI), vector databases.

**Limitation:** Naive RAG fails on complex queries; agents lack evaluation and safety.

---

## Era 5: Advanced Patterns (2024)

**Problem solved:** Naive RAG and agent failures at scale.

| Year | Milestone | Engineering Impact |
|------|-----------|-------------------|
| 2024 | [Self-RAG](retrieval-papers.md) | Retrieval reflection |
| 2024 | [GraphRAG](retrieval-papers.md) | Knowledge graph retrieval |
| 2024 | [RAPTOR](retrieval-papers.md) | Hierarchical retrieval |
| 2024 | [CRAG](retrieval-papers.md) | Corrective retrieval |
| 2024 | [SWE-Agent](swe-agent.md) | Coding agent ACI |
| 2024 | [DSPy](dspy.md) | Programmatic prompt optimization |
| 2024 | Devin / Cursor Agent | Commercial coding agents |

```mermaid
flowchart LR
    NAIVE[Naive RAG] --> ADV[Advanced RAG]
    ADV --> SRAG[Self-RAG]
    ADV --> GRAG[GraphRAG]
    ADV --> CRAG[CRAG]
    BASIC[Basic Agents] --> CODE[Coding Agents]
    CODE --> SWE[SWE-Agent ACI]
    MANUAL[Manual Prompts] --> DSPY[DSPy Optimization]
```

**Engineering unlock:** Advanced RAG architectures, coding agent interfaces, systematic prompt optimization.

**Limitation:** Fragmented tool interfaces, no standard agent-tool protocol.

---

## Era 6: Protocols + Standardization (2025)

**Problem solved:** Every agent framework invents its own tool interface.

| Year | Milestone | Engineering Impact |
|------|-----------|-------------------|
| 2025 | [MCP (Model Context Protocol)](../mcp/README.md) | Standardized tool/resource protocol |
| 2025 | A2A (Agent-to-Agent) | Inter-agent communication |
| 2025 | OpenAI function calling maturity | Production tool use |
| 2025 | Agent evaluation frameworks | SWE-bench, AgentBench, custom evals |

```mermaid
flowchart TD
    FRAG[Fragmented Tool APIs] --> MCP[MCP Standard]
    MCP --> SERVER[MCP Servers]
    MCP --> CLIENT[MCP Clients]
    SERVER --> TOOLS2[Tools + Resources + Prompts]
    CLIENT --> AGENT2[Any Agent Framework]
```

**Engineering unlock:** Portable tool servers, multi-framework agent tooling, standardized observability.

**Limitation:** MCP adoption still early; agent reliability and safety remain unsolved.

---

## Era 7: Future (2026+)

See [Future Research](future-research.md) for detailed open problems.

```mermaid
flowchart TD
    NOW[Current: Compound AI Systems] --> EVAL[Eval-Driven Development]
    NOW --> MULTI2[Multi-Agent Orchestration]
    NOW --> MEM[Persistent Agent Memory]
    EVAL --> RELIABLE[Reliable Production Agents]
    MULTI2 --> RELIABLE
    MEM --> RELIABLE
    RELIABLE --> FUTURE[Autonomous Software Teams]
```

**Emerging themes:**
- Compound systems (RAG + agents + tools + eval in one pipeline)
- Test-time compute scaling (o1, inference-time reasoning)
- Agent memory and lifelong learning
- Formal verification of agent outputs
- Cost-optimal routing across models and patterns

---

## How Eras Build on Each Other

```mermaid
flowchart BT
    T[Transformers] --> S[Scale + Prompting]
    S --> A[Alignment + Reasoning]
    A --> R[RAG + Agents]
    R --> AP[Advanced Patterns]
    AP --> P[Protocols]
    P --> F[Future]

    T -.- T2["API: inference"]
    S -.- S2["API: few-shot prompts"]
    A -.- A2["API: function calling"]
    R -.- R2["Stack: vector DB + agent loop"]
    AP -.- AP2["Stack: GraphRAG + SWE-Agent"]
    P -.- P2["Stack: MCP servers"]
```

| Era | You Build | You Consume |
|-----|-----------|-------------|
| Transformers | Fine-tuning pipelines | LLM APIs |
| Prompting | Prompt templates | Chat completions |
| Reasoning | Agent loops | Function calling |
| RAG + Agents | Retrieval + orchestration | Vector DBs + frameworks |
| Advanced | Custom ACI, compilers | DSPy, SWE-bench |
| Protocols | MCP servers | MCP clients |
| Future | Eval infrastructure | Everything above |

---

## Interview Questions

**Q: What did each era add to the previous one?**
Transformers (architecture) → Prompting (task adaptation) → Alignment (safety/quality) → RAG (grounding) → Agents (autonomy) → Protocols (interoperability).

**Q: Why did RAG emerge after ChatGPT?**
Chat models hallucinate and have knowledge cutoffs. RAG grounds generation in retrieved facts without retraining.

**Q: What problem does MCP solve?**
Every agent framework had its own tool interface. MCP standardizes how agents discover and call tools/resources.

**Q: Where are we on the hype cycle?**
Past peak hype for "autonomous AGI agents." Entering productive phase for specific agent applications (coding, support, research) with real evaluation.

**Q: What is the next likely research breakthrough?**
Reliable multi-agent orchestration with formal evaluation, or test-time compute making reasoning models practical at agent-loop cost.

---

## See Also

- [Attention Is All You Need](attention-is-all-you-need.md)
- [Future Research](future-research.md)
- [Engineering Takeaways](engineering-takeaways.md)
- [AI Research Timeline Cheat Sheet](../../cheat-sheets/ai-research-timeline-cheat-sheet.md)

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Initial timeline |
