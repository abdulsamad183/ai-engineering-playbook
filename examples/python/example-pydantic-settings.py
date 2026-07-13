"""Pydantic Settings example for AI applications.

Demonstrates typed configuration, SecretStr for API keys,
environment-specific overrides, and validation.

Prerequisites:
    pip install pydantic pydantic-settings

Run:
    OPENAI_API_KEY=sk-test DATABASE_URL=postgresql://localhost/ai python example-pydantic-settings.py
"""

from __future__ import annotations

from pydantic import Field, SecretStr, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    app_env: str = "development"
    log_level: str = "info"

    database_url: str = Field(..., description="PostgreSQL connection string")
    redis_url: str = "redis://localhost:6379/0"

    openai_api_key: SecretStr = Field(..., description="OpenAI API key")
    llm_model: str = "gpt-4o-mini"
    llm_timeout_seconds: float = 30.0
    max_retries: int = 3

    @field_validator("app_env")
    @classmethod
    def validate_env(cls, v: str) -> str:
        allowed = {"development", "staging", "production"}
        if v not in allowed:
            raise ValueError(f"app_env must be one of {allowed}")
        return v

    @property
    def is_production(self) -> bool:
        return self.app_env == "production"


def main() -> None:
    settings = Settings(
        database_url="postgresql://user:pass@localhost:5432/ai_app",
        openai_api_key="sk-test-key-do-not-commit",
    )

    print(f"Environment: {settings.app_env}")
    print(f"LLM model: {settings.llm_model}")
    print(f"Timeout: {settings.llm_timeout_seconds}s")
    print(f"Production mode: {settings.is_production}")
    # SecretStr prevents accidental logging of the key
    print(f"API key configured: {bool(settings.openai_api_key.get_secret_value())}")


if __name__ == "__main__":
    main()
