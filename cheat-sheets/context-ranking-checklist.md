# Context Ranking Checklist

> Pre-production ranking validation. See [Context Ranking](../domains/context-engineering/context-ranking.md).

## Configuration

- [ ] Min similarity threshold set
- [ ] Hybrid fusion (RRF or weighted) configured
- [ ] Recency decay for time-sensitive content
- [ ] Business boosts for mandatory docs
- [ ] Reranker stage defined (optional)

## Eval

- [ ] Labeled query-doc pairs (≥50)
- [ ] recall@5 measured
- [ ] Compare vector-only vs hybrid
- [ ] Log full ranked list in traces

## Production

- [ ] Feature-flag weight profiles
- [ ] Cross-tenant filter before rank
- [ ] Stable sort for reproducibility
- [ ] Alert on score distribution drift

## See Also

- [Context Selection](../domains/context-engineering/context-selection.md)
