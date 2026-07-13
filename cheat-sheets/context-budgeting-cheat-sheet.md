# Context Budgeting Cheat Sheet

> Token and cost allocation. See [Context Budgeting](../domains/context-engineering/context-budgeting.md).

## Formula

```
input_cap = context_limit - reserved_output
Σ(layer_tokens) ≤ input_cap
```

## Priority Fill Order

1. System + mandatory policies (P0)
2. Current user message (never truncate)
3. Retrieval (P1 for KB tasks)
4. History (P2)
5. Memory (P3)

## Cost Control

- Reduce `top_k` before dropping policies
- Prompt-cache stable prefix
- Compress history before retrieval
- Right-size model per route

## Alerts

| Metric | Threshold |
|--------|-----------|
| Truncation rate | >15% |
| Avg input tokens | 2× baseline |
| Empty retrieval | >10% |

## See Also

- [Context Windows](../domains/context-engineering/context-windows.md)
