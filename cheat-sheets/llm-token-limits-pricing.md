# LLM Token Limits & Pricing Cheat Sheet

> Context windows and cost awareness. Verify current limits with providers — they change frequently.

## Context Windows (approximate, 2026)

| Model Family | Context Window |
|--------------|----------------|
| GPT-4o / 4o-mini | 128K |
| Claude 3.5/4 Sonnet | 200K |
| Gemini 2.0 Flash | 1M |
| Llama 3.x | 128K |
| DeepSeek V3 | 128K |

## Token Budget Formula

```
total_tokens = system_prompt + conversation_history + retrieved_context + user_message + max_output
```

Must be **≤ model context window**.

## Cost Estimation

```python
cost = (input_tokens / 1_000_000) * input_price + (output_tokens / 1_000_000) * output_price
```

Use `tiktoken` for OpenAI models; provider APIs return usage in responses.

## Cost Reduction Quick Wins

| Technique | Savings |
|-----------|---------|
| Smaller model for simple tasks | 10–50× |
| Shorter system prompts | 5–20% |
| Prompt / prefix caching | 50–90% on repeated prefixes |
| Response caching (Redis) | 100% on cache hits |
| Truncate old conversation turns | Variable |

## See Also

- [Tokens and Tokenization](../domains/llm-engineering/tokens-and-tokenization.md)
- [LLM Cost Optimization](../domains/llm-engineering/llm-cost-optimization.md)
- [example-token-counting.py](../examples/llm-applications/example-token-counting.py)
