"""Structured logging example for AI applications.

Demonstrates JSON logging, correlation IDs, and safe logging
(without PII or secrets).

Run: python example-structured-logging.py
"""

from __future__ import annotations

import json
import logging
import sys
import uuid
from contextvars import ContextVar
from datetime import UTC, datetime

request_id_var: ContextVar[str] = ContextVar("request_id", default="")


class JSONFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        log_entry = {
            "timestamp": datetime.now(UTC).isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "request_id": request_id_var.get(),
        }
        if hasattr(record, "extra_fields"):
            log_entry.update(record.extra_fields)
        return json.dumps(log_entry)


def setup_logging(level: str = "INFO") -> logging.Logger:
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(JSONFormatter())
    root = logging.getLogger()
    root.handlers = [handler]
    root.setLevel(level)
    return logging.getLogger("ai_app")


def log_llm_call(
    logger: logging.Logger,
    model: str,
    input_tokens: int,
    output_tokens: int,
    latency_ms: float,
) -> None:
    record = logger.makeRecord(
        logger.name,
        logging.INFO,
        "",
        0,
        "llm_call_completed",
        (),
        None,
    )
    record.extra_fields = {
        "event": "llm_call_completed",
        "model": model,
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "latency_ms": latency_ms,
        # Never log: prompt content, API keys, user PII
    }
    logger.handle(record)


def main() -> None:
    logger = setup_logging()
    request_id_var.set(str(uuid.uuid4()))

    logger.info("Processing chat request")
    log_llm_call(
        logger,
        model="gpt-4o-mini",
        input_tokens=150,
        output_tokens=80,
        latency_ms=1234.5,
    )
    logger.info("Request completed")


if __name__ == "__main__":
    main()
