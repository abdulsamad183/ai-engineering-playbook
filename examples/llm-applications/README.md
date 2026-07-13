# LLM Application Examples

> Production-ready Python examples for LLM API integration.

| Example | Provider | Topic |
|---------|----------|-------|
| [example-openai-chat.py](example-openai-chat.py) | OpenAI | Chat completions |
| [example-openai-streaming.py](example-openai-streaming.py) | OpenAI | Token streaming |
| [example-structured-output.py](example-structured-output.py) | OpenAI | JSON / Pydantic |
| [example-function-calling.py](example-function-calling.py) | OpenAI | Tool use |
| [example-embeddings.py](example-embeddings.py) | OpenAI | Embeddings + similarity |
| [example-token-counting.py](example-token-counting.py) | tiktoken | Token count + cost |
| [example-anthropic-chat.py](example-anthropic-chat.py) | Anthropic | Claude messages API |
| [example-gemini-chat.py](example-gemini-chat.py) | Google | Gemini generate |
| [example-groq-chat.py](example-groq-chat.py) | Groq | Fast inference |
| [example-openrouter-chat.py](example-openrouter-chat.py) | OpenRouter | Multi-provider routing |
| [example-ollama-chat.py](example-ollama-chat.py) | Ollama | Local inference |
| [example-vision-request.py](example-vision-request.py) | OpenAI | Multimodal vision |

## Setup

```bash
pip install -r requirements.txt
export OPENAI_API_KEY=sk-...
export ANTHROPIC_API_KEY=sk-ant-...
export GOOGLE_API_KEY=...
```

## See Also

- [Phase 4 LLM Engineering](../../domains/llm-engineering/README.md)
- [Provider Guides](../../domains/llm-engineering/providers/)
