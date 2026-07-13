# Context Debugging Checklist

> When answers fail in production. See [Context Engineering Mistakes](../domains/context-engineering/context-engineering-mistakes.md).

## 1. Trace Inspection

- [ ] Full `ContextPackage` logged for failing request?
- [ ] Token count per layer?
- [ ] Included vs excluded IDs with reasons?

## 2. Wrong Facts

- [ ] Retrieval recall — gold doc in top-K?
- [ ] Stale index or cache?
- [ ] Memory pollution?
- [ ] Cross-tenant leak ruled out?

## 3. Forgot Context

- [ ] History pruned too aggressively?
- [ ] Summary lost key entities?
- [ ] Session expired?

## 4. Cost / Latency

- [ ] Assembly timing breakdown?
- [ ] Cache hit rates?
- [ ] Compression on every turn?

## 5. Replay

- [ ] Re-run assembly from trace without LLM
- [ ] A/B policy version comparison

## Quick Fixes

| Symptom | First action |
|---------|--------------|
| Hallucination | Check retrieval + grounding |
| Forgot prior turn | Check history budget + summary |
| Slow | Parallel fetch + cache |
| Wrong policy | Check dynamic resolver branch |

## See Also

- [Context Quality](../domains/context-engineering/context-quality.md)
