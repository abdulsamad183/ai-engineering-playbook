"""STDIO transport — subprocess pipes for local MCP servers.

Run: python example-stdio-transport.py
"""

import subprocess
import sys
from pathlib import Path

from mcp_protocol import MiniMcpClient


def main() -> None:
    here = Path(__file__).parent
    proc = subprocess.Popen(
        [sys.executable, "example-basic-mcp-server.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        text=True,
        cwd=here,
    )
    client = MiniMcpClient(proc)
    client.initialize()
    print("STDIO transport OK — tools:", client.list_tools())
    proc.terminate()


if __name__ == "__main__":
    main()
