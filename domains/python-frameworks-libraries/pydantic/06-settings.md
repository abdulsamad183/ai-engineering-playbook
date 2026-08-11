---
title: "Pydantic: Settings Management"
description: "Type-safe configuration from environment variables."
domain: python-frameworks-libraries
tags: [pydantic, settings]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# Pydantic: Settings Management

> Type-safe configuration from environment variables.

## Definition

**`BaseSettings`** (via `pydantic-settings`) loads config from environment variables and `.env` files with validation — better than raw `os.environ`.

## Important APIs

| API | Use |
|-----|-----|
| `BaseSettings` | Settings model |
| `SettingsConfigDict` | env file / prefix |
| env names | Field names uppercased by default |

## Code

```python
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    openai_api_key: str = Field(min_length=1)
    app_env: str = "dev"
    request_timeout_s: float = 30.0

# settings = Settings()  # reads OPENAI_API_KEY, APP_ENV, ...
```

## Uses

- 12-factor config for AI services
- Fail fast on missing secrets at startup

---

## Continue

- **Hub:** [Pydantic hub](README.md)
- **Frameworks overview:** [Python Frameworks & Libraries](../README.md)
