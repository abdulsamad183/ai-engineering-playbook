# FastAPI Foundation Examples

| Example | Description | Related Doc |
|---------|-------------|-------------|
| [example-streaming-endpoint.py](example-streaming-endpoint.py) | SSE streaming for LLM responses | [FastAPI Foundation](../../domains/fastapi/fastapi-foundation.md) |
| [example-dependency-injection.py](example-dependency-injection.py) | DI patterns with test overrides | [Backend Fundamentals](../../domains/backend-engineering/backend-fundamentals-for-ai.md) |

## Prerequisites

```bash
pip install fastapi uvicorn httpx pytest
```

## Run Streaming Example

```bash
uvicorn example-streaming-endpoint:app --reload
curl -N http://localhost:8000/v1/chat/stream \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello"}'
```

## Run Tests (DI Example)

```bash
python -c "from example_dependency_injection import test_chat_with_mock; test_chat_with_mock()"
```

## See Also

- [HTTP Fundamentals for AI](../../domains/apis/http-fundamentals-for-ai.md)
- [Python Examples](../python/README.md)
