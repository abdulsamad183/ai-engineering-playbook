---
title: "Translation Prompt Template"
description: "Reusable prompt for accurate, context-aware translation preserving tone, terminology, and formatting."
domain: prompt-engineering
tags: [prompt, translation, localization, multilingual]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
id: translation-v1
task: translation
models:
  recommended: [gpt-4o, claude-sonnet-4, gpt-4o-mini]
  min_capability: intermediate
token_budget:
  system: 250
  user_per_input: 60
variables:
  required: [source_text, target_language]
  optional: [source_language, domain, tone, glossary, preserve_formatting]
output:
  format: text
  schema: null
related:
  - ../../domains/prompt-engineering/prompt-templates-guide.md
keywords: [translation, localization, multilingual, glossary]
---

# Translation Prompt Template

> Translate text between languages while preserving meaning, tone, proper nouns, and structural formatting.

## Pattern Overview

| Attribute | Value |
|-----------|-------|
| Use Case | Product localization, document translation, multilingual support, subtitle translation |
| Best Models | gpt-4o, claude-sonnet-4, gpt-4o-mini |
| Complexity | Simple to Moderate |
| Token Budget | ~300–600 tokens (system + user) |
| Expected Output | Translated text only (no commentary) |

## When to Use

- Translating user-facing UI strings, emails, or documentation
- Localizing marketing content with tone constraints
- Batch translation pipelines with glossary enforcement
- Back-translation for quality assurance checks

## When Not to Use

- Certified legal or medical translation requiring human translators
- Real-time interpretation with latency under 100ms
- Languages or dialects where the model has known weaknesses (verify first)

## System Prompt

```
You are a professional translator specializing in {{domain}} content.

Translate from {{source_language}} to {{target_language}}.

Rules:
- Preserve the original meaning, intent, and {{tone}} tone.
- Do not add, omit, or editorialize content.
- Keep proper nouns, brand names, and product names unchanged unless a glossary entry specifies otherwise.
- Preserve formatting: line breaks, bullet structure, markdown, and placeholders like {{variable}} or {0}.
- Apply this glossary strictly:
{{glossary}}
- Output ONLY the translated text. No explanations, notes, or alternatives.

{{preserve_formatting_instructions}}
```

## User Prompt

```
<text>
{{source_text}}
</text>
```

## Variables

| Name | Required | Default | Description |
|------|----------|---------|-------------|
| `source_text` | Yes | — | Text to translate |
| `target_language` | Yes | — | Target language (e.g., Spanish, Japanese) |
| `source_language` | No | auto-detect | Source language; use "auto-detect" if unknown |
| `domain` | No | general | Domain: legal, medical, technical, marketing |
| `tone` | No | neutral professional | formal, casual, technical, marketing |
| `glossary` | No | (none) | Term mappings: `source_term → target_term` per line |
| `preserve_formatting` | No | true | When true, keep markdown/HTML structure intact |
| `preserve_formatting_instructions` | No | Preserve all markdown and placeholder syntax. | Extra formatting rules |

## Complete Example

### Input Variables

```yaml
source_text: "Your trial expires in **3 days**. Upgrade to Pro to keep your data."
source_language: English
target_language: German
domain: SaaS product UI
tone: friendly and direct
glossary: |
  Pro → Pro
  trial → Testversion
```

### Expected Output

```
Deine Testversion läuft in **3 Tagen** ab. Upgrade auf Pro, um deine Daten zu behalten.
```

## Evaluation Criteria

| Metric | Target | How to Measure |
|--------|--------|----------------|
| Meaning preservation | > 95% | Bilingual human review or COMET score |
| Glossary compliance | 100% | Automated term check against glossary |
| Formatting preservation | 100% | Markdown/placeholder diff vs. source structure |
| Fluency | > 4/5 | Native speaker rating |
| Back-translation BLEU | Baseline-dependent | Round-trip semantic similarity |

## Tips and Pitfalls

- Provide a glossary for product terms; preserve `{{variable}}` placeholders.
- Specify `{{tone}}` explicitly; chunk long documents to avoid truncation.
- Verify rare language pairs before production rollout.
