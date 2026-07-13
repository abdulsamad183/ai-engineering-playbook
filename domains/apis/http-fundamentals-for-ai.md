---
title: "HTTP Fundamentals for AI"
description: "Production-ready HTTP, REST, authentication, and API design fundamentals for AI engineers building LLM-powered applications."
domain: apis
tags: [api, foundations, security, backend, production, interview]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - ../foundations/ai-engineering-overview.md
  - ../backend-engineering/backend-fundamentals-for-ai.md
  - ../fastapi/fastapi-foundation.md
  - ../security/README.md
  - ../foundations/configuration-and-secrets.md
keywords: [HTTP, REST, JSON, JWT, OAuth, API versioning, pagination, streaming, webhooks, rate limiting, FastAPI]
author: hp
---

# HTTP Fundamentals for AI

> The HTTP and API foundations every AI engineer needs — from request lifecycle to streaming completions, authentication to rate limiting — with production patterns for LLM-powered services.

## Table of Contents

- [Why HTTP Matters for AI Engineers](#why-http-matters-for-ai-engineers)
- [HTTP Fundamentals](#http-fundamentals)
- [The HTTP Request Lifecycle](#the-http-request-lifecycle)
- [REST Principles](#rest-principles)
- [JSON as the Lingua Franca](#json-as-the-lingua-franca)
- [CRUD Operations](#crud-operations)
- [HTTP Status Codes](#http-status-codes)
- [Authentication](#authentication)
- [Authorization](#authorization)
- [JWT Overview](#jwt-overview)
- [OAuth Overview](#oauth-overview)
- [API Versioning](#api-versioning)
- [Pagination](#pagination)
- [Streaming Responses](#streaming-responses)
- [Webhooks](#webhooks)
- [Rate Limiting](#rate-limiting)
- [API Security](#api-security)
- [AI API Architecture](#ai-api-architecture)
- [Production Considerations](#production-considerations)
- [Common Mistakes](#common-mistakes)
- [Best Practices](#best-practices)
- [Interview Preparation](#interview-preparation)
- [Navigation](#navigation)

---

## Why HTTP Matters for AI Engineers

AI applications are distributed systems. Whether you are calling OpenAI's chat completions API, exposing a RAG endpoint to a frontend, or receiving webhook callbacks from a document processor, **HTTP is the transport layer that connects every component**.

| AI Engineering Task | HTTP Concept Involved |
|---------------------|----------------------|
| Streaming chat UI | Server-Sent Events (SSE), chunked transfer |
| RAG document upload | `multipart/form-data`, `POST`, file size limits |
| Agent tool calls | REST endpoints, JSON request/response bodies |
| LLM provider integration | Bearer token auth, rate limits, retry on 429 |
| User-facing AI API | JWT auth, versioning, pagination |
| Async job completion | Webhooks, idempotency, signature verification |
| Production monitoring | Status codes, health endpoints, structured errors |

> **Production Standard:** If you cannot explain what happens between `curl` and your FastAPI handler — headers, status codes, auth, timeouts — you will ship fragile AI services that fail silently under load.

For the broader engineering context, see [AI Engineering Overview](../foundations/ai-engineering-overview.md) and [Backend Fundamentals for AI](../backend-engineering/backend-fundamentals-for-ai.md).

---

## HTTP Fundamentals

**HTTP (Hypertext Transfer Protocol)** is a stateless, request-response protocol. A client sends a request; a server returns a response. Every AI API interaction — inbound and outbound — follows this model.

### Core Components of an HTTP Message

**Request:**

```
POST /v1/chat/completions HTTP/1.1
Host: api.openai.com
Authorization: Bearer sk-...
Content-Type: application/json
Content-Length: 142

{"model": "gpt-4o", "messages": [{"role": "user", "content": "Hello"}]}
```

**Response:**

```
HTTP/1.1 200 OK
Content-Type: application/json
Transfer-Encoding: chunked

{"id": "chatcmpl-abc", "choices": [{"message": {"content": "Hi!"}}]}
```

### Request Line and Method

| Part | Example | Purpose |
|------|---------|---------|
| Method | `POST` | What action to perform |
| Path | `/v1/chat/completions` | Resource identifier |
| Version | `HTTP/1.1` | Protocol version |

### HTTP Methods

| Method | Idempotent | Safe | Typical Use in AI Apps |
|--------|------------|------|------------------------|
| `GET` | Yes | Yes | Fetch conversation history, list documents |
| `POST` | No | No | Send chat message, trigger embedding job |
| `PUT` | Yes | No | Replace entire user profile or config |
| `PATCH` | No* | No | Update prompt template fields |
| `DELETE` | Yes | No | Remove document from vector store index |
| `HEAD` | Yes | Yes | Check resource existence without body |
| `OPTIONS` | Yes | Yes | CORS preflight |

*PATCH idempotency depends on implementation.

### Headers

Headers carry metadata. AI services rely heavily on specific headers:

| Header | Direction | Purpose |
|--------|-----------|---------|
| `Authorization` | Request | API keys, JWT bearer tokens |
| `Content-Type` | Both | `application/json`, `text/event-stream` |
| `Accept` | Request | Client's expected response format |
| `X-Request-ID` | Both | Distributed tracing correlation |
| `X-RateLimit-Remaining` | Response | Quota visibility for clients |
| `Retry-After` | Response | Seconds to wait after 429 |
| `Idempotency-Key` | Request | Prevent duplicate charges or jobs |

### HTTP Versions

| Version | Relevance to AI |
|---------|-----------------|
| HTTP/1.1 | Default; supports chunked transfer for streaming |
| HTTP/2 | Multiplexing; used by most cloud load balancers |
| HTTP/3 | QUIC-based; lower latency for mobile clients |

For AI streaming, HTTP/1.1 chunked transfer and HTTP/2 both work. What matters is that your framework and reverse proxy do not buffer the entire response before forwarding.

### Stateless vs Stateful

HTTP is **stateless** — each request is independent. Conversation memory in chat apps is **application state**, stored in a database or cache and keyed by session ID, not held in the HTTP connection.

```python
# Conversation state belongs in your data layer, not in HTTP
class ConversationStore:
    async def append_message(self, session_id: str, role: str, content: str) -> None:
        await self.db.execute(
            "INSERT INTO messages (session_id, role, content) VALUES ($1, $2, $3)",
            session_id, role, content,
        )
```

---

## The HTTP Request Lifecycle

Understanding the full path a request takes prevents debugging blind spots in production AI services.

```mermaid
sequenceDiagram
    participant Client as Client (Browser / SDK)
    participant DNS as DNS Resolver
    participant LB as Load Balancer
    participant Proxy as Reverse Proxy
    participant App as FastAPI App
    participant Auth as Auth Middleware
    participant Svc as AI Service Layer
    participant LLM as LLM Provider API

    Client->>DNS: Resolve api.example.com
    DNS-->>Client: IP address
    Client->>LB: HTTPS POST /v1/chat
    LB->>Proxy: Forward request (TLS terminated)
    Proxy->>App: HTTP request
    App->>Auth: Validate JWT / API key
    Auth-->>App: User context (sub, scopes)
    App->>Svc: chat_completion(user_id, message)
    Svc->>LLM: POST /v1/chat/completions
    LLM-->>Svc: Stream tokens (SSE)
    Svc-->>App: Async generator
    App-->>Proxy: text/event-stream response
    Proxy-->>LB: Chunked forward
    LB-->>Client: Streamed response
```

### Lifecycle Stages

1. **DNS resolution** — Client resolves hostname to IP.
2. **TLS handshake** — Encrypted channel established (HTTPS).
3. **Load balancing** — Request routed to a healthy backend instance.
4. **Reverse proxy** — Nginx/Envoy may handle TLS, compression, rate limits.
5. **Application routing** — Framework matches path to handler.
6. **Middleware chain** — Auth, logging, CORS, request ID injection.
7. **Business logic** — Service layer orchestrates AI calls.
8. **External API call** — Outbound HTTP to LLM provider.
9. **Response assembly** — JSON or streamed body returned.
10. **Client rendering** — Frontend parses SSE or JSON.

### Timeouts at Each Layer

| Layer | Typical Timeout | Failure Symptom |
|-------|-----------------|-----------------|
| Client | 30–120s | UI shows "request failed" |
| Load balancer | 60s | 504 Gateway Timeout |
| Reverse proxy | 60s | 502 Bad Gateway |
| App server | Configurable | Hung workers |
| LLM provider | 30–600s | Partial stream, then disconnect |

> **Production Standard:** Set timeouts at every layer. An LLM call that hangs forever consumes a worker and eventually exhausts your connection pool.

---

## REST Principles

**REST (Representational State Transfer)** is an architectural style for designing networked APIs. Most AI product APIs are RESTful or REST-inspired, even when they also support streaming.

### REST Constraints (Practical View)

| Constraint | AI Application Example |
|------------|------------------------|
| Client-server | React frontend ↔ FastAPI backend |
| Stateless | Each request includes auth token; no server-side session in HTTP |
| Cacheable | `GET /documents` responses cacheable with `ETag` |
| Uniform interface | Resources identified by URLs, manipulated via HTTP methods |
| Layered system | Client → CDN → API gateway → service → database |
| Code on demand (optional) | Rare in AI APIs; occasionally SDK-driven behavior |

### Resource Naming

Use **nouns**, not verbs. Actions that do not map cleanly to CRUD become sub-resources or RPC-style endpoints (pragmatic exception).

```
# Good — resource-oriented
GET    /v1/conversations
POST   /v1/conversations
GET    /v1/conversations/{id}/messages
POST   /v1/conversations/{id}/messages
POST   /v1/documents              # upload for RAG
DELETE /v1/documents/{id}

# Acceptable — action sub-resource when CRUD is awkward
POST   /v1/documents/{id}/reindex
POST   /v1/conversations/{id}/summarize

# Avoid — verb in URL
POST   /v1/createConversation
GET    /v1/getDocumentById
```

### FastAPI REST Example

```python
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, Field
from uuid import UUID

router = APIRouter(prefix="/v1/conversations", tags=["conversations"])


class MessageCreate(BaseModel):
    content: str = Field(..., min_length=1, max_length=32_000)


class MessageResponse(BaseModel):
    id: UUID
    role: str
    content: str


@router.get("/{conversation_id}/messages", response_model=list[MessageResponse])
async def list_messages(
    conversation_id: UUID,
    user_id: str = Depends(get_current_user_id),
    service: ConversationService = Depends(get_conversation_service),
):
    return await service.list_messages(conversation_id, user_id)


@router.post(
    "/{conversation_id}/messages",
    response_model=MessageResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_message(
    conversation_id: UUID,
    body: MessageCreate,
    user_id: str = Depends(get_current_user_id),
    service: ConversationService = Depends(get_conversation_service),
):
    try:
        return await service.add_user_message(conversation_id, user_id, body.content)
    except ConversationNotFound:
        raise HTTPException(status_code=404, detail="Conversation not found")
```

---

## JSON as the Lingua Franca

**JSON (JavaScript Object Notation)** is the default serialization format for AI APIs — for both your own services and every major LLM provider.

### Why JSON Dominates AI APIs

- Human-readable for debugging prompts and responses
- Native support in Python (`pydantic`), JavaScript, and every LLM SDK
- Schema validation via JSON Schema / OpenAPI
- Efficient enough for text payloads (not for raw embeddings at scale — use binary or dedicated formats)

### Request and Response Structure

```json
{
  "model": "gpt-4o",
  "messages": [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Explain RAG in one paragraph."}
  ],
  "temperature": 0.7,
  "stream": true
}
```

### Pydantic Models for Type Safety

Never pass raw dicts through your service layer. Use Pydantic models at API boundaries.

```python
from pydantic import BaseModel, Field
from typing import Literal


class ChatMessage(BaseModel):
    role: Literal["system", "user", "assistant", "tool"]
    content: str


class ChatCompletionRequest(BaseModel):
    messages: list[ChatMessage] = Field(..., min_length=1)
    model: str = "gpt-4o-mini"
    temperature: float = Field(0.7, ge=0.0, le=2.0)
    stream: bool = False


class ChatCompletionResponse(BaseModel):
    id: str
    content: str
    model: str
    input_tokens: int
    output_tokens: int
```

### JSON Error Responses

Use a consistent error envelope across your API:

```json
{
  "error": {
    "code": "CONTEXT_LENGTH_EXCEEDED",
    "message": "Input exceeds model context window of 128000 tokens.",
    "details": {"token_count": 135000, "max_tokens": 128000},
    "request_id": "req_abc123"
  }
}
```

### JSON Limitations in AI Systems

| Limitation | Mitigation |
|------------|------------|
| No binary support | Base64-encode files, or use `multipart/form-data` for uploads |
| Large embedding arrays | Consider MessagePack, Arrow, or dedicated vector DB APIs |
| No streaming JSON standard | Use SSE (`text/event-stream`) or NDJSON for token streams |
| Schema drift from LLMs | Validate LLM output with Pydantic `model_validate_json()` |

---

## CRUD Operations

**CRUD** maps HTTP methods to persistent resource operations. In AI applications, CRUD applies to conversations, documents, prompts, agents, and configuration — not to individual LLM inference calls (those are actions).

### CRUD Mapping

| Operation | HTTP Method | Path Example | AI Resource |
|-----------|-------------|--------------|-------------|
| Create | `POST` | `/v1/documents` | Upload document for RAG |
| Read (one) | `GET` | `/v1/documents/{id}` | Fetch document metadata |
| Read (list) | `GET` | `/v1/documents` | List indexed documents |
| Update (full) | `PUT` | `/v1/prompts/{id}` | Replace prompt template |
| Update (partial) | `PATCH` | `/v1/agents/{id}` | Update agent tool list |
| Delete | `DELETE` | `/v1/documents/{id}` | Remove from index |

### Status Codes for CRUD

| Operation | Success Code | Body |
|-----------|--------------|------|
| Create | `201 Created` | Created resource + `Location` header |
| Read | `200 OK` | Resource or list |
| Update | `200 OK` or `204 No Content` | Updated resource or empty |
| Delete | `204 No Content` | Empty |

### FastAPI CRUD for RAG Documents

```python
@router.post("/documents", status_code=status.HTTP_201_CREATED)
async def upload_document(
    file: UploadFile,
    user_id: str = Depends(get_current_user_id),
    service: DocumentService = Depends(get_document_service),
):
    doc = await service.ingest(file, user_id)
    return JSONResponse(
        status_code=201,
        content=doc.model_dump(mode="json"),
        headers={"Location": f"/v1/documents/{doc.id}"},
    )


@router.get("/documents/{doc_id}")
async def get_document(doc_id: UUID, user_id: str = Depends(get_current_user_id), ...):
    ...


@router.delete("/documents/{doc_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_document(doc_id: UUID, user_id: str = Depends(get_current_user_id), ...):
    await service.delete(doc_id, user_id)
```

---

## HTTP Status Codes

Status codes communicate outcome without parsing the body. AI engineers must use them precisely — clients, SDKs, and retry logic depend on them.

### Code Categories

| Range | Meaning | Client Action |
|-------|---------|---------------|
| 1xx | Informational | Wait (rare in REST) |
| 2xx | Success | Process response |
| 3xx | Redirection | Follow `Location` (rare in APIs) |
| 4xx | Client error | Fix request; generally do not retry |
| 5xx | Server error | Retry with backoff |

### Essential Status Codes for AI APIs

| Code | Name | When to Use in AI Apps |
|------|------|------------------------|
| `200` | OK | Successful read, update, or non-streaming completion |
| `201` | Created | New conversation, document, or agent created |
| `202` | Accepted | Async embedding job queued |
| `204` | No Content | Successful delete |
| `400` | Bad Request | Invalid prompt, malformed JSON, schema violation |
| `401` | Unauthorized | Missing or invalid auth token |
| `403` | Forbidden | Valid auth but insufficient permissions |
| `404` | Not Found | Conversation or document does not exist |
| `409` | Conflict | Duplicate idempotency key or version conflict |
| `413` | Payload Too Large | Document exceeds upload limit |
| `422` | Unprocessable Entity | Pydantic validation failure (FastAPI default) |
| `429` | Too Many Requests | Rate limit or LLM quota exceeded |
| `500` | Internal Server Error | Unhandled exception |
| `502` | Bad Gateway | LLM provider returned unexpected error |
| `503` | Service Unavailable | Circuit breaker open, model overloaded |
| `504` | Gateway Timeout | LLM provider did not respond in time |

### Mapping LLM Provider Errors

```python
import httpx
from fastapi import HTTPException


PROVIDER_STATUS_MAP = {
    400: 400,   # bad prompt → 400
    401: 502,   # our key bad → 502 (don't leak provider auth details)
    429: 429,   # rate limit → 429
    500: 502,   # provider error → 502
    503: 503,   # overloaded → 503
}


async def call_llm_with_status_mapping(client: httpx.AsyncClient, payload: dict) -> dict:
    response = await client.post("/v1/chat/completions", json=payload)
    if response.is_success:
        return response.json()
    mapped = PROVIDER_STATUS_MAP.get(response.status_code, 502)
    raise HTTPException(
        status_code=mapped,
        detail={"provider_status": response.status_code, "message": response.text[:500]},
    )
```

### Structured Error Handler in FastAPI

```python
from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={
            "error": {
                "code": "VALIDATION_ERROR",
                "message": "Request validation failed",
                "details": exc.errors(),
                "request_id": request.state.request_id,
            }
        },
    )
```

---

## Authentication

**Authentication** answers: *Who is making this request?* AI APIs must authenticate both inbound requests (users calling your service) and outbound requests (your service calling LLM providers).

### Authentication Methods

| Method | Use Case | AI Example |
|--------|----------|------------|
| API key (header) | Service-to-service, LLM providers | `Authorization: Bearer sk-...` |
| API key (query) | Legacy; avoid in production | `?api_key=...` (leaks in logs) |
| Basic auth | Internal tools, dev environments | Username/password base64 |
| Bearer token (JWT) | User-facing apps | `Authorization: Bearer eyJ...` |
| OAuth 2.0 | Third-party integrations, SSO | "Sign in with Google" |
| mTLS | High-security service mesh | Certificate-based mutual auth |

### API Key Authentication (FastAPI)

```python
from fastapi import Security, HTTPException, status
from fastapi.security import APIKeyHeader

api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)


async def verify_api_key(
    api_key: str | None = Security(api_key_header),
    settings: Settings = Depends(get_settings),
) -> str:
    if not api_key or api_key != settings.api_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API key",
            headers={"WWW-Authenticate": "ApiKey"},
        )
    return api_key
```

### Storing API Keys

Never hardcode keys. Use environment variables or a secrets manager. See [Configuration and Secrets](../foundations/configuration-and-secrets.md).

```python
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    openai_api_key: str
    internal_api_key: str

    model_config = {"env_file": ".env", "extra": "ignore"}
```

### Inbound vs Outbound Auth

| Direction | Pattern |
|-----------|---------|
| Inbound (users → your API) | JWT for users, API keys for B2B partners |
| Outbound (your API → OpenAI) | Provider API key in `Authorization` header |
| Outbound (your API → internal services) | Service account JWT or mTLS |

---

## Authorization

**Authorization** answers: *Is this authenticated identity allowed to perform this action on this resource?* Authentication without authorization is a common AI security gap.

### Authentication vs Authorization

| | Authentication | Authorization |
|---|----------------|---------------|
| Question | Who are you? | What can you do? |
| Failure code | `401 Unauthorized` | `403 Forbidden` |
| Mechanism | Login, API key, JWT | Roles, scopes, policies |
| AI example | Valid user token | User can only read their own conversations |

### Role-Based Access Control (RBAC)

```python
from enum import Enum


class Role(str, Enum):
    VIEWER = "viewer"
    EDITOR = "editor"
    ADMIN = "admin"


ROLE_PERMISSIONS = {
    Role.VIEWER: {"conversations:read"},
    Role.EDITOR: {"conversations:read", "conversations:write", "documents:write"},
    Role.ADMIN: {"*"},
}


def require_permission(permission: str):
    async def checker(user: User = Depends(get_current_user)):
        perms = ROLE_PERMISSIONS.get(user.role, set())
        if "*" not in perms and permission not in perms:
            raise HTTPException(status_code=403, detail="Insufficient permissions")
        return user
    return checker


@router.delete("/documents/{doc_id}")
async def delete_document(
    doc_id: UUID,
    user: User = Depends(require_permission("documents:write")),
    ...
):
    ...
```

### Resource-Level Authorization

Always verify the user owns the resource — not just that they are authenticated.

```python
async def get_conversation_for_user(
    conversation_id: UUID,
    user_id: str,
    repo: ConversationRepository,
) -> Conversation:
    conversation = await repo.get(conversation_id)
    if not conversation or conversation.user_id != user_id:
        raise HTTPException(status_code=404, detail="Conversation not found")
    return conversation
```

> Return `404` instead of `403` when a resource does not exist or is not owned — prevents enumeration attacks.

---

## JWT Overview

**JWT (JSON Web Token)** is a compact, self-contained token format for transmitting claims between parties. Widely used for user sessions in AI applications.

### JWT Structure

```
eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1c2VyMTIzIiwicm9sZSI6ImVkaXRvciJ9.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
|______Header______|.|_____________Payload_____________|.|_______Signature_______|
```

| Part | Content |
|------|---------|
| Header | Algorithm (`alg`) and token type (`typ`) |
| Payload | Claims: `sub` (subject), `exp` (expiry), `role`, custom scopes |
| Signature | HMAC or RSA signature verifying integrity |

### Common Claims

| Claim | Meaning |
|-------|---------|
| `sub` | Subject — user ID |
| `iss` | Issuer — your auth service |
| `aud` | Audience — intended recipient API |
| `exp` | Expiration timestamp |
| `iat` | Issued at timestamp |
| `scope` | Space-separated permissions |

### FastAPI JWT Validation

```python
import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    settings: Settings = Depends(get_settings),
) -> User:
    token = credentials.credentials
    try:
        payload = jwt.decode(
            token,
            settings.jwt_secret,
            algorithms=["HS256"],
            audience="ai-api",
            issuer="auth-service",
        )
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

    return User(id=payload["sub"], role=payload.get("role", "viewer"))
```

### JWT Security Considerations

| Risk | Mitigation |
|------|------------|
| Token theft (XSS) | HttpOnly cookies for browser apps; short expiry |
| Long-lived tokens | Access token (15 min) + refresh token pattern |
| Algorithm confusion | Explicitly allowlist algorithms in `jwt.decode()` |
| Sensitive data in payload | JWT is base64, not encrypted — no PII in claims |
| No revocation | Maintain a denylist in Redis for logout/revoke |

---

## OAuth Overview

**OAuth 2.0** is an authorization framework enabling third-party applications to access resources without sharing passwords. **OpenID Connect (OIDC)** adds identity on top of OAuth.

### When AI Apps Use OAuth

| Scenario | Flow |
|----------|------|
| "Sign in with Google" for chat app | Authorization Code + PKCE |
| Slack bot accessing workspace | OAuth with bot scopes |
| Enterprise SSO (Okta, Azure AD) | OIDC |
| Service accessing user's Google Drive for RAG | OAuth with offline refresh token |

### Authorization Code Flow (Most Common)

```mermaid
sequenceDiagram
    participant User
    participant App as AI Application
    participant Auth as Auth Server (Google/Okta)
    participant API as Your API

    User->>App: Click "Sign in with Google"
    App->>Auth: Redirect to /authorize (client_id, scope, redirect_uri, PKCE challenge)
    User->>Auth: Authenticate and consent
    Auth->>App: Redirect with authorization code
    App->>Auth: POST /token (code, client_secret, PKCE verifier)
    Auth-->>App: access_token + refresh_token + id_token
    App->>API: Request with Bearer access_token
    API-->>App: Protected AI resource
```

### Key OAuth Concepts

| Term | Definition |
|------|------------|
| Resource Owner | The user |
| Client | Your AI application |
| Authorization Server | Google, Okta, Auth0 |
| Resource Server | Your API |
| Scope | Permissions requested (`openid`, `email`, `drive.readonly`) |
| PKCE | Proof Key for Code Exchange — required for public clients |

### OAuth vs API Keys

| | API Key | OAuth |
|---|---------|-------|
| Identity | Service identity | User identity |
| Rotation | Manual | Refresh tokens |
| Scope | All-or-nothing | Granular scopes |
| Use case | Server-to-server LLM calls | User-facing AI apps with SSO |

For deeper security patterns, see [Security](../security/README.md).

---

## API Versioning

APIs evolve. Versioning prevents breaking existing clients when you change request/response schemas, add fields, or deprecate endpoints.

### Versioning Strategies

| Strategy | Example | Pros | Cons |
|----------|---------|------|------|
| URL path | `/v1/chat`, `/v2/chat` | Explicit, easy to route | URL proliferation |
| Header | `Accept: application/vnd.ai.v2+json` | Clean URLs | Harder to test in browser |
| Query param | `/chat?version=2` | Simple | Easy to forget |
| Subdomain | `v2.api.example.com` | Infra-level separation | DNS/SSL overhead |

**Recommendation for AI APIs:** URL path versioning (`/v1/`) — it is the industry default, works with OpenAPI docs, and is immediately visible.

### FastAPI Versioned Routers

```python
from fastapi import FastAPI

app = FastAPI(title="AI API")

v1 = APIRouter(prefix="/v1")
v2 = APIRouter(prefix="/v2")

@v1.post("/chat")
async def chat_v1(request: ChatRequestV1): ...

@v2.post("/chat")
async def chat_v2(request: ChatRequestV2):
    # v2 adds tool_calls support in response
    ...

app.include_router(v1)
app.include_router(v2)
```

### Versioning Guidelines

- **Additive changes** (new optional fields) do not require a new version
- **Breaking changes** (removed fields, changed types) require a new version
- Support **N-1 versions** for at least 6 months with deprecation headers
- Document changes in a changelog linked from OpenAPI

```python
from fastapi import Response

@app.get("/v1/models")
async def list_models(response: Response):
    response.headers["Deprecation"] = "true"
    response.headers["Sunset"] = "Sat, 01 Jan 2027 00:00:00 GMT"
    response.headers["Link"] = '</v2/models>; rel="successor-version"'
    return await model_service.list_v1()
```

---

## Pagination

List endpoints — conversations, documents, audit logs — must paginate. Returning unbounded lists will OOM your service and timeout clients.

### Pagination Strategies

| Strategy | How It Works | Best For |
|----------|--------------|----------|
| Offset/limit | `?offset=20&limit=10` | Small datasets, admin UIs |
| Cursor-based | `?cursor=eyJ...&limit=10` | Large datasets, real-time feeds |
| Keyset | `?after_id=uuid&limit=10` | Stable ordering by indexed column |

**Recommendation:** Cursor or keyset pagination for production AI apps. Offset pagination degrades on large tables (`OFFSET 100000` is slow).

### Cursor Pagination Response

```json
{
  "data": [
    {"id": "conv_01", "title": "RAG debugging session"},
    {"id": "conv_02", "title": "Prompt engineering notes"}
  ],
  "pagination": {
    "next_cursor": "eyJpZCI6ImNvbnZfMDIifQ==",
    "has_more": true,
    "limit": 20
  }
}
```

### FastAPI Cursor Pagination

```python
import base64
import json
from uuid import UUID


def encode_cursor(last_id: UUID) -> str:
    return base64.urlsafe_b64encode(json.dumps({"id": str(last_id)}).encode()).decode()


def decode_cursor(cursor: str) -> UUID:
    data = json.loads(base64.urlsafe_b64decode(cursor.encode()))
    return UUID(data["id"])


@router.get("/conversations")
async def list_conversations(
    limit: int = Query(20, ge=1, le=100),
    cursor: str | None = None,
    user_id: str = Depends(get_current_user_id),
    repo: ConversationRepository = Depends(get_conversation_repo),
):
    after_id = decode_cursor(cursor) if cursor else None
    rows, has_more = await repo.list_after(user_id, after_id, limit)
    next_cursor = encode_cursor(rows[-1].id) if has_more and rows else None
    return {
        "data": rows,
        "pagination": {"next_cursor": next_cursor, "has_more": has_more, "limit": limit},
    }
```

---

## Streaming Responses

Streaming is central to AI UX — users see tokens appear in real time. HTTP supports streaming via **chunked transfer encoding** and **Server-Sent Events (SSE)**.

### Why Streaming Matters

| Without Streaming | With Streaming |
|-------------------|----------------|
| 30s blank screen | Tokens appear in ~200ms |
| Timeout risk on long responses | Connection stays active with chunks |
| Poor perceived latency | ChatGPT-like experience |

### Server-Sent Events (SSE)

SSE is the standard for LLM token streaming. Content type: `text/event-stream`.

```
data: {"delta": "Hello"}

data: {"delta": " world"}

data: [DONE]

```

### FastAPI Streaming Endpoint

```python
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import json


@app.post("/v1/chat/stream")
async def stream_chat(request: ChatRequest, user: User = Depends(get_current_user)):
    async def event_generator():
        try:
            async for token in llm_service.stream_completion(request.messages):
                payload = json.dumps({"delta": token})
                yield f"data: {payload}\n\n"
            yield "data: [DONE]\n\n"
        except Exception as exc:
            error = json.dumps({"error": str(exc)})
            yield f"data: {error}\n\n"

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no",  # disable nginx buffering
        },
    )
```

### Consuming OpenAI-Compatible Streams

```python
import httpx


async def stream_from_provider(messages: list[dict]):
    async with httpx.AsyncClient(timeout=120.0) as client:
        async with client.stream(
            "POST",
            "https://api.openai.com/v1/chat/completions",
            headers={"Authorization": f"Bearer {api_key}"},
            json={"model": "gpt-4o-mini", "messages": messages, "stream": True},
        ) as response:
            response.raise_for_status()
            async for line in response.aiter_lines():
                if line.startswith("data: ") and line != "data: [DONE]":
                    chunk = json.loads(line[6:])
                    delta = chunk["choices"][0]["delta"].get("content", "")
                    if delta:
                        yield delta
```

### Streaming Production Checklist

- [ ] Disable proxy buffering (`X-Accel-Buffering: no`)
- [ ] Set appropriate timeouts (60–120s minimum)
- [ ] Handle client disconnect (cancel LLM call to save cost)
- [ ] Send heartbeats for very long streams
- [ ] Log stream duration and token count for observability

```python
async def event_generator():
    try:
        async for token in llm_service.stream(...):
            if await request.is_disconnected():
                break
            yield f"data: {json.dumps({'delta': token})}\n\n"
    finally:
        await llm_service.cancel()
```

---

## Webhooks

**Webhooks** are HTTP callbacks — the server pushes events to your endpoint when something happens. Essential for async AI pipelines.

### AI Webhook Use Cases

| Event | Webhook Action |
|-------|----------------|
| Document ingestion complete | Trigger embedding and index update |
| Fine-tuning job finished | Notify app, swap model version |
| Payment succeeded | Activate subscription, increase rate limit |
| Moderation flag raised | Quarantine content, alert ops |

### Webhook Flow

```mermaid
sequenceDiagram
    participant Client
    participant API as Your AI API
    participant Queue as Job Queue
    participant Worker as Embedding Worker
    participant WH as Client Webhook Endpoint

    Client->>API: POST /v1/documents (async=true)
    API->>Queue: Enqueue ingestion job
    API-->>Client: 202 Accepted {job_id}
    Queue->>Worker: Process document
    Worker->>Worker: Chunk, embed, index
    Worker->>WH: POST /webhooks/ingestion-complete
    WH-->>Worker: 200 OK
    Client->>API: GET /v1/jobs/{job_id}
    API-->>Client: {status: "completed"}
```

### Webhook Receiver (FastAPI)

```python
import hmac
import hashlib
from fastapi import Request, HTTPException


def verify_webhook_signature(payload: bytes, signature: str, secret: str) -> bool:
    expected = hmac.new(secret.encode(), payload, hashlib.sha256).hexdigest()
    return hmac.compare_digest(f"sha256={expected}", signature)


@router.post("/webhooks/document-ingested")
async def handle_document_ingested(request: Request):
    body = await request.body()
    signature = request.headers.get("X-Webhook-Signature", "")

    if not verify_webhook_signature(body, signature, settings.webhook_secret):
        raise HTTPException(status_code=401, detail="Invalid signature")

    event = DocumentIngestedEvent.model_validate_json(body)
    await indexing_service.mark_complete(event.document_id)
    return {"received": True}
```

### Webhook Best Practices

| Practice | Reason |
|----------|--------|
| Verify signatures (HMAC) | Prevent spoofed events |
| Return 200 quickly | Process async; avoid sender retries storm |
| Implement idempotency | Senders retry on timeout — handle duplicates |
| Use exponential backoff on sender side | Standard retry policy |
| Log all webhook deliveries | Debugging and audit trail |

---

## Rate Limiting

**Rate limiting** protects your service from abuse, controls LLM costs, and ensures fair usage across tenants.

### Why Rate Limiting Is Critical for AI

- LLM calls are **expensive** — unbounded requests can burn budget in minutes
- Embedding and RAG queries are **CPU/GPU intensive**
- Public AI APIs are **abuse targets** — prompt injection, scraping, DDoS

### Rate Limiting Strategies

| Strategy | Mechanism | Use Case |
|----------|-----------|----------|
| Fixed window | N requests per minute | Simple API keys |
| Sliding window | Rolling time window | Smoother limiting |
| Token bucket | Burst allowed, steady rate | LLM token budgets |
| Concurrent limit | Max in-flight requests | GPU-bound inference |
| Cost-based | Limit by dollar spend | Multi-model APIs |

### Response Headers (Standard De Facto)

```http
HTTP/1.1 429 Too Many Requests
Retry-After: 30
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 0
X-RateLimit-Reset: 1720867200
```

### FastAPI Rate Limiting with Redis

```python
import time
from fastapi import Request, HTTPException


async def rate_limit(request: Request, redis, limit: int = 60, window: int = 60):
    key = f"rl:{request.state.user_id}:{int(time.time()) // window}"
    current = await redis.incr(key)
    if current == 1:
        await redis.expire(key, window)
    if current > limit:
        raise HTTPException(
            status_code=429,
            detail="Rate limit exceeded",
            headers={"Retry-After": str(window)},
        )
```

### Tiered Limits for AI Products

| Tier | Requests/min | Tokens/day | Concurrent streams |
|------|--------------|------------|-------------------|
| Free | 10 | 50,000 | 1 |
| Pro | 60 | 500,000 | 5 |
| Enterprise | Custom | Custom | Custom |

### Handling Upstream 429 from LLM Providers

```python
import asyncio
import random


async def call_with_retry(func, max_retries: int = 3):
    for attempt in range(max_retries):
        try:
            return await func()
        except RateLimitError as exc:
            if attempt == max_retries - 1:
                raise
            delay = (2 ** attempt) + random.uniform(0, 1)
            await asyncio.sleep(delay)
```

---

## API Security

AI APIs face unique security challenges: prompt injection, data exfiltration via tools, PII in prompts, and API key exposure.

### Security Layers

```mermaid
graph TB
    subgraph "Edge Security"
        WAF[Web Application Firewall]
        DDOS[DDoS Protection]
        TLS[TLS Termination]
    end

    subgraph "API Gateway"
        RL[Rate Limiting]
        AUTH[Authentication]
        VALID[Input Validation]
    end

    subgraph "Application"
        AUTHZ[Authorization]
        SANITIZE[Output Sanitization]
        AUDIT[Audit Logging]
    end

    subgraph "AI-Specific"
        PIIRED[PII Redaction]
        PROMPTGUARD[Prompt Injection Defenses]
        TOOLPOL[Tool Policy Enforcement]
    end

    WAF --> RL
    DDOS --> RL
    TLS --> RL
    RL --> AUTH
    AUTH --> VALID
    VALID --> AUTHZ
    AUTHZ --> SANITIZE
    SANITIZE --> AUDIT
    AUTHZ --> PIIRED
    PIIRED --> PROMPTGUARD
    PROMPTGUARD --> TOOLPOL
```

### OWASP API Security Top Risks (AI-Relevant)

| Risk | AI Context |
|------|------------|
| Broken object level authorization | User A reads User B's conversation |
| Broken authentication | Leaked API keys in client-side code |
| Unrestricted resource consumption | Unlimited LLM calls drain budget |
| SSRF via tool calls | Agent fetches internal metadata endpoints |
| Improper inventory management | Shadow AI endpoints without auth |
| Sensitive data exposure | PII in logs, prompts stored unencrypted |

### Input Validation

```python
from pydantic import BaseModel, Field, field_validator
import re


class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=32_000)

    @field_validator("message")
    @classmethod
    def no_null_bytes(cls, v: str) -> str:
        if "\x00" in v:
            raise ValueError("Invalid characters in message")
        return v.strip()
```

### CORS Configuration

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,  # never ["*"] with credentials
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Authorization", "Content-Type", "X-Request-ID"],
)
```

### Security Checklist for AI APIs

- [ ] HTTPS everywhere; HSTS enabled
- [ ] API keys in secrets manager, not source code
- [ ] JWT short expiry; refresh token rotation
- [ ] Rate limiting per user and per IP
- [ ] Input validation on all endpoints (Pydantic)
- [ ] Output encoding to prevent XSS in rendered AI responses
- [ ] PII detection and redaction before logging
- [ ] Webhook signature verification
- [ ] Dependency scanning in CI/CD
- [ ] Regular penetration testing on agent tool endpoints

See [Security](../security/README.md) and [Configuration and Secrets](../foundations/configuration-and-secrets.md) for full hardening guides.

---

## AI API Architecture

A typical production AI application exposes REST endpoints while orchestrating multiple backend services and LLM providers.

```mermaid
graph TB
    subgraph "Clients"
        WEB[Web App]
        MOBILE[Mobile App]
        SDK[Partner SDK]
    end

    subgraph "Edge"
        CDN[CDN / Static Assets]
        GW[API Gateway]
    end

    subgraph "AI API Layer (FastAPI)"
        CHAT["/v1/chat (stream)"]
        RAG["/v1/documents"]
        AGENT["/v1/agents/run"]
        WH["/webhooks/*"]
    end

    subgraph "Services"
        CONV[Conversation Service]
        DOC[Document Service]
        EMB[Embedding Service]
        AGENT_SVC[Agent Orchestrator]
    end

    subgraph "Data"
        PG[(PostgreSQL)]
        REDIS[(Redis Cache)]
        VDB[(Vector DB)]
    end

    subgraph "External"
        OPENAI[OpenAI API]
        ANTHROPIC[Anthropic API]
    end

    WEB --> CDN
    WEB --> GW
    MOBILE --> GW
    SDK --> GW
    GW --> CHAT
    GW --> RAG
    GW --> AGENT
    GW --> WH

    CHAT --> CONV
    RAG --> DOC
    AGENT --> AGENT_SVC
    CONV --> PG
    CONV --> REDIS
    DOC --> PG
    DOC --> EMB
    EMB --> VDB
    EMB --> OPENAI
    CONV --> OPENAI
    AGENT_SVC --> ANTHROPIC
    AGENT_SVC --> VDB
```

### Endpoint Design for AI Products

| Endpoint | Method | Auth | Response |
|----------|--------|------|----------|
| `/v1/chat` | POST | JWT | JSON completion |
| `/v1/chat/stream` | POST | JWT | SSE stream |
| `/v1/conversations` | GET | JWT | Paginated list |
| `/v1/documents` | POST | JWT | 202 async or 201 sync |
| `/v1/agents/{id}/run` | POST | JWT + scope | JSON or stream |
| `/health` | GET | None | `200 {"status": "ok"}` |
| `/ready` | GET | None | Checks DB + LLM connectivity |

For FastAPI project structure and dependency injection patterns, see [FastAPI Foundation](../fastapi/fastapi-foundation.md).

---

## Production Considerations

### OpenAPI Documentation

FastAPI generates OpenAPI (Swagger) docs automatically. Ship them in staging; protect or disable in production.

```python
app = FastAPI(
    title="AI API",
    version="1.0.0",
    docs_url="/docs" if settings.environment != "production" else None,
    redoc_url="/redoc" if settings.environment != "production" else None,
)
```

### Request ID Propagation

```python
import uuid
from starlette.middleware.base import BaseHTTPMiddleware


class RequestIDMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        request_id = request.headers.get("X-Request-ID", str(uuid.uuid4()))
        request.state.request_id = request_id
        response = await call_next(request)
        response.headers["X-Request-ID"] = request_id
        return response
```

### Health and Readiness Probes

```python
@router.get("/health")
async def health():
    return {"status": "ok"}


@router.get("/ready")
async def readiness(db=Depends(get_db), redis=Depends(get_redis)):
    await db.execute("SELECT 1")
    await redis.ping()
    return {"status": "ready"}
```

### Idempotency for Expensive Operations

```python
@router.post("/v1/chat")
async def chat(
    request: ChatRequest,
    idempotency_key: str | None = Header(None, alias="Idempotency-Key"),
    ...
):
    if idempotency_key:
        cached = await redis.get(f"idempotency:{idempotency_key}")
        if cached:
            return JSONResponse(content=json.loads(cached))
    result = await chat_service.complete(request)
    if idempotency_key:
        await redis.setex(f"idempotency:{idempotency_key}", 86400, result.model_dump_json())
    return result
```

### Observability

| Signal | What to Capture |
|--------|-----------------|
| Logs | `request_id`, `user_id`, `model`, `latency_ms`, `token_count` |
| Metrics | Request rate, error rate, p95 latency, tokens/minute |
| Traces | Full path: API → service → LLM provider |

---

## Common Mistakes

| Mistake | Impact | Fix |
|---------|--------|-----|
| Returning 200 with error in body | Clients cannot retry correctly | Use proper status codes |
| No auth on internal AI endpoints | Lateral movement in breaches | Authenticate all endpoints |
| API keys in frontend JavaScript | Key theft, unlimited LLM spend | Proxy through backend |
| Unbounded list endpoints | OOM, timeouts | Cursor pagination |
| Buffering streamed responses | 30s blank UI | Disable proxy buffering |
| Ignoring 429 from LLM provider | Cascading failures | Exponential backoff |
| JWT without expiry | Stolen tokens valid forever | Short-lived access tokens |
| `403` when resource not owned | User enumeration | Return `404` |
| No request timeouts | Worker exhaustion | Timeouts at every layer |
| Logging full prompts with PII | Compliance violations | Redact before logging |
| CORS `allow_origins=["*"]` with credentials | CSRF-like attacks | Explicit origin allowlist |
| Webhooks without signature verification | Spoofed events | HMAC verification |

---

## Best Practices

### API Design

1. **Use nouns for resources, HTTP methods for actions** — consistent REST semantics
2. **Version from day one** — `/v1/` even for MVPs
3. **Consistent error envelope** — `{error: {code, message, request_id}}`
4. **Document with OpenAPI** — auto-generated from FastAPI + Pydantic
5. **Paginate all list endpoints** — cursor-based for scale

### Authentication and Security

1. **Never expose LLM API keys to clients** — backend proxy pattern
2. **Validate JWTs with explicit algorithm allowlist** — prevent algorithm confusion
3. **Implement resource-level authorization** — not just authentication
4. **Rate limit by user and IP** — protect cost and availability
5. **Verify webhook signatures** — HMAC-SHA256 minimum

### AI-Specific

1. **Stream by default for chat** — fallback to non-streaming for batch
2. **Cancel LLM calls on client disconnect** — save cost
3. **Map provider errors to your status codes** — do not leak provider internals
4. **Use idempotency keys for paid operations** — prevent double billing
5. **Set token budgets per request and per user** — cost guardrails

### Operations

1. **Propagate `X-Request-ID`** — across all services and LLM calls
2. **Separate `/health` and `/ready`** — liveness vs readiness
3. **Test with contract tests** — validate OpenAPI schema in CI
4. **Monitor p95 latency and error rate per endpoint** — not just averages
5. **Deprecate with `Sunset` headers** — give clients migration time

---

## Interview Preparation

### Conceptual Questions

**Q: What is the difference between authentication and authorization?**

> **Strong answer:** Authentication verifies identity (who you are) — typically via API key, JWT, or OAuth. Authorization verifies permissions (what you can do) — via roles, scopes, or resource ownership checks. A valid JWT that cannot access another user's conversation is a 403 authorization failure, not a 401.

**Q: When would you use 401 vs 403 vs 404?**

> **Strong answer:** 401 — missing or invalid credentials. 403 — authenticated but lacks permission (e.g., viewer role trying to delete). 404 — resource does not exist OR exists but caller should not know (prevent enumeration). In AI APIs, return 404 when user B requests user A's conversation.

**Q: Why is streaming important for LLM APIs?**

> **Strong answer:** LLM generation is sequential and can take 10–60 seconds. Without streaming, the client waits for the full completion — poor UX and higher timeout risk. SSE with chunked transfer lets tokens arrive incrementally. Must disable proxy buffering and handle client disconnect to cancel the upstream call.

**Q: How do you handle rate limiting for an AI product?**

> **Strong answer:** Multi-layer: per-IP for abuse, per-user for fairness, per-tier for business model. Track both request count and token consumption. Return 429 with `Retry-After`. On upstream LLM 429, use exponential backoff with jitter. Consider a token bucket for burst tolerance.

**Q: Explain the OAuth Authorization Code flow.**

> **Strong answer:** User redirected to auth server, authenticates, grants consent. Auth server redirects back with a short-lived authorization code. Client exchanges code for access token (and refresh token) server-side. PKCE required for public clients. Access token sent as Bearer to API. Refresh token used to get new access tokens without re-login.

### System Design Prompt

**Design an API for a RAG-powered document Q&A product.**

> **Discussion points:**
> - `POST /v1/documents` for upload (async with 202 + webhook, or sync for small files)
> - `POST /v1/conversations/{id}/messages` for Q&A (streaming SSE)
> - JWT auth, resource-level authorization on conversations
> - Cursor pagination for document and conversation lists
> - Rate limiting by tier (requests + tokens)
> - API versioning from `/v1/`
> - Idempotency keys on document upload
> - Health/readiness probes, request ID propagation
> - Backend proxies LLM calls — keys never in frontend

### Coding Exercise

**Implement a FastAPI endpoint that streams LLM tokens via SSE, with JWT auth and rate limiting.**

> **Key evaluation criteria:** `StreamingResponse` with `text/event-stream`, auth dependency, rate limit check before streaming, client disconnect handling, proper error status codes, Pydantic request validation.

---

## Navigation

### Prerequisites

- [AI Engineering Overview](../foundations/ai-engineering-overview.md)
- [Software Engineering for AI](../foundations/software-engineering-for-ai.md)

### Related Topics

- [Backend Fundamentals for AI](../backend-engineering/backend-fundamentals-for-ai.md)
- [FastAPI Foundation](../fastapi/fastapi-foundation.md)
- [Configuration and Secrets](../foundations/configuration-and-secrets.md)
- [Security](../security/README.md)

### Next Topics

- [FastAPI Foundation](../fastapi/fastapi-foundation.md)
- [Backend Fundamentals for AI](../backend-engineering/backend-fundamentals-for-ai.md)
- [LLM Engineering](../llm-engineering/README.md)

### Future Reading

- [AI Application Architecture](../ai-application-architecture/README.md)
- [Observability](../observability/README.md)
- [Performance Optimization](../performance-optimization/README.md)
- [AI Safety](../ai-safety/README.md)

---

## See Also

- [APIs Index](README.md)
- [Master Index](../../meta/indexes/MASTER-INDEX.md)
- [Learning Roadmap](../../meta/roadmap.md)

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Initial version |
