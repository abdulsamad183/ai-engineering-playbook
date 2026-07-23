---
title: "Docker for AI Applications"
description: "Docker images, multi-stage builds, Compose, networking, security for AI services."
domain: ai-deployment
tags: [docker, containers, production-ai]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - production-ai-overview.md
  - ../../examples/production-ai/README.md
keywords: [Dockerfile, multi-stage, Docker Compose AI]
author: hp
---

# Docker for AI Applications

## Overview

Section **2**.

## Core Concepts

| Concept | AI usage |
|---------|----------|
| **Image** | Immutable app + deps |
| **Container** | Running API, worker, MCP server |
| **Volume** | Model cache, local index |
| **Network** | API ↔ Redis ↔ Postgres |

## Multi-Stage Dockerfile

```dockerfile
FROM python:3.12-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt -t /deps

FROM python:3.12-slim
WORKDIR /app
COPY --from=builder /deps /deps
COPY src/ ./src
ENV PYTHONPATH=/deps
USER 1000
CMD ["python", "-m", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## Docker Compose (dev)

```yaml
services:
  api:
    build: .
    ports: ["8000:8000"]
    env_file: .env
    depends_on: [redis, postgres]
  redis:
    image: redis:7-alpine
  postgres:
    image: postgres:16-alpine
```

## Security

- Non-root user
- No secrets in image layers
- Scan images in CI

## Build Optimization

- Layer cache: requirements before code
- `.dockerignore` venv, data

## Navigation

- [Deployment Strategies](ai-deployment-strategies.md) · [Examples](../../examples/production-ai/)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Initial publication |
