# LLM Provider APIs Cheat Sheet

> Quick reference for major LLM providers. See [providers/](../domains/llm-engineering/providers/).

## Client Setup

```python
# OpenAI
from openai import AsyncOpenAI
client = AsyncOpenAI(api_key=os.environ["OPENAI_API_KEY"])

# Anthropic
from anthropic import AsyncAnthropic
client = AsyncAnthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

# Groq (OpenAI-compatible)
client = AsyncOpenAI(api_key=os.environ["GROQ_API_KEY"], base_url="https://api.groq.com/openai/v1")

# Ollama (local)
client = AsyncOpenAI(api_key="ollama", base_url="http://localhost:11434/v1")
```

## Chat Request Patterns

| Provider | Endpoint / Method |
|----------|-----------------|
| OpenAI | `client.chat.completions.create(...)` |
| Anthropic | `client.messages.create(...)` |
| Gemini | `client.aio.models.generate_content(...)` |
| Groq / OpenRouter / Ollama | OpenAI-compatible `chat.completions` |

## Streaming

```python
# OpenAI / compatible
stream = await client.chat.completions.create(..., stream=True)
async for chunk in stream:
    print(chunk.choices[0].delta.content, end="")
```

## Structured Output

| Provider | Mechanism |
|----------|-----------|
| OpenAI | `response_format={"type": "json_object"}` or strict schema |
| Anthropic | Tool use with single forced tool |
| Gemini | `response_mime_type="application/json"` |

## Embeddings

```python
# OpenAI
emb = await client.embeddings.create(input=["text"], model="text-embedding-3-small")
```

## Always In Production

- [ ] Timeouts on every call
- [ ] Retry with exponential backoff (429, 5xx)
- [ ] Log token usage, not prompt content
- [ ] Fallback model configured
- [ ] `max_tokens` set

## See Also

- [Model Comparison Guide](../domains/llm-engineering/model-comparison-guide.md)
- [Examples](../examples/llm-applications/)
