# Context Engineering Workflow Cheat Sheet

> End-to-end context pipeline. See [Introduction](../domains/context-engineering/introduction-to-context-engineering.md).

## Pipeline Stages

```
Collect → Enrich → Filter → Rank → Compress → Assemble → Infer → Update
```

## Per-Request Checklist

1. Load session state + user profile
2. Parallel fetch: memory, retrieval, policies
3. Permission filter (tenant/user)
4. Deduplicate cross-sources
5. Rank candidates
6. Enforce token budget per layer
7. Compress if over budget
8. Assemble messages with delimiters
9. Pre-count tokens; log trace
10. Post-turn: update state/memory async

## Layer Budget (starting point, 8K input)

| Layer | Tokens |
|-------|--------|
| System + tools | ~600–800 |
| Retrieval | ~2000–3000 |
| History | ~1500–2500 |
| Memory | ~300–600 |
| User | ~300–500 |
| Output reserve | ~1500–2500 |

## See Also

- [Context Budgeting Cheat Sheet](context-budgeting-cheat-sheet.md)
- [Context Debugging Checklist](context-debugging-checklist.md)
