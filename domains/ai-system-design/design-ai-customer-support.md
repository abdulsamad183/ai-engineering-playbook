---
title: "Design: AI Customer Support"
description: "Support AI — ticket routing, CRM, tools, escalation, memory, evaluation."
domain: ai-system-design
tags: [system-design, customer-support, crm, hitl]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - design-ai-crm-assistant.md
  - ../ai-agents/human-in-the-loop.md
keywords: [customer support AI, escalation, ticket routing]
author: hp
---

# Design: AI Customer Support

## Problem Statement

Resolve tier-1 support with KB grounding, CRM tools, and human escalation.

## Functional Requirements

- Chat/email channel
- Ticket create/update via tools
- Order lookup, refund policy Q&A
- Escalate to human with summary

## Architecture

```mermaid
flowchart TB
    USER[Customer] --> BOT[Support agent]
    BOT --> RAG[KB RAG]
    BOT --> CRM[CRM tools]
    BOT --> ROUTE[Intent router]
    ROUTE --> HUMAN[Human queue]
    BOT --> PG[(Conversation history)]
```

## Components

- **Ticket routing** — intent classifier → queue
- **Memory** — customer profile + past tickets
- **Tool calling** — read-only default; write with approval
- **Evaluation** — resolution rate, CSAT, escalation rate

## Security

- Tenant isolation; PII redaction in logs

## Navigation

- [AI Coding Assistant](design-ai-coding-assistant.md)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Initial publication |
