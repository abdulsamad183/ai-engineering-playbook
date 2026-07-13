# Agent Debugging Checklist

1. [ ] Trace: which tool at failure step?
2. [ ] Repeated identical actions? → loop guard
3. [ ] Wrong tool args? → schema validation
4. [ ] Context too large? → truncate observations
5. [ ] Stale checkpoint? → version mismatch
6. [ ] Retry storm? → circuit breaker metrics

See [Agent Mistakes](../domains/ai-agents/agent-engineering-mistakes.md).
