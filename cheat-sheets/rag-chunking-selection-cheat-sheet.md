# Chunking Selection Cheat Sheet

> See [Chunking](../domains/rag/chunking.md).

| Use case | Strategy | Size hint |
|----------|----------|-----------|
| General docs | Recursive | 512 tokens, 15% overlap |
| Enterprise KB | Parent-child | 128 child / 2K parent |
| Code | AST / file | Per function/class |
| Legal | Section-based | By clause heading |
| Chat logs | Semantic | Variable |

**Eval:** Tune with recall@K on golden set — not guesswork.
