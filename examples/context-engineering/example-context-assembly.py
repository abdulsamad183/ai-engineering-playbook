"""Context assembly — merge sources into message list.

Run: python example-context-assembly.py
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ContextBlock:
    source: str
    content: str


class ContextAssembler:
    def __init__(self, system_template: str):
        self.system_template = system_template

    def assemble(
        self,
        blocks: list[ContextBlock],
        user_message: str,
    ) -> list[dict[str, str]]:
        context_body = "\n\n".join(
            f'<{b.source}>\n{b.content}\n</{b.source}>' for b in blocks
        )
        system = self.system_template.replace("{{context}}", context_body)
        return [
            {"role": "system", "content": system},
            {"role": "user", "content": user_message},
        ]


if __name__ == "__main__":
    assembler = ContextAssembler(
        "Answer using only:\n{{context}}\nIf unknown, say so."
    )
    blocks = [
        ContextBlock("policy", "Refunds in 3 business days."),
        ContextBlock("memory", "User tier: enterprise"),
    ]
    messages = assembler.assemble(blocks, "How fast is my refund?")
    print(messages[0]["content"][:200])
