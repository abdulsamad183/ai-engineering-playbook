---
title: "6. Context Window"
description: "How many tokens the model can see at once — hard system constraint."
domain: llm-engineering
tags: [fundamentals, context]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 6. Context Window

> How many tokens the model can see at once — hard system constraint.

## Definition

The **context window** is the max tokens of prompt+generation the model can attend over. Exceeding it truncates or errors.

## Engineering impacts

- RAG chunk budgets  
- Chat history compaction  
- Long-doc strategies  

## See also

- [context-windows.md](../context-windows.md) (reference note)

---

## Continue

- **Section hub:** [LLM Fundamentals](README.md)
- **LLM overview:** [Large Language Models](../README.md)
