---
title: "{API Name}"
description: "Reference and integration guide for the {API Name} API."
domain: apis
tags: [api, {tag1}, {tag2}]
status: draft
created: YYYY-MM-DD
updated: YYYY-MM-DD
version: "1.0"
related: []
keywords: []
---

# {API Name}

> What this API provides, who it's for, and how it fits into AI application architectures.

## Table of Contents

- [Overview](#overview)
- [Authentication](#authentication)
- [Base URL and Versioning](#base-url-and-versioning)
- [Endpoints](#endpoints)
- [Request and Response Formats](#request-and-response-formats)
- [Error Handling](#error-handling)
- [Rate Limits](#rate-limits)
- [SDK and Client Libraries](#sdk-and-client-libraries)
- [Integration Examples](#integration-examples)
- [Production Best Practices](#production-best-practices)

## Overview

| Attribute | Value |
|-----------|-------|
| Protocol | REST / gRPC / WebSocket |
| Format | JSON / Protobuf |
| Auth | API Key / OAuth / Bearer Token |
| Documentation | [Official Docs](https://example.com) |

## Authentication

```bash
curl -H "Authorization: Bearer $API_KEY" https://api.example.com/v1/endpoint
```

### API Key Management

> **Production Standard:** Never hardcode API keys. Use environment variables or a secrets manager.

## Base URL and Versioning

```
Production: https://api.example.com/v1
Staging:    https://staging-api.example.com/v1
```

## Endpoints

### `POST /endpoint-name`

Description of what this endpoint does.

**Request:**

```json
{
  "field": "value"
}
```

**Response:**

```json
{
  "result": "value"
}
```

**Status Codes:**

| Code | Meaning |
|------|---------|
| 200 | Success |
| 400 | Bad request |
| 401 | Unauthorized |
| 429 | Rate limited |
| 500 | Server error |

### `GET /another-endpoint`

Description.

## Request and Response Formats

### Common Headers

| Header | Required | Description |
|--------|----------|-------------|
| `Authorization` | Yes | Bearer token |
| `Content-Type` | Yes | `application/json` |

## Error Handling

```json
{
  "error": {
    "code": "rate_limit_exceeded",
    "message": "Rate limit exceeded. Retry after 60 seconds.",
    "retry_after": 60
  }
}
```

### Retry Strategy

```python
# Recommended retry pattern with exponential backoff
```

## Rate Limits

| Tier | Requests/min | Tokens/min | Notes |
|------|-------------|------------|-------|
| Free | | | |
| Pro | | | |

## SDK and Client Libraries

| Language | Package | Install |
|----------|---------|---------|
| Python | `package-name` | `pip install package-name` |
| TypeScript | `@scope/package` | `npm install @scope/package` |

## Integration Examples

### Python (FastAPI)

```python
# Integration example
```

### Direct HTTP

```bash
curl -X POST https://api.example.com/v1/endpoint \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"field": "value"}'
```

## Production Best Practices

- [ ] Implement request timeouts (≤ 30s)
- [ ] Use exponential backoff for retries
- [ ] Log request IDs for debugging
- [ ] Monitor rate limit headers
- [ ] Set up cost alerts
- [ ] Implement circuit breaker for cascading failures

---

## See Also

- [Related API](../path/to/doc.md)

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | YYYY-MM-DD | Initial version |
