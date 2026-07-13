# LLM Sampling Parameters Cheat Sheet

> Quick reference for decoding parameters. See [Sampling and Decoding](../domains/llm-engineering/sampling-and-decoding.md).

## Parameters

| Parameter | Range | Effect | Use When |
|-----------|-------|--------|----------|
| `temperature` | 0.0–2.0 | Randomness | 0 for deterministic; 0.7+ for creative |
| `top_p` | 0.0–1.0 | Nucleus sampling | Alternative to temperature |
| `top_k` | 1–100 | Limit token pool | Reduce nonsense tokens |
| `max_tokens` | 1–model limit | Cap output length | Always set — prevents runaway cost |
| `stop` | strings | End generation early | Custom delimiters, `###` |
| `frequency_penalty` | -2 to 2 | Penalize repetition | Reduce word loops |
| `presence_penalty` | -2 to 2 | Encourage new topics | Diverse outputs |

## Presets by Task

| Task | temperature | top_p | max_tokens |
|------|-------------|-------|------------|
| Classification / extraction | 0.0 | 1.0 | 256 |
| RAG answer generation | 0.1–0.3 | 0.9 | 1024 |
| Creative writing | 0.7–1.0 | 0.95 | 2048 |
| Code generation | 0.0–0.2 | 0.95 | 4096 |
| Brainstorming | 0.8–1.2 | 0.95 | 1024 |

## Rules

- Do **not** tune both `temperature` and `top_p` aggressively — pick one primary knob.
- Always set `max_tokens` in production.
- Use `seed` (where supported) for reproducible evals, not production variety.

## See Also

- [LLM Inference](../domains/llm-engineering/llm-inference.md)
- [LLM Engineering Mistakes](../domains/llm-engineering/llm-engineering-mistakes.md)
