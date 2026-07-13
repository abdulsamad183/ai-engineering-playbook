"""MCP server with tool, resource, and prompt registration."""

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("playbook-mcp-starter")


@mcp.tool()
def search_docs(query: str) -> str:
    """Search internal documentation."""
    return f"Results for: {query}"


@mcp.resource("docs://index")
def docs_index() -> str:
    return "# Documentation index"


@mcp.prompt()
def summarize_prompt(text: str) -> str:
    return f"Summarize the following:\n\n{text}"


if __name__ == "__main__":
    mcp.run(transport="stdio")
