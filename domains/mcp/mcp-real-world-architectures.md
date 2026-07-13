---
title: "Real-World MCP Architectures"
description: "Production architectures — coding assistant, enterprise KB, research agent, multi-agent, internal tools, ops."
domain: mcp
tags: [mcp, architecture, case-study, production, phase-9]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - multi-server-mcp.md
  - ../ai-agents/agent-case-studies.md
keywords: [MCP architecture, case study, enterprise]
author: hp
---

# Real-World MCP Architectures

## Overview

Section **20** of Phase 9 — six production architecture patterns.

---

## 1. AI Coding Assistant

```mermaid
flowchart LR
    IDE[IDE Host] --> C[MCP Client]
    C --> FS[Filesystem Server]
    C --> GIT[Git Server]
    C --> LINT[Linter Server]
    FS & GIT & LINT --> REPO[Codebase]
```

- **Transport:** STDIO subprocess per server
- **Tools:** `read_file`, `search`, `run_tests`
- **Resources:** `file://` URIs for open tabs
- **Security:** Workspace root sandbox

---

## 2. Enterprise Knowledge Platform

```mermaid
flowchart TB
    AGENT[Support Agent] --> R[MCP Router]
    R --> RAG[RAG Resource Server]
    R --> CRM[CRM Tool Server]
    R --> POL[Policy Prompt Server]
    RAG --> VDB[(Vector DB)]
    CRM --> SF[Salesforce API]
```

- **Resources:** chunked doc URIs with citations
- **Prompts:** `escalation`, `refund_policy` templates
- **Auth:** OAuth per user; CRM tools scoped

---

## 3. AI Research Agent

- **Servers:** web fetch (read-only), arXiv, notebook execution (sandboxed)
- **Streaming:** long PDF summarization via progress notifications
- **Pattern:** read resources → synthesize → cite URIs in output

---

## 4. Multi-Agent Platform

- **Supervisor agent** holds MCP client pool
- **Worker agents** receive delegated tool subsets
- **Router** namespaces tools per agent role
- See [Multi-Agent Systems](../ai-agents/multi-agent-systems.md)

---

## 5. Internal Tool Platform

- Central registry of approved MCP servers
- Golden schemas; CI validates tool contracts
- Developers publish servers; platform team certifies

---

## 6. AI Operations Dashboard

- **Resources:** live metrics streams (`metrics://service/latency`)
- **Tools:** `scale_replicas`, `rollback_deploy` (HITL gated)
- **Observability:** every tool call → audit + trace

---

## Comparison Table

| Architecture | Servers | Transport | Critical concern |
|--------------|---------|-----------|------------------|
| Coding assistant | 3–5 local | STDIO | Filesystem sandbox |
| Enterprise KB | 3+ remote | HTTP | Tenant ACL |
| Research agent | 2–4 | Mixed | Untrusted content |
| Multi-agent | N × M | HTTP | Tool namespace |
| Internal platform | Catalog | HTTP | Schema CI |
| Ops dashboard | 2 | HTTP | HITL on writes |

## Interview Preparation

**Whiteboard:** Design MCP for a bank — read-only market data resources, trade tools with dual approval, air-gapped STDIO for core banking, full audit.

## Navigation

- [Comparison Guides](mcp-comparison-guides.md) · [Phase 9 Hub](README.md)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Phase 9 Section 20 |
