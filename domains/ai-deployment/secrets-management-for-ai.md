---
title: "Secrets Management for AI"
description: "Env vars, rotation, Vault, API keys, secure configuration."
domain: ai-deployment
tags: [secrets, security, api-keys]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - security-production-ai.md
keywords: [secrets management, API key rotation, Vault]
author: hp
---

# Secrets Management for AI

## Overview

Section **5**.

## Practices

- **Never** commit `.env` or keys
- Inject at runtime: K8s secrets, AWS SM, Vault
- Separate keys per environment
- Rotate LLM keys quarterly; automate where possible

## API Key Management

| Scope | Pattern |
|-------|---------|
| Server-side | Platform holds keys |
| User-delegated | OAuth to SaaS tools |

## Python

```python
import os
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]  # fail fast if missing
```

## Navigation

- [Monitoring](monitoring-ai-systems.md)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Initial publication |
