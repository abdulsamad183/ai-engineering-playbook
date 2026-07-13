"""Structured logging with correlation IDs.

Run: python example-structured-logging.py
"""

import json
import logging
import uuid

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger("ai")


def log_event(event: str, request_id: str, **kwargs) -> None:
    logger.info(json.dumps({"event": event, "request_id": request_id, **kwargs}))


def handle_request(path: str) -> None:
    request_id = uuid.uuid4().hex
    log_event("request_start", request_id, path=path)
    log_event("llm_call", request_id, model="gpt-4", latency_ms=420)
    log_event("request_end", request_id, status=200)


if __name__ == "__main__":
    handle_request("/chat")
