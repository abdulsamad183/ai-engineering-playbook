---
title: "SQL Generation Prompt Template"
description: "Reusable prompt for generating safe, optimized SQL from natural language and schema context."
domain: prompt-engineering
tags: [prompt, sql, database, query-generation]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
id: sql-generation-v1
task: sql-generation
models:
  recommended: [gpt-4o, claude-sonnet-4, gpt-4o-mini]
  min_capability: intermediate
token_budget:
  system: 400
  user_per_request: 250
variables:
  required: [question, schema]
  optional: [dialect, constraints, sample_data, output_format]
output:
  format: sql
  schema: null
related:
  - code-generation.md
  - ../../domains/prompt-engineering/prompt-templates-guide.md
keywords: [SQL, text-to-SQL, analytics, query builder]
---

# SQL Generation Prompt Template

> Generate correct, readable SQL from natural language questions against a provided schema. Prefer safe patterns and explain assumptions.

## Pattern Overview

| Attribute | Value |
|-----------|-------|
| Use Case | Analytics copilots, internal query tools, BI assistants, data exploration |
| Best Models | gpt-4o, claude-sonnet-4, gpt-4o-mini |
| Complexity | Moderate |
| Token Budget | ~500–1200 tokens (system + user) |
| Expected Output | SQL query with optional explanation |

## When to Use

- Natural-language interfaces over warehouse or OLTP schemas
- Generating ad-hoc analytics queries for analysts
- Bootstrapping complex JOINs and aggregations from schema docs
- Teaching SQL by showing idiomatic query patterns

## When Not to Use

- Executing generated SQL without human review or read-only sandboxes
- Schemas not provided or outdated (model will hallucinate columns)
- Write operations (INSERT/UPDATE/DELETE) in production without safeguards

## System Prompt

```
You are an expert {{dialect}} SQL engineer.

Generate SQL to answer the user's question using ONLY the tables and columns in the provided schema.

Rules:
- Use {{dialect}} syntax exclusively.
- SELECT queries only unless explicitly asked for DML and {{allow_writes}} is true.
- Always qualify column names with table aliases in multi-table queries.
- Use explicit JOINs; avoid implicit comma joins.
- Add appropriate WHERE filters to limit result size (default LIMIT {{default_limit}}).
- Never use SELECT * in production queries; list columns explicitly.
- Do not invent tables, columns, or relationships not in the schema.
{{constraints}}

Output format:
{{output_format}}
```

## User Prompt

```
<schema>
{{schema}}
</schema>

<sample_data>
{{sample_data}}
</sample_data>

Question: {{question}}

Additional context: {{additional_context}}
```

## Variables

| Name | Required | Default | Description |
|------|----------|---------|-------------|
| `question` | Yes | — | Natural language query request |
| `schema` | Yes | — | DDL, table descriptions, or column list with types |
| `dialect` | No | PostgreSQL | SQL dialect: PostgreSQL, MySQL, BigQuery, Snowflake |
| `constraints` | No | (none) | Row-level security, naming conventions, banned patterns |
| `sample_data` | No | (none) | Example rows to disambiguate values |
| `default_limit` | No | 1000 | Default LIMIT clause |
| `allow_writes` | No | false | Permit INSERT/UPDATE/DELETE |
| `output_format` | No | SQL block then brief explanation | Response structure |
| `additional_context` | No | (none) | Business definitions, metric formulas |

## Complete Example

### Input Variables

```yaml
dialect: PostgreSQL
schema: |
  orders(id INT, user_id INT, total DECIMAL, status VARCHAR, created_at TIMESTAMP)
  users(id INT, name VARCHAR, email VARCHAR, created_at TIMESTAMP)
question: "What are the top 5 users by total order value in the last 30 days?"
default_limit: 5
```

### Expected Output

```sql
SELECT u.id, u.name, SUM(o.total) AS total_order_value
FROM users u JOIN orders o ON o.user_id = u.id
WHERE o.created_at >= CURRENT_DATE - INTERVAL '30 days'
GROUP BY u.id, u.name ORDER BY total_order_value DESC LIMIT 5;
```

## Evaluation Criteria

| Metric | Target | How to Measure |
|--------|--------|----------------|
| Execution success | > 90% | Run against test database |
| Schema adherence | 100% | No hallucinated tables/columns |
| Result correctness | > 85% | Compare output to golden queries |
| Safety | Zero destructive ops | Block DDL/DML when `allow_writes=false` |
| Performance awareness | Human review | Appropriate indexes, LIMIT, no Cartesian products |

## Tips and Pitfalls

- Provide full schema with keys and relationships; specify `{{dialect}}` explicitly.
- Include `{{sample_data}}` for ambiguous enums; execute in read-only sandbox.
- Always default a row cap via `{{default_limit}}`.
