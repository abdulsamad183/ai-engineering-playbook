"""RAG-ready prompt assembly — system + retrieved context + user query.

Run: python example-rag-prompt.py
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class RetrievedChunk:
    doc_id: str
    text: str
    score: float


RAG_SYSTEM_PROMPT = """You are a helpful assistant that answers questions using only the provided context.

Rules:
- Answer ONLY from the <context> block. If the answer is not in context, say "I don't have enough information."
- Cite sources using [doc_id] inline after claims.
- Do not use outside knowledge.
- Be concise. Use bullet points for multi-part answers.
"""

RAG_USER_TEMPLATE = """<context>
{context_block}
</context>

<question>
{question}
</question>
"""


def format_context(chunks: list[RetrievedChunk], max_chars: int = 8000) -> str:
    """Build delimited context block with budget."""
    parts: list[str] = []
    used = 0
    for chunk in chunks:
        block = f'<source id="{chunk.doc_id}" score="{chunk.score:.3f}">\n{chunk.text}\n</source>'
        if used + len(block) > max_chars:
            break
        parts.append(block)
        used += len(block)
    return "\n".join(parts)


def build_rag_messages(question: str, chunks: list[RetrievedChunk]) -> list[dict[str, str]]:
    context = format_context(chunks)
    return [
        {"role": "system", "content": RAG_SYSTEM_PROMPT},
        {"role": "user", "content": RAG_USER_TEMPLATE.format(context_block=context, question=question)},
    ]


if __name__ == "__main__":
    sample_chunks = [
        RetrievedChunk("policy-12", "Refunds process within 5 business days.", 0.92),
        RetrievedChunk("policy-07", "Enterprise plans include SSO.", 0.81),
    ]
    messages = build_rag_messages("How long do refunds take?", sample_chunks)
    for m in messages:
        print(f"--- {m['role']} ---\n{m['content'][:200]}...\n")
