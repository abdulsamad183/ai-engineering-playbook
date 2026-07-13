---
title: "Configuration and Secrets"
description: "Production configuration management for AI applications — environment variables, secrets, API keys, Pydantic settings, hierarchy, and secure storage patterns."
domain: foundations
tags: [foundations, configuration, secrets, security, pydantic, production, intermediate]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - software-engineering-for-ai.md
  - testing-fundamentals.md
  - ../python-engineering/python-for-ai-engineering.md
  - ../backend-engineering/backend-fundamentals-for-ai.md
  - ../logging/logging-and-error-handling.md
keywords: [environment variables, pydantic-settings, secrets manager, API keys, twelve-factor, configuration hierarchy, dotenv]
author: hp
---

# Configuration and Secrets

> How to manage environment-specific settings and sensitive credentials in AI services — without leaking API keys, breaking deployments, or hardcoding provider details in application code.

## Table of Contents

- [Why Configuration Matters for AI](#why-configuration-matters-for-ai)
- [Configuration Hierarchy](#configuration-hierarchy)
- [Environment Variables and .env Files](#environment-variables-and-env-files)
- [Pydantic Settings](#pydantic-settings)
- [API Keys and Provider Credentials](#api-keys-and-provider-credentials)
- [Environment-Specific Configuration](#environment-specific-configuration)
- [Secure Storage Patterns](#secure-storage-patterns)
- [Configuration Loading Lifecycle](#configuration-loading-lifecycle)
- [Validation and Fail-Fast](#validation-and-fail-fast)
- [Testing with Configuration](#testing-with-configuration)
- [Best Practices](#best-practices)
- [Production Considerations](#production-considerations)
- [Common Mistakes](#common-mistakes)
- [Interview Preparation](#interview-preparation)
- [Navigation](#navigation)

---

## Why Configuration Matters for AI

AI applications depend on more external configuration than typical CRUD APIs: LLM provider keys, embedding model names, vector store URLs, rate limits, token budgets, feature flags for new models, and observability endpoints.
When configuration is scattered across code, shell scripts, and undocumented `.env` files, every deploy becomes a guessing game.

| Failure Mode | Typical Cause | Engineering Fix |
|--------------|---------------|-----------------|
| Production calls dev OpenAI project | Wrong API key in env | Explicit `APP_ENV` + secret isolation per environment |
| Staging uses production vector DB | Shared `DATABASE_URL` | Environment-specific config sources |
| Service starts but LLM calls fail | Missing key discovered at runtime | Pydantic validation at startup |
| Key leaked in GitHub | `.env` committed | `.gitignore`, secret scanning, never commit secrets |
| Cannot reproduce bug locally | Undocumented env vars | `.env.example` + typed settings class |

> **Production Standard:** Configuration is data, not code. Load it once at startup, validate it immediately, inject it through dependencies — never read `os.environ` ad hoc in business logic.

See [Software Engineering for AI](software-engineering-for-ai.md) for where settings fit in layered architecture, and [Backend Fundamentals for AI](../backend-engineering/backend-fundamentals-for-ai.md) for wiring settings into FastAPI lifespan and dependency injection.

```mermaid
graph TB
  subgraph "Configuration Sources (priority high → low)"
    CLI[CLI / Runtime Overrides]
    ENV[Environment Variables]
    SECRETS[Secret Manager]
    ENVFILE[".env (local dev only)"]
    DEFAULTS[Code Defaults]
  end

  subgraph "Application"
    SETTINGS[Pydantic Settings]
    DI[Dependency Injection]
    SVC[Services / AI Logic]
  end

  CLI --> SETTINGS
  ENV --> SETTINGS
  SECRETS --> ENV
  ENVFILE --> SETTINGS
  DEFAULTS --> SETTINGS
  SETTINGS --> DI
  DI --> SVC
```

---

## Configuration Hierarchy

Production systems resolve configuration from multiple layers.
Later layers override earlier ones.
Document this hierarchy so every engineer knows which value wins.

### Recommended Precedence (Highest Wins)

| Priority | Source | When Used |
|----------|--------|-----------|
| 1 | CLI flags / runtime overrides | One-off debugging, integration tests |
| 2 | Process environment variables | Docker, Kubernetes, CI, production |
| 3 | Secret manager injection | Production credentials at deploy time |
| 4 | `.env` file | Local development only |
| 5 | Code defaults | Safe fallbacks for non-secret values |

```mermaid
flowchart LR
  A[Defaults in code] --> B[".env (dev)"]
  B --> C[Secret Manager → env]
  C --> D[Container/K8s env]
  D --> E[CLI override]
  E --> F[Resolved Settings]
```

**Twelve-Factor alignment:** Store config in the environment.
The codebase stays identical across dev, staging, and production; only injected config changes.

### What Belongs Where

| Setting Type | Example | Storage |
|--------------|---------|---------|
| Secret | `OPENAI_API_KEY` | Secret manager / env (never in repo) |
| Environment marker | `APP_ENV=production` | Env var |
| Tunable behavior | `LLM_TIMEOUT_SECONDS=30` | Env var with code default |
| Feature flag | `ENABLE_AGENT_MODE=true` | Env or feature-flag service |
| Non-secret default | `LLM_MODEL=gpt-4o-mini` | Code default, overridable via env |
| Local-only convenience | `LOG_LEVEL=debug` | `.env` for dev |

---

## Environment Variables and .env Files

### Naming Conventions

Use a consistent prefix to avoid collisions and make grepping easy:

```bash
# Application
APP_ENV=development
APP_NAME=ai-assistant
LOG_LEVEL=info

# Infrastructure
DATABASE_URL=postgresql+asyncpg://user:pass@localhost:5432/ai_app
REDIS_URL=redis://localhost:6379/0

# AI providers
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
LLM_MODEL=gpt-4o-mini
EMBEDDING_MODEL=text-embedding-3-small

# Observability
OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317
```

| Convention | Rationale |
|------------|-----------|
| `SCREAMING_SNAKE_CASE` | Standard for Unix environment variables |
| Grouped prefixes (`LLM_`, `DB_`) | Easier scanning in dashboards and docs |
| No secrets in variable names | `OPENAI_API_KEY`, not `SECRET_OPENAI` |

### `.env` for Local Development

`.env` files are a **developer convenience**, not a production config mechanism.

```bash
# .env.example — commit this; never commit .env
APP_ENV=development
APP_NAME=ai-assistant
LOG_LEVEL=debug

DATABASE_URL=postgresql+asyncpg://postgres:postgres@localhost:5432/ai_app_dev
REDIS_URL=redis://localhost:6379/0

# Replace with your keys — obtain from provider dashboard
OPENAI_API_KEY=sk-your-key-here
LLM_MODEL=gpt-4o-mini
LLM_TIMEOUT_SECONDS=30
MAX_RETRIES=3

# Optional: vector store
PINECONE_API_KEY=
PINECONE_INDEX_NAME=
```

```gitignore
# Never commit real secrets
.env
.env.local
.env.*.local
```

> **Warning:** `.env` in Docker images or committed to Git is one of the most common causes of credential leaks in AI startups.
> Use `.env.example` as documentation; inject real values via your orchestrator or secret manager in non-local environments.

### Loading `.env` Safely

```python
# Only load dotenv in local/dev — production should rely on injected env
import os

def maybe_load_dotenv() -> None:
    if os.getenv("APP_ENV", "development") == "development":
        from dotenv import load_dotenv
        load_dotenv(override=False)  # do not override existing env vars
```

`override=False` ensures CI and Docker-injected variables take precedence over `.env` when both exist.

---

## Pydantic Settings

[Pydantic Settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/) (`pydantic-settings`) is the production standard for typed, validated configuration in Python AI services.
It integrates with FastAPI and aligns with patterns in [Python for AI Engineering](../python-engineering/python-for-ai-engineering.md).

### Base Settings Class

```python
# src/app/config/settings.py
from functools import lru_cache
from typing import Literal

from pydantic import Field, SecretStr, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",  # ignore unknown env vars — avoids deploy failures on typos in platform
    )

    # Application
    app_env: Literal["development", "staging", "production"] = "development"
    app_name: str = "ai-assistant"
    log_level: Literal["debug", "info", "warning", "error"] = "info"

    # Database
    database_url: str = Field(..., description="Async SQLAlchemy URL")
    redis_url: str = "redis://localhost:6379/0"

    # LLM
    openai_api_key: SecretStr = Field(..., min_length=10)
    llm_model: str = "gpt-4o-mini"
    llm_timeout_seconds: float = Field(default=30.0, gt=0, le=300)
    max_retries: int = Field(default=3, ge=0, le=10)

    # RAG / embeddings
    embedding_model: str = "text-embedding-3-small"
    chunk_size: int = Field(default=512, ge=128, le=4096)
    retrieval_top_k: int = Field(default=5, ge=1, le=50)

    @field_validator("database_url")
    @classmethod
    def validate_database_url(cls, v: str) -> str:
        if not v.startswith(("postgresql", "sqlite")):
            raise ValueError("database_url must be postgresql or sqlite")
        return v

    @property
    def is_production(self) -> bool:
        return self.app_env == "production"

    def safe_repr(self) -> dict:
        """Dict safe for logging — secrets redacted."""
        data = self.model_dump()
        data["openai_api_key"] = "***"
        return data


@lru_cache
def get_settings() -> Settings:
    """Singleton settings — parse env once per process."""
    return Settings()
```

### Nested Settings with `env_nested_delimiter`

Complex AI apps group provider config:

```python
from pydantic import BaseModel, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class OpenAIConfig(BaseModel):
    api_key: SecretStr
    model: str = "gpt-4o-mini"
    base_url: str | None = None  # for Azure OpenAI or proxies


class VectorStoreConfig(BaseModel):
    provider: str = "pinecone"
    api_key: SecretStr | None = None
    index_name: str = "documents"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_nested_delimiter="__",
        env_file=".env",
    )

    app_env: str = "development"
    openai: OpenAIConfig
    vector_store: VectorStoreConfig
```

Environment variables:

```bash
OPENAI__API_KEY=sk-...
OPENAI__MODEL=gpt-4o-mini
VECTOR_STORE__PROVIDER=pinecone
VECTOR_STORE__API_KEY=pc-...
VECTOR_STORE__INDEX_NAME=prod-docs
```

### FastAPI Integration

```python
from fastapi import Depends, FastAPI
from app.config.settings import Settings, get_settings

app = FastAPI()


@app.on_event("startup")
async def validate_config() -> None:
    settings = get_settings()
    if settings.is_production and settings.log_level == "debug":
        raise RuntimeError("Refusing to start: debug logging in production")


def get_app_settings() -> Settings:
    return get_settings()


@app.get("/health")
async def health(settings: Settings = Depends(get_app_settings)) -> dict:
    return {"status": "ok", "env": settings.app_env}
```

See [Backend Fundamentals for AI](../backend-engineering/backend-fundamentals-for-ai.md) for lifespan hooks and dependency injection patterns.

---

## API Keys and Provider Credentials

AI services typically hold keys for multiple providers.
Treat each as a **secret credential**, not a configuration string.

### Provider Key Inventory

| Provider | Typical Env Var | Rotation Notes |
|----------|-----------------|----------------|
| OpenAI | `OPENAI_API_KEY` | Project-scoped keys; set spend limits |
| Anthropic | `ANTHROPIC_API_KEY` | Separate keys per environment |
| Azure OpenAI | `AZURE_OPENAI_API_KEY` + endpoint URL | Often paired with `AZURE_OPENAI_ENDPOINT` |
| Cohere | `COHERE_API_KEY` | |
| Pinecone | `PINECONE_API_KEY` | Index-level access in newer plans |
| Hugging Face | `HF_TOKEN` | For inference endpoints |

### Never Log or Serialize Secrets

```python
from pydantic import SecretStr

settings = get_settings()

# WRONG — may appear in logs, traces, error reports
logger.info("Starting with key %s", settings.openai_api_key)

# CORRECT — SecretStr repr is '**********'
logger.info("OpenAI configured", extra={"model": settings.llm_model})

# When you need the raw value for the SDK client
api_key = settings.openai_api_key.get_secret_value()
```

### Multi-Provider Abstraction

Keep provider selection in config; inject the right client via DI:

```python
# domain/ports/llm.py — interface from software-engineering-for-ai.md
from abc import ABC, abstractmethod


class LLMClient(ABC):
    @abstractmethod
    async def complete(self, prompt: str) -> str: ...


# infrastructure/llm/factory.py
from app.config.settings import Settings


def build_llm_client(settings: Settings) -> LLMClient:
    if settings.llm_provider == "openai":
        from infrastructure.llm.openai_client import OpenAIClient
        return OpenAIClient(
            api_key=settings.openai_api_key.get_secret_value(),
            model=settings.llm_model,
            timeout=settings.llm_timeout_seconds,
        )
    if settings.llm_provider == "anthropic":
        from infrastructure.llm.anthropic_client import AnthropicClient
        return AnthropicClient(...)
    raise ValueError(f"Unsupported LLM provider: {settings.llm_provider}")
```

---

## Environment-Specific Configuration

### Three-Environment Model

| Environment | Purpose | Secret Source | Data |
|-------------|---------|---------------|------|
| `development` | Local engineer machines | `.env` / personal dev keys | Synthetic or anonymized |
| `staging` | Pre-production validation | Staging secret manager | Copy or subset of prod schema |
| `production` | Live traffic | Production secret manager | Real user data |

```mermaid
graph TB
  subgraph "development"
    DEV[Local .env]
    DEVKEY[Dev API keys / low limits]
  end

  subgraph "staging"
    STG[CI/CD injects staging secrets]
    STGKEY[Staging keys — separate billing]
  end

  subgraph "production"
    PROD[K8s / ECS secret refs]
    PRODKEY[Prod keys — rotation policy]
  end

  DEV --> DEVKEY
  STG --> STGKEY
  PROD --> PRODKEY
```

### Environment-Specific Files (Optional Pattern)

Some teams use layered env files — use sparingly; prefer platform injection in cloud:

```
config/
  settings.py          # Pydantic model (single source of truth)
.env.example           # Documented template
.env                   # Local only (gitignored)
```

Avoid `settings_production.py` with hardcoded values.
Behavior differences belong in env vars, not duplicate code paths.

### Feature Flags and Model Routing

```python
class Settings(BaseSettings):
    enable_reranking: bool = False
    enable_agent_tools: bool = False
    llm_fallback_model: str = "gpt-4o-mini"

    def resolve_model(self, primary: str | None = None) -> str:
        return primary or self.llm_model
```

Route expensive models only in production when flagged:

```python
if settings.app_env == "production" and settings.enable_premium_model:
    model = "gpt-4o"
else:
    model = settings.llm_fallback_model
```

---

## Secure Storage Patterns

### Local Development

| Approach | Security Level | Notes |
|----------|----------------|-------|
| `.env` file | Low | Acceptable locally; never in images |
| `direnv` | Low–Medium | Auto-loads per-directory env |
| 1Password / Vault CLI | Medium | `op run -- env` injects at process start |

### Cloud / Production

| Service | Use Case |
|---------|----------|
| AWS Secrets Manager / SSM Parameter Store | ECS, Lambda, EKS |
| GCP Secret Manager | Cloud Run, GKE |
| Azure Key Vault | Azure Container Apps |
| HashiCorp Vault | Multi-cloud, dynamic secrets |
| Doppler / Infisical | Developer-friendly secret sync |

```mermaid
sequenceDiagram
  participant Deploy as CI/CD Pipeline
  participant SM as Secret Manager
  participant Orch as Orchestrator
  participant Pod as App Container

  Deploy->>SM: Fetch secrets at deploy
  SM-->>Deploy: OPENAI_API_KEY, DATABASE_URL
  Deploy->>Orch: Register task with secret refs
  Orch->>Pod: Inject as env vars at runtime
  Pod->>Pod: Pydantic validates on startup
```

### Secret Rotation

1. **Dual-key window** — support old and new key in config during rotation.
2. **Automated rotation** — secret manager generates new value; restart pods.
3. **Audit** — log key version/id, never the value.
4. **Blast radius** — per-environment, per-service keys; not one master key.

```python
class Settings(BaseSettings):
    openai_api_key: SecretStr
    openai_api_key_previous: SecretStr | None = None  # optional during rotation

    def openai_keys_for_retry(self) -> list[str]:
        keys = [self.openai_api_key.get_secret_value()]
        if self.openai_api_key_previous:
            keys.append(self.openai_api_key_previous.get_secret_value())
        return keys
```

---

## Configuration Loading Lifecycle

```mermaid
sequenceDiagram
  participant Main as main.py
  participant Settings as Pydantic Settings
  participant Env as Environment
  participant App as FastAPI App

  Main->>Env: Process starts
  Main->>Settings: get_settings() — first call
  Settings->>Env: Read env vars + optional .env
  Settings->>Settings: Validate types & constraints
  alt Validation fails
    Settings-->>Main: ValidationError — exit non-zero
  end
  Main->>App: Create app with validated settings
  App->>App: Wire DI — DB, LLM, cache clients
```

**Fail fast:** A misconfigured AI service should not start and accept traffic.
Silent defaults (e.g., wrong model, zero timeout) cause expensive incidents.

```python
import sys
from pydantic import ValidationError

try:
    settings = get_settings()
except ValidationError as exc:
    print("Configuration error — fix environment variables:", file=sys.stderr)
    print(exc)
    sys.exit(1)
```

---

## Validation and Fail-Fast

### Cross-Field Validation

```python
from pydantic import model_validator


class Settings(BaseSettings):
    app_env: str = "development"
    openai_api_key: SecretStr
    anthropic_api_key: SecretStr | None = None
    llm_provider: str = "openai"

    @model_validator(mode="after")
    def check_provider_key_present(self) -> "Settings":
        if self.llm_provider == "openai" and not self.openai_api_key:
            raise ValueError("openai_api_key required when llm_provider=openai")
        if self.llm_provider == "anthropic" and not self.anthropic_api_key:
            raise ValueError("anthropic_api_key required when llm_provider=anthropic")
        return self
```

### Production Guardrails

```python
@model_validator(mode="after")
def production_safety_checks(self) -> "Settings":
    if self.app_env == "production":
        if self.log_level == "debug":
            raise ValueError("debug log_level not allowed in production")
        if "localhost" in self.database_url:
            raise ValueError("localhost database_url not allowed in production")
    return self
```

---

## Testing with Configuration

Override settings in tests — never read production `.env` in CI.

```python
# tests/conftest.py
import pytest
from app.config.settings import Settings, get_settings
from app.main import app


@pytest.fixture
def test_settings() -> Settings:
    return Settings(
        app_env="development",
        database_url="sqlite+aiosqlite:///:memory:",
        redis_url="redis://localhost:6379/15",
        openai_api_key="sk-test-fake-key-not-real",
        llm_model="gpt-4o-mini",
        log_level="warning",
    )


@pytest.fixture
def client(test_settings: Settings):
    app.dependency_overrides[get_settings] = lambda: test_settings
    from fastapi.testclient import TestClient
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()
```

See [Testing Fundamentals](testing-fundamentals.md) for fixtures, mocking, and API testing patterns.

```python
# Use monkeypatch for unit tests without FastAPI
def test_chunk_size_bounds(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "sk-test")
    monkeypatch.setenv("DATABASE_URL", "sqlite:///test.db")
    monkeypatch.setenv("CHUNK_SIZE", "99999")
    with pytest.raises(ValidationError):
        Settings()
```

---

## Best Practices

| Practice | Why |
|----------|-----|
| Single `Settings` class | One place to document and validate all config |
| `@lru_cache` on `get_settings()` | Parse once; consistent values across requests |
| `SecretStr` for credentials | Prevents accidental logging and serialization |
| Commit `.env.example` | Onboarding without sharing real secrets |
| Prefix env vars (`LLM_`, `DB_`) | Clarity in large deployments |
| Validate at startup | Fail deploy, not first user request |
| Inject settings via DI | Testable; no global `os.environ` reads |
| Separate keys per environment | Limits blast radius of leaks and misconfig |
| Document required vars in README | Reduces "works on my machine" |
| Version config schema changes | Breaking env renames need migration notes |

### Configuration Checklist for New AI Services

- [ ] `Settings` class with typed fields and validators
- [ ] `.env.example` with every required variable documented
- [ ] `.env` in `.gitignore`
- [ ] Secret manager wired in staging/production
- [ ] No secrets in Dockerfiles, logs, or OpenAPI responses
- [ ] CI uses injected test credentials, not developer keys
- [ ] Startup health check confirms config loaded (not secret values)

---

## Production Considerations

- **Immutable config per deploy** — reload settings only on process restart; avoid mid-flight env mutation.
- **Config vs. secrets** — non-sensitive tunables can live in ConfigMaps; credentials in Secret objects with encryption at rest.
- **Sidecar injection** — some platforms mount secrets as files; use `SettingsConfigDict(secrets_dir="/run/secrets")` for file-based secrets.
- **Cost controls** — configure `max_tokens`, rate limits, and model defaults via env so ops can tune without redeploying code.
- **Observability** — log `app_env`, `llm_model`, and config version — never secret values. See [Logging and Error Handling](../logging/logging-and-error-handling.md).
- **Compliance** — EU deployments may require region-specific endpoints; express as config (`OPENAI_BASE_URL`, `DATA_RESIDENCY=eu`).
- **12-factor parity** — dev/staging/prod run the same container image; only injected config differs.

---

## Common Mistakes

| Mistake | Impact | Fix |
|---------|--------|-----|
| Committing `.env` to Git | Credential leak, account compromise | `.gitignore`, secret scanning, rotate keys |
| Reading `os.environ` in services | Untestable, inconsistent | Central `Settings` + DI |
| Logging full settings dump | API keys in log aggregators | `safe_repr()` with redaction |
| Shared prod keys in dev | Accidental prod data/billing | Per-environment keys |
| No validation on startup | Runtime failures on first LLM call | Pydantic `Settings` at import/startup |
| Secrets in Docker `ARG`/`ENV` | Visible in image layers | Runtime injection from orchestrator |
| Hardcoding model names in code | Cannot roll back model without deploy | `LLM_MODEL` env var |
| `override=True` on dotenv | Local file overwrites CI secrets | `override=False` |
| Storing prompts with secrets inline | Secrets in prompt templates | Load from env/settings only |
| One `.env` for all developers | Key sharing, no audit trail | Personal dev keys or shared dev vault |

---

## Interview Preparation

### Frequently Asked Questions

**Q1: How do you manage configuration in a production AI service?**

> **Strong answer:** Single Pydantic Settings class loaded once at startup from environment variables, with optional `.env` for local dev only. Secrets use `SecretStr`, injected via secret manager in cloud. Settings wired through FastAPI DI. Validate cross-field rules (provider + key) and fail fast on boot. Never hardcode API keys or environment-specific URLs.

**Q2: What is the difference between config and secrets?**

> **Strong answer:** Config is non-sensitive tunables (log level, model name, timeout) — can live in ConfigMaps or env with less restriction. Secrets are credentials (API keys, DB passwords) — encrypted at rest, least-privilege access, rotation policy, never logged or committed. Both load through the same Settings abstraction but secrets get `SecretStr` and stricter handling.

**Q3: How do you test code that depends on environment variables?**

> **Strong answer:** Construct `Settings` directly in tests with explicit values, or use `monkeypatch.setenv` + dependency overrides in FastAPI. Never depend on a developer's `.env` in CI. Use fake keys for unit tests; integration tests may use sandbox provider keys from CI secrets.

**Q4: How would you rotate an OpenAI API key without downtime?**

> **Strong answer:** Support dual keys during rotation window (`OPENAI_API_KEY` + `OPENAI_API_KEY_PREVIOUS`), retry auth failures with secondary key, deploy new key to secret manager, restart pods gradually, remove old key after traffic stabilizes, audit access logs.

### Real-World Scenario

**Scenario:** A junior engineer commits `.env` containing production OpenAI and Pinecone keys to a public GitHub repo.

> **Discussion points:** Immediate key rotation in provider dashboards; enable GitHub secret scanning; audit git history; move to secret manager; add pre-commit hook for secret detection; use `.env.example` only; review spend and access logs for abuse.

---

## Navigation

### Prerequisites

- [Software Engineering for AI](software-engineering-for-ai.md) — configuration management overview, layered architecture
- [Python for AI Engineering](../python-engineering/python-for-ai-engineering.md) — Pydantic basics, project layout

### Related Topics

- [Backend Fundamentals for AI](../backend-engineering/backend-fundamentals-for-ai.md) — DI, lifespan, health checks
- [Testing Fundamentals](testing-fundamentals.md) — overriding settings in pytest
- [Logging and Error Handling](../logging/logging-and-error-handling.md) — safe logging without leaking secrets

### Next Topics

- [Testing Fundamentals](testing-fundamentals.md)
- [Logging and Error Handling](../logging/logging-and-error-handling.md)
- [Security Domain](../security/README.md)

### Future Reading

- [CICD Domain](../cicd/README.md) — injecting secrets in pipelines
- [Cloud Deployment](../cloud-deployment/README.md) — platform-specific secret wiring
- [Docker Domain](../docker/README.md) — avoiding secrets in images

---

## See Also

- [Foundations Domain README](README.md)
- [Software Engineering for AI — Configuration Management](software-engineering-for-ai.md#configuration-management)
- [Master Index](../../meta/indexes/MASTER-INDEX.md)

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Initial version |
