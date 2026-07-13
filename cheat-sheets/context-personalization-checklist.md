# Context Personalization Checklist

> Safe personalization rollout. See [Context Personalization](../domains/context-engineering/context-personalization.md).

## Data

- [ ] Explicit preferences with opt-out
- [ ] Profile version in context trace
- [ ] PII minimized in prompts
- [ ] Regional compliance reviewed

## Technical

- [ ] Cache invalidation on profile update
- [ ] Fallback to generic context on miss
- [ ] Separate profile vs semantic memory
- [ ] Tenant isolation on all stores

## Product

- [ ] User can view/delete stored memories
- [ ] Fairness check across segments
- [ ] No sensitive attribute inference without consent

## See Also

- [Context Security](../domains/context-engineering/context-security.md)
