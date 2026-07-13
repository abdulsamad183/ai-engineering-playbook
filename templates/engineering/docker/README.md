# Docker Starter

> Multi-stage builds and Compose stacks for dev and production.

---

## Purpose

Reusable Docker assets: multi-stage Dockerfile, development vs production targets, Compose with API + Redis + Qdrant.

---

## Files

| File | Description |
|------|-------------|
| `Dockerfile.multistage` | `development` and `production` targets |
| `docker-compose.yml` | API, Redis, Qdrant with volumes |

---

## Usage

```bash
docker compose -f templates/engineering/docker/docker-compose.yml up --build
```

---

## Production Considerations

- Non-root user in production stage
- Health checks on API service
- Named volumes for vector data

---

## Related

- [FastAPI Dockerfile](../fastapi-starter/Dockerfile)
- [Production Docker Guide](../../domains/ai-deployment/docker-for-ai-applications.md)
