---
title: "Agent Communication"
description: "Message passing, shared memory, negotiation, coordination, synchronization, conflict resolution."
domain: ai-agents
tags: [ai-agents, communication, coordination, A2A, phase-8]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - multi-agent-systems.md
  - ../a2a/README.md
keywords: [agent communication, message passing, shared memory, negotiation]
author: hp
---

# Agent Communication

## Overview

Section **13** of Phase 8. Foundation for [A2A](../a2a/README.md) phase.

| Mechanism | Description |
|-----------|-------------|
| **Message passing** | Structured messages between agents |
| **Shared memory** | Blackboard / Redis / DB |
| **Context sharing** | Scoped slices of state |
| **Negotiation** | Agents agree on plan split |
| **Synchronization** | Locks, leases on shared artifacts |
| **Conflict resolution** | Supervisor tie-break; last-writer-wins forbidden for critical data |

## Production Rules

- Version shared artifacts
- Audit all cross-agent messages
- Tenant scope on every shared store

## Navigation

- [Agent Frameworks](frameworks/README.md)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Phase 8 Section 13 |
