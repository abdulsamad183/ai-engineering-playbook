"""HTTP transport concept — JSON-RPC over POST (simplified).

Production: use MCP streamable HTTP / SSE. This shows request/response shape.

Run: python example-http-transport.py
"""

import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from threading import Thread

from mcp_protocol import MiniMcpServer


server = MiniMcpServer("http-demo")
server.register_tool(
    "ping",
    {"description": "Ping", "inputSchema": {"type": "object", "properties": {}}},
    lambda _args: "pong",
)


class Handler(BaseHTTPRequestHandler):
    def do_POST(self) -> None:
        length = int(self.headers.get("Content-Length", 0))
        body = json.loads(self.rfile.read(length))
        resp = server.handle(body)
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(resp).encode())

    def log_message(self, *_args) -> None:
        pass


def main() -> None:
    httpd = HTTPServer(("127.0.0.1", 8765), Handler)
    thread = Thread(target=httpd.serve_forever, daemon=True)
    thread.start()
    import urllib.request

    req = urllib.request.Request(
        "http://127.0.0.1:8765",
        data=json.dumps({"jsonrpc": "2.0", "id": 1, "method": "tools/call", "params": {"name": "ping", "arguments": {}}}).encode(),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req) as resp:
        print(resp.read().decode())
    httpd.shutdown()


if __name__ == "__main__":
    main()
