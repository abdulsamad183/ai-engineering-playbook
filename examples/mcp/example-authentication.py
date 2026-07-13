"""Authentication pattern — API key gate before tool execution.

Run: python example-authentication.py
"""

import os

from mcp_protocol import JsonRpcError, MiniMcpServer


def authorized_tool_handler(args: dict) -> str:
    return f"secret data for {args.get('id')}"


class AuthMcpServer(MiniMcpServer):
    def __init__(self, name: str, api_key: str) -> None:
        super().__init__(name)
        self._api_key = api_key
        self._principal: str | None = None

    def _initialize(self, params: dict) -> dict:
        token = params.get("apiKey") or os.environ.get("MCP_API_KEY")
        if token != self._api_key:
            raise JsonRpcError(-32001, "Unauthorized")
        self._principal = "service-account"
        return super()._initialize(params)

    def _tools_call(self, params: dict) -> dict:
        if not self._principal:
            raise JsonRpcError(-32001, "Not initialized")
        return super()._tools_call(params)


def main() -> None:
    server = AuthMcpServer("secure-server", api_key="dev-key-123")
    server.register_tool(
        "fetch_record",
        {"description": "Fetch record", "inputSchema": {"type": "object", "properties": {"id": {"type": "string"}}, "required": ["id"]}},
        authorized_tool_handler,
    )
    bad = server.handle({"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"apiKey": "wrong"}})
    good = server.handle({"jsonrpc": "2.0", "id": 2, "method": "initialize", "params": {"apiKey": "dev-key-123"}})
    call = server.handle({"jsonrpc": "2.0", "id": 3, "method": "tools/call", "params": {"name": "fetch_record", "arguments": {"id": "42"}}})
    print("bad:", bad)
    print("good:", good)
    print("call:", call)


if __name__ == "__main__":
    main()
