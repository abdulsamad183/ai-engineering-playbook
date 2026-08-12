# From mini RAG → production starter

> Path from the offline demo to the full RAG template.

## 1. Run the mini (no API keys)

```bash
python3 examples/rag/mini_rag/run.py
```

What you learn: chunk → retrieve → answer with citations (bag-of-words).

## 2. Graduate to the starter

```bash
cp -r templates/engineering/rag-starter my-rag
cd my-rag
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
```

Read [rag-starter README](../../templates/engineering/rag-starter/README.md).

## 3. Capstone

Follow [Capstone: RAG Chat API](../../meta/capstone-walkthrough.md) to add FastAPI, eval, Docker, and CI.

## Handbook

- [RAG hub](../../domains/rag/README.md)
- [Embeddings & Vector DBs](../../domains/embeddings-vector-databases/README.md)
