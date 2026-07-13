# Topic Indexes

> Cross-cutting topic collections that span multiple domains.
> Create a new topic index when a theme appears in 3+ domains.

---

## Available Topic Indexes

| Topic | Description | Status |
|-------|-------------|--------|
| [Streaming](streaming.md) | Real-time LLM responses, SSE, WebSockets | Planned |
| [Cost Optimization](cost-optimization.md) | Reducing AI infrastructure and API costs | Planned |
| [Security](security.md) | Security practices across all AI domains | Planned |
| [Testing](testing.md) | Testing strategies for AI applications | Planned |
| [Error Handling](error-handling.md) | Resilience patterns for AI systems | Planned |
| [Caching](caching.md) | Caching strategies for AI workloads | Planned |

---

## Creating a New Topic Index

1. Confirm the topic appears in 3+ domain documents.
2. Create `{topic-name}.md` in this folder.
3. List all relevant documents grouped by domain.
4. Add an entry to this README.
5. Cross-link from relevant domain indexes.

### Topic Index Template

```markdown
# {Topic Name}

> Documents across the playbook related to {topic}.

## {Domain Name}

- [Document Title](../../domains/domain/doc.md) — description

## See Also

- [Tag: {tag}](../tags/tag-registry.md)
- [Master Index](../MASTER-INDEX.md)
```

---

## See Also

- [Master Index](../MASTER-INDEX.md)
- [Indexing Strategy](../../indexing-strategy.md)
