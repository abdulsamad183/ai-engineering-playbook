"""Configuration via environment variables."""

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_name: str = "ai-app"
    debug: bool = False
    api_key: str = ""
    openai_api_key: str = ""
    log_level: str = "INFO"
    redis_url: str = "redis://localhost:6379/0"
    database_url: str = "sqlite+aiosqlite:///./app.db"


@lru_cache
def get_settings() -> Settings:
    return Settings()
