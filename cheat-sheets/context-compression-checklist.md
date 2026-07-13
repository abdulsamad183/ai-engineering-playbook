# Context Compression Checklist

> Before deploying compression. See [Context Compression](../domains/context-engineering/context-compression.md).

## Strategy

- [ ] Drop lowest-ranked chunks first
- [ ] Extractive trim before abstractive summarize
- [ ] Entity validation (numbers, dates, names)
- [ ] Never compress P0 policy blocks

## Quality Gates

- [ ] Faithfulness eval on sample summaries
- [ ] Fail closed: drop chunk vs corrupt
- [ ] Re-count tokens after compression

## Triggers

- [ ] Compress only when over budget (not every turn)
- [ ] Async pre-compress for known long sessions

## Anti-Patterns

- ❌ Compress before ranking
- ❌ Abstractive-only without validation
- ❌ Summarize user message

## See Also

- [Summarization Template](../prompts/templates/summarization.md)
