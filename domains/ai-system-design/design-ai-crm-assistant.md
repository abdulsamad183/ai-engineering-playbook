---
title: "Design: AI CRM Assistant"
description: "CRM AI — customer profiles, memory, opportunities, workflow automation."
domain: ai-system-design
tags: [system-design, crm, sales, recommendations, phase-11]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - design-ai-customer-support.md
keywords: [CRM assistant, opportunity tracking, sales AI]
author: hp
---

# Design: AI CRM Assistant

## Problem Statement

Help sales teams with account intelligence, next-best-action, and automated CRM updates.

## Architecture

```mermaid
flowchart LR
    REP[Sales rep] --> AGENT[CRM agent]
    AGENT --> CRM[(Salesforce API)]
    AGENT --> MEM[Account memory]
    AGENT --> REC[Recommendations]
    AGENT --> WF[Workflow automation]
```

## Components

- **Customer profiles** — aggregate emails, calls, deals
- **Memory** — long-term account narrative
- **Opportunity tracking** — stage suggestions, risk flags
- **Recommendations** — similar won deals, talk tracks
- **Workflow** — log calls, update fields via tools (HITL)

## Evaluation

- Forecast accuracy proxy; rep time saved

## Navigation

- [Voice Agent](design-ai-voice-agent.md)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Phase 11 Section 13 |
