from fastapi import Header

from app.config.settings import Settings, get_settings
from app.core.exceptions import UnauthorizedError


def get_app_settings() -> Settings:
    return get_settings()


async def verify_api_key(
    x_api_key: str | None = Header(default=None),
    settings: Settings = None,  # type: ignore[assignment]
) -> None:
    settings = settings or get_settings()
    if settings.api_key and x_api_key != settings.api_key:
        raise UnauthorizedError()
