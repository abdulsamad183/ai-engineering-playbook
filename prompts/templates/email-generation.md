---
title: "Email Generation Prompt Template"
description: "Reusable prompt for professional emails with tone control, structure, and compliance constraints."
domain: prompt-engineering
tags: [prompt, email, communication, tone]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
id: email-generation-v1
task: email-generation
models:
  recommended: [gpt-4o-mini, gpt-4o, claude-sonnet-4]
  min_capability: basic
token_budget:
  system: 250
  user_per_input: 100
variables:
  required: [purpose, recipient_context, key_points]
  optional: [tone, sender_name, max_words, call_to_action, forbidden_phrases]
output:
  format: markdown
  schema: null
related:
  - summarization.md
  - ../../domains/prompt-engineering/prompt-templates-guide.md
keywords: [email, outreach, customer communication, professional writing]
---

# Email Generation Prompt Template

> Draft professional emails with controlled tone, structure, and explicit content boundaries.

## Pattern Overview

| Attribute | Value |
|-----------|-------|
| Use Case | Customer replies, sales outreach, internal updates, support responses, follow-ups |
| Best Models | gpt-4o-mini, gpt-4o, claude-sonnet-4 |
| Complexity | Simple |
| Token Budget | ~300–500 tokens |
| Expected Output | Subject line + email body in Markdown |

## When to Use

- Drafting first-pass customer support replies from ticket context
- Sales or partnership outreach with consistent brand voice
- Internal status updates from bullet-point notes
- Follow-up emails after meetings (from notes, not invented outcomes)

## When Not to Use

- Legally binding communications without legal review
- Emails containing PII from unredacted logs (sanitize input first)
- High-stakes apology or crisis communications without executive approval

## System Prompt

```
You are a professional communication assistant for {{sender_name}}.

Write an email for this purpose: {{purpose}}

Tone: {{tone}}

Rules:
- Maximum {{max_words}} words in the body.
- Include a clear subject line on the first line as: Subject: ...
- Cover all key points provided. Do not add commitments, dates, or offers not in the input.
- End with this call to action: {{call_to_action}}
- Never use these phrases: {{forbidden_phrases}}
- Do not include placeholder brackets like [NAME] — use provided names or omit.
- No emojis unless tone explicitly requests casual style.

Output: Markdown with Subject line, then body paragraphs.
```

## User Prompt

```
<recipient>
{{recipient_context}}
</recipient>

<key_points>
{{key_points}}
</key_points>

<reference_material>
{{reference_material}}
</reference_material>
```

## Variables

| Name | Required | Default | Description |
|------|----------|---------|-------------|
| `purpose` | Yes | — | Why this email is being sent |
| `recipient_context` | Yes | — | Who they are, relationship, prior context |
| `key_points` | Yes | — | Bullets the email must address |
| `tone` | No | professional and warm | formal, concise, empathetic, assertive |
| `sender_name` | No | the team | Signature name or team |
| `max_words` | No | 150 | Body word limit |
| `call_to_action` | No | reply if questions | Desired reader action |
| `forbidden_phrases` | No | guaranteed, always, never | Compliance or brand restrictions |
| `reference_material` | No | (none) | Ticket text, meeting notes, policy excerpts |

## Complete Example

### Input Variables

```yaml
purpose: Respond to billing inquiry about duplicate charge
recipient_context: Enterprise customer, account manager is Sarah Chen
tone: empathetic and professional
key_points:
  - Acknowledge duplicate charge on invoice #8842
  - Refund processing within 3 business days
  - Offer to schedule call if further questions
max_words: 120
```

### Expected Output

```
Subject: Re: Duplicate charge on invoice #8842

Hi Sarah,

Thank you for flagging the duplicate charge on invoice #8842. We have initiated a refund, which should appear within 3 business days.

Please reply if you have any other questions — happy to schedule a call.

Best regards,
The team
```

## Evaluation Criteria

| Metric | Target | How to Measure |
|--------|--------|----------------|
| Key point coverage | 100% | All bullets addressed |
| Tone match | Subjective | Brand/compliance review |
| No hallucination | 100% | No invented refunds, dates, or names |
| Length | ≤ max_words | Automated word count |

## Tips and Pitfalls

- Redact PII in `reference_material` before sending to external APIs.
- Put policy constraints in `forbidden_phrases` and system rules.
- Human review required for billing, legal, and crisis emails.
