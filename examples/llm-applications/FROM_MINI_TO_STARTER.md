# From mini chat API → FastAPI starter

> Path from the stdlib mock server to the FastAPI production template.

## 1. Run the mini (no API keys)

```bash
# terminal 1
python3 examples/llm-applications/mini_chat_api/server.py
# terminal 2
python3 examples/llm-applications/mini_chat_api/client.py
```

What you learn: request/response chat contract and local HTTP loop.

## 2. Graduate to FastAPI starter

```bash
cp -r templates/engineering/fastapi-starter my-api
cd my-api
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
uvicorn app.main:app --reload
```

Read [fastapi-starter README](../../templates/engineering/fastapi-starter/README.md).

## 3. Combine with RAG

Use the FastAPI starter + [rag-starter](../../templates/engineering/rag-starter/README.md) via the [Capstone walkthrough](../../meta/capstone-walkthrough.md).

## Handbook

- [LLM Application Development](../../domains/llm-application-development/README.md)
- [FastAPI domain](../../domains/fastapi/README.md) (Reference)
