---
title: "Agent Security"
description: "Agent security — tool permissions, injection, sandboxing, secrets, approval gates, resource limits."
domain: ai-agents
tags: [ai-agents, security, sandbox, injection]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - ../prompt-engineering/prompt-security.md
  - human-in-the-loop.md
keywords: [agent security, tool injection, sandboxing]
author: hp
---

# Agent Security

## Overview

Section **18**.

| Threat | Mitigation |
|--------|------------|
| **Prompt injection** | Delimit untrusted content; system rules |
| **Tool injection** | Validate tool names; registry allowlist |
| **Privilege escalation** | RBAC per tool; least privilege |
| **Secret leakage** | Vault injection; never log secrets |
| **Resource abuse** | Timeouts, CPU/memory caps, step limits |
| **Unsafe code exec** | Sandboxed containers; no network |

## Approval Gates

Destructive tools require HITL — see [Human-in-the-Loop](human-in-the-loop.md).

## Sandboxing

- E2B, Docker, WASM for code execution
- Read-only filesystem default

## Navigation

- [Agent Mistakes](agent-engineering-mistakes.md)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Initial publication |
