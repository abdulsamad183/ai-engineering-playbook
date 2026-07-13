# Docker for AI Cheat Sheet

```bash
docker build -t ai-api .
docker compose up --build
docker run -p 8000:8000 --env-file .env ai-api
```

See [Docker for AI](../domains/ai-deployment/docker-for-ai.md).
