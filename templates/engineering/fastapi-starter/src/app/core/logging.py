import json
import logging
import sys
from typing import Any


def setup_logging(level: str = "INFO") -> None:
    logging.basicConfig(level=level, stream=sys.stdout, format="%(message)s")


def log_event(logger: logging.Logger, event: str, **fields: Any) -> None:
    logger.info(json.dumps({"event": event, **fields}))
