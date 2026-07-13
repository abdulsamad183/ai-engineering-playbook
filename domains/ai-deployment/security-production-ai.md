---
title: "Production AI Security"
description: "Auth, prompt injection, tool security, tenant isolation, rate limiting."
domain: ai-deployment
tags: [security, production, prompt-injection, phase-12]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - ../mcp/mcp-security.md
  - ../ai-agents/agent-security.md
keywords: [production security, tenant isolation, rate limiting]
author: hp
---

# Production AI Security

## Overview

Section **12** of Phase 12.

## Controls

- **Authentication** — JWT at API edge
- **Authorization** — RBAC per tenant/resource
- **Prompt injection** — separate untrusted content; tool approval
- **Tool security** — sandbox, allow lists
- **Rate limiting** — per user/IP/API key
- **Tenant isolation** — row-level security; separate indexes

## API Protection

- WAF, request size limits
- Output moderation filter

## Navigation

- [Performance](performance-optimization-production.md)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Phase 12 Section 12 |
