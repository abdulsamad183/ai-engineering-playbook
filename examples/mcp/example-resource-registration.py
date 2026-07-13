"""Resource registration — URI-addressable context.

Run: python example-resource-registration.py
"""

from mcp_protocol import MiniMcpServer


def main() -> None:
    server = MiniMcpServer("resource-server")
    server.register_resource(
        "policy://refund",
        {"name": "Refund Policy", "mimeType": "text/plain"},
        lambda: "Refunds within 30 days with receipt.",
    )
    resp = server.handle(
        {"jsonrpc": "2.0", "id": 1, "method": "resources/read", "params": {"uri": "policy://refund"}}
    )
    print(resp)


if __name__ == "__main__":
    main()
