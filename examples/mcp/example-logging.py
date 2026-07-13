"""Structured logging for MCP requests.

Run: python example-logging.py
"""

import json
import logging
import time

from mcp_protocol import MiniMcpServer

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger("mcp")


class LoggingMcpServer(MiniMcpServer):
    def handle(self, message: dict) -> dict | None:
        request_id = message.get("id")
        method = message.get("method")
        start = time.perf_counter()
        resp = super().handle(message)
        ms = (time.perf_counter() - start) * 1000
        logger.info(json.dumps({"event": "mcp_request", "method": method, "request_id": request_id, "latency_ms": round(ms, 2)}))
        return resp


def main() -> None:
    server = LoggingMcpServer("logged-server")
    server.register_tool("ping", {"description": "Ping", "inputSchema": {"type": "object", "properties": {}}}, lambda _: "pong")
    server.handle({"jsonrpc": "2.0", "id": 1, "method": "tools/call", "params": {"name": "ping", "arguments": {}}})


if __name__ == "__main__":
    main()
