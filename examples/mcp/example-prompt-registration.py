"""Prompt registration — reusable protocol templates.

Run: python example-prompt-registration.py
"""

from mcp_protocol import MiniMcpServer


def code_review_prompt(args: dict) -> list[dict]:
    lang = args.get("language", "python")
    return [
        {"role": "user", "content": f"Review this {lang} code for bugs and style."},
    ]


def main() -> None:
    server = MiniMcpServer("prompt-server")
    server.register_prompt(
        "code_review",
        {"description": "Code review template", "arguments": [{"name": "language", "required": False}]},
        code_review_prompt,
    )
    resp = server.handle(
        {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "prompts/get",
            "params": {"name": "code_review", "arguments": {"language": "rust"}},
        }
    )
    print(resp)


if __name__ == "__main__":
    main()
