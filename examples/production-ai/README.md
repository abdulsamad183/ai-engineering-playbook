# Production AI Examples

> patterns. See [Production AI Handbook](../../domains/ai-deployment/README.md).

| Example | Pattern |
|---------|---------|
| [Dockerfile](Dockerfile) + [docker-compose.yml](docker-compose.yml) | Containerized FastAPI |
| [src/main.py](src/main.py) | Minimal AI API |
| [.github-workflows-ci.yml](.github-workflows-ci.yml) | CI/CD with eval gate |
| [example-health-endpoints.py](example-health-endpoints.py) | Health + readiness |
| [example-structured-logging.py](example-structured-logging.py) | JSON logs + correlation ID |
| [example-opentelemetry.py](example-opentelemetry.py) | Trace spans |
| [example-langfuse-integration.py](example-langfuse-integration.py) | LLM trace export |
| [example-phoenix-integration.py](example-phoenix-integration.py) | RAG trace export |
| [example-redis-cache.py](example-redis-cache.py) | Response caching |
| [example-retry-middleware.py](example-retry-middleware.py) | Exponential backoff |
| [example-rate-limiting.py](example-rate-limiting.py) | Token bucket |
| [example-cost-tracking.py](example-cost-tracking.py) | Per-request cost |
| [example-monitoring-dashboard.py](example-monitoring-dashboard.py) | Metrics aggregation |

```bash
cd examples/production-ai
python example-regression-testing.py  # from ai-evaluation if linked
docker compose up --build
```
