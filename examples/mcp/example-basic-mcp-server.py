"""Basic MCP-style server over STDIO.

Run: python example-basic-mcp-server.py
Test with: python example-basic-mcp-client.py
"""

from mcp_protocol import MiniMcpServer


def echo_handler(args: dict) -> str:
    return args.get("text", "")


def main() -> None:
    server = MiniMcpServer("basic-server")
    server.register_tool(
        "echo",
        {
            "description": "Echo input text",
            "inputSchema": {
                "type": "object",
                "properties": {"text": {"type": "string"}},
                "required": ["text"],
            },
        },
        echo_handler,
    )
    server.serve_stdio()


if __name__ == "__main__":
    main()
