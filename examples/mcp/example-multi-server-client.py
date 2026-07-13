"""Multi-server client — route tools by server prefix.

Run: python example-multi-server-client.py
"""

from mcp_protocol import MiniMcpServer


def make_fs_server() -> MiniMcpServer:
    s = MiniMcpServer("filesystem")
    s.register_tool(
        "read_file",
        {"description": "Read file", "inputSchema": {"type": "object", "properties": {"path": {"type": "string"}}, "required": ["path"]}},
        lambda a: f"contents of {a['path']}",
    )
    return s


def make_db_server() -> MiniMcpServer:
    s = MiniMcpServer("postgres")
    s.register_tool(
        "query",
        {"description": "SQL query", "inputSchema": {"type": "object", "properties": {"sql": {"type": "string"}}, "required": ["sql"]}},
        lambda a: f"rows: 0 for {a['sql'][:20]}",
    )
    return s


ROUTES = {"read_file": "filesystem", "query": "postgres"}


def route_call(servers: dict[str, MiniMcpServer], name: str, args: dict) -> dict:
    server_key = ROUTES[name]
    return servers[server_key].handle(
        {"jsonrpc": "2.0", "id": 1, "method": "tools/call", "params": {"name": name, "arguments": args}}
    )


def main() -> None:
    servers = {"filesystem": make_fs_server(), "postgres": make_db_server()}
    print(route_call(servers, "read_file", {"path": "/etc/hosts"}))
    print(route_call(servers, "query", {"sql": "SELECT 1"}))


if __name__ == "__main__":
    main()
