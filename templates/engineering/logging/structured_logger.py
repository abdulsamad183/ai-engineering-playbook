"""Production logging module — structured JSON, correlation IDs, rotation."""

import json
import logging
import sys
import uuid
from contextvars import ContextVar
from logging.handlers import RotatingFileHandler
from typing import Any

request_id_var: ContextVar[str] = ContextVar("request_id", default="")


class JsonFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        payload: dict[str, Any] = {
            "level": record.levelname,
            "message": record.getMessage(),
            "logger": record.name,
            "request_id": request_id_var.get(),
        }
        if hasattr(record, "extra_fields"):
            payload.update(record.extra_fields)  # type: ignore[arg-type]
        return json.dumps(payload)


def setup_logging(*, level: str = "INFO", log_file: str | None = None) -> logging.Logger:
    logger = logging.getLogger("app")
    logger.handlers.clear()
    handler: logging.Handler = logging.StreamHandler(sys.stdout)
    if log_file:
        handler = RotatingFileHandler(log_file, maxBytes=5_000_000, backupCount=5)
    handler.setFormatter(JsonFormatter())
    logger.addHandler(handler)
    logger.setLevel(level)
    return logger


def bind_request_id(value: str | None = None) -> str:
    rid = value or str(uuid.uuid4())
    request_id_var.set(rid)
    return rid
