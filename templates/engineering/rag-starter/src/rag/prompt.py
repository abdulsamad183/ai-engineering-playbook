"""Prompt assembly with citations."""

from rag.retrieval import Retriever, rerank


def build_rag_prompt(query: str, retriever: Retriever, top_n: int = 3) -> tuple[str, list[dict]]:
    docs = rerank(query, retriever.retrieve(query), top_n=top_n)
    context = "\n\n".join(f"[{i+1}] {d['text']}" for i, d in enumerate(docs))
    prompt = (
        "Answer using only the context. Cite sources as [n].\n\n"
        f"Context:\n{context}\n\nQuestion: {query}"
    )
    return prompt, docs
