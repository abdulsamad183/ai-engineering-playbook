"""
Mini chat API with a mock LLM (stdlib HTTP server, no FastAPI required).

Run:
  python examples/llm-applications/mini_chat_api/server.py
Then:
  python examples/llm-applications/mini_chat_api/client.py
"""
from __future__ import annotations

import json
from http.server import BaseHTTPRequestHandler, HTTPServer


def mock_llm(messages: list[dict]) -> str:
    last = messages[-1]["content"] if messages else ""
    return f"echo: {last}"


class Handler(BaseHTTPRequestHandler):
    def do_POST(self):  # noqa: N802
        if self.path != "/v1/chat":
            self.send_error(404)
            return
        length = int(self.headers.get("Content-Length", "0"))
        body = json.loads(self.rfile.read(length) or b"{}")
        reply = mock_llm(body.get("messages", []))
        payload = json.dumps({"reply": reply}).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def log_message(self, fmt, *args):  # quieter
        print("[server]", fmt % args)


def main() -> None:
    host, port = "127.0.0.1", 8765
    print(f"listening on http://{host}:{port}/v1/chat")
    HTTPServer((host, port), Handler).serve_forever()


if __name__ == "__main__":
    main()
