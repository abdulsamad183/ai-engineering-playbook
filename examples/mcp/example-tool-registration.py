"""Tool registration pattern — schema + handler registry.

Run: python example-tool-registration.py
"""

from mcp_protocol import MiniMcpServer


def search_tickets(args: dict) -> str:
    q = args["query"]
    return f'[{{"id":1,"title":"{q} match"}}]'


def main() -> None:
    server = MiniMcpServer("ticket-tools")
    server.register_tool(
        "search_tickets",
        {
            "description": "Search support tickets",
            "inputSchema": {
                "type": "object",
                "properties": {"query": {"type": "string"}},
                "required": ["query"],
            },
        },
        search_tickets,
    )
    # Demo: handle one request inline
    resp = server.handle(
        {"jsonrpc": "2.0", "id": 1, "method": "tools/call", "params": {"name": "search_tickets", "arguments": {"query": "refund"}}}
    )
    print(resp)


if __name__ == "__main__":
    main()
