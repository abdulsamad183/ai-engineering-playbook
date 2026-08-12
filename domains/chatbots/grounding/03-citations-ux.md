---
title: "Citations UX"
description: "Design citation experiences users trust — inline markers, source panels, snippet fidelity, and anti-theater patterns."
domain: chatbots
tags: [chatbots, citations, ux, grounding]
status: published
created: 2026-08-12
updated: 2026-08-12
version: "1.0"
related:
  - 01-grounded-support-bots.md
  - 02-rag-in-chat.md
  - ../ops/01-chatbot-evaluation.md
  - ../../rag/README.md
keywords: [citations, provenance, source links, grounded UX]
author: hp
---

# Citations UX

> Citations are a product surface — decorative footnotes that do not support the claim are worse than none.

## Table of Contents

- [Definition](#definition)
- [Why It Matters](#why-it-matters)
- [Common Uses](#common-uses)
- [How It Works](#how-it-works)
- [UX Patterns](#ux-patterns)
- [Python Examples](#python-examples)
- [Production Considerations](#production-considerations)
- [Cost Considerations](#cost-considerations)
- [Security Considerations](#security-considerations)
- [Best Practices](#best-practices)
- [Common Mistakes](#common-mistakes)
- [Navigation](#navigation)

---

## Definition

**Citations UX** is how the product presents provenance for chatbot claims: inline markers, source cards, quote snippets, and confidence affordances. Engineering must keep claim→source alignment honest.

---

## Why It Matters

Users (and auditors) click sources. If the linked doc does not contain the claim, trust evaporates and support load rises. Good citations also speed human agents during handoff.

---

## Common Uses

| Channel | Citation form |
|---------|---------------|
| Web chat | Inline [1] + side panel |
| Slack | Link to help article + quote |
| WhatsApp | Short URL + title (length limits) |
| Voice | “According to the returns policy…” + SMS link |

---

## How It Works

```mermaid
flowchart LR
  Gen[Model output with [n]] --> Align[Align spans to chunks]
  Align --> UI[Render markers + cards]
  Align --> Eval[Citation precision metrics]
```

Pipeline options:

1. Model emits `[n]` grounded in numbered evidence
2. Post-hoc linker attributes sentences to chunks
3. Extractive answers quote snippets directly

---

## UX Patterns

| Pattern | Pros | Cons |
|---------|------|------|
| Inline [n] | Precise | Clutter on mobile |
| End footnotes | Cleaner prose | Weaker claim binding |
| Source cards | Rich previews | Space heavy |
| Quote chips | High trust | Brittle if chunking poor |

Anti-theater rules:

- Hide sources that were retrieved but unused
- Do not show a URL the model never relied on
- Prefer deep links to the relevant section

---

## Python Examples

### Parse citation ids

```python
import re

CIT_RE = re.compile(r"\[(\d+)\]")

def cited_ids(text: str) -> list[int]:
    return sorted({int(x) for x in CIT_RE.findall(text)})
```

### Validate ids against evidence

```python
def invalid_citations(answer: str, n_chunks: int) -> list[int]:
    return [i for i in cited_ids(answer) if i < 1 or i > n_chunks]
```

### Build UI payload

```python
def citation_cards(ids: list[int], chunks: list[dict]) -> list[dict]:
    cards = []
    for i in ids:
        c = chunks[i - 1]
        cards.append({"id": i, "title": c["title"], "url": c["url"], "snippet": c["text"][:240]})
    return cards
```

---

## Production Considerations

- Measure citation precision/recall on golden sets
- Fallback UI when model forgets markers: attach top used chunk
- Localize source titles
- Track click-through as a weak quality signal
- Keep chunk IDs stable across a turn

---

## Cost Considerations

Long snippets in the UI do not cost LLM tokens — but packing long snippets into the prompt does. Separate **prompt evidence** from **display snippet**.

---

## Security Considerations

- Do not cite internal-only docs to unauthorized users
- Strip signed URLs that over-expose data
- Avoid leaking other customers’ ticket IDs in “sources”
- Be careful with auto-screenshots of confidential pages

---

## Best Practices

1. Number evidence and require `[n]` in the prompt
2. Validate citation IDs before render
3. Show snippets that actually contain the claim
4. Soften language when evidence is thin
5. Educate users: citations ≠ legal advice

---

## Common Mistakes

- Footnotes for unused retrieval hits
- Broken or login-walled links
- Citing the homepage instead of the policy section
- Tiny unreadable marker UIs on mobile
- No offline eval for citation faithfulness

---

## Navigation

| | |
|--|--|
| **Previous** | [RAG in Chat](02-rag-in-chat.md) |
| **Next** | [Tone and Persona](../personality-and-safety/01-tone-and-persona.md) |
| **Section** | [Grounding](README.md) |
| **Handbook** | [Chatbots](../README.md) |
