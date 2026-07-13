---
title: "Test File Template"
description: "Backend test file template for FastAPI AI services."
type: backend-template
---

# Test File Template

## conftest.py

```python
import pytest
from httpx import ASGITransport, AsyncClient

from my_ai_api.main import create_app
from my_ai_api.api.dependencies import get_llm_client, get_db_session


class MockLLMClient:
    async def complete(self, messages, model=None):
        return LLMResponse(content="mock response", model="mock", total_tokens=10)


@pytest.fixture
def app():
    application = create_app()
    application.dependency_overrides[get_llm_client] = lambda: MockLLMClient()
    yield application
    application.dependency_overrides.clear()


@pytest.fixture
async def client(app):
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac
```

## API Test

```python
import pytest


@pytest.mark.asyncio
async def test_create_conversation(client):
    response = await client.post(
        "/api/v1/conversations",
        json={"title": "Test"},
        headers={"Authorization": "Bearer test-token"},
    )
    assert response.status_code == 201
    data = response.json()
    assert "id" in data["data"]
```

## Service Unit Test

```python
@pytest.mark.asyncio
async def test_chat_service_not_found():
    mock_repo = AsyncMock(spec=ConversationRepository)
    mock_repo.get_by_id.return_value = None
    service = ChatService(repo=mock_repo, llm=MockLLMClient(), logger=logging.getLogger("test"))

    with pytest.raises(ConversationNotFoundError):
        await service.send_message(ChatRequest(conversation_id="x", message="hi"), user_id="u1")
```

## See Also

- [Testing Backend for AI](../../../domains/backend-engineering/testing-backend-for-ai.md)
