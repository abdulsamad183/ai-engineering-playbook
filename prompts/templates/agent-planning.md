---
title: "Agent Planning Prompt Template"
description: "Reusable prompt for decomposing complex tasks into executable steps with tool selection and dependencies."
domain: prompt-engineering
tags: [prompt, agent, planning, reasoning, tools]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
id: agent-planning-v1
task: agent-planning
models:
  recommended: [gpt-4o, claude-sonnet-4]
  min_capability: advanced
token_budget:
  system: 450
  user_per_request: 300
variables:
  required: [goal, available_tools]
  optional: [constraints, context, max_steps, output_format]
output:
  format: json
  schema: agent_plan
related:
  - rag-query.md
  - evaluation-judge.md
  - ../../domains/prompt-engineering/prompt-templates-guide.md
keywords: [agent planning, task decomposition, tool use, ReAct]
---

# Agent Planning Prompt Template

> Decompose a complex goal into ordered, executable steps. Select tools, identify dependencies, and flag risks before execution.

## Pattern Overview

| Attribute | Value |
|-----------|-------|
| Use Case | Autonomous agents, multi-step workflows, research tasks, orchestration |
| Best Models | gpt-4o, claude-sonnet-4 |
| Complexity | Complex |
| Token Budget | ~600–1500 tokens (system + user) |
| Expected Output | JSON plan with steps, tools, and success criteria |

## When to Use

- Agent loops that plan before executing tools
- Breaking user requests into subtasks with clear dependencies
- Research or analysis tasks spanning multiple data sources
- Human-in-the-loop workflows needing upfront transparency

## When Not to Use

- Single-step tasks answerable in one tool call or one LLM response
- Real-time tasks where planning latency exceeds user tolerance
- Goals with insufficient tool coverage (plan will fail at execution)

## System Prompt

```
You are a strategic planning agent for {{domain}}.

Create an execution plan to achieve the user's goal using ONLY these tools:

{{available_tools}}

Constraints:
{{constraints}}

Rules:
- Maximum {{max_steps}} steps.
- Each step must specify: id, description, tool, tool_input, depends_on, success_criteria.
- Use tool names exactly as listed. Do not invent tools.
- Identify steps that can run in parallel vs. sequential dependencies.
- Flag risks, missing information, or assumptions in a separate "risks" array.
- If the goal is impossible with available tools, return a plan with step 1 as "clarify_goal".

Output format (valid JSON only):
{{output_format}}
```

## User Prompt

```
Goal: {{goal}}

Current context:
{{context}}

Prior execution results (if replanning):
{{prior_results}}

User preferences: {{user_preferences}}
```

## Variables

| Name | Required | Default | Description |
|------|----------|---------|-------------|
| `goal` | Yes | — | High-level objective to accomplish |
| `available_tools` | Yes | — | Tool catalog with name, description, and input schema |
| `domain` | No | general task automation | Domain for planning heuristics |
| `constraints` | No | minimize tool calls; prefer read before write | Budget, safety, ordering rules |
| `context` | No | (none) | Current state, user info, session history |
| `max_steps` | No | 8 | Maximum plan steps |
| `prior_results` | No | (none) | Results from previous steps when replanning |
| `user_preferences` | No | (none) | Speed vs. thoroughness, approval requirements |
| `output_format` | No | see below | JSON plan schema |

Default `output_format`: `{"goal_summary": "...", "risks": ["..."], "steps": [{"id": 1, "tool": "...", "tool_input": {}, "depends_on": [], "success_criteria": "..."}]}`

## Complete Example

### Input

```yaml
goal: "Find Q3 revenue from annual report and email summary to CFO."
available_tools: "search_documents(query), send_email(to, subject, body)"
max_steps: 5
```

### Expected Output

```json
{"goal_summary": "Extract Q3 revenue and draft CFO email.", "steps": [{"id": 1, "tool": "search_documents", "tool_input": {"query": "Q3 revenue"}, "depends_on": []}, {"id": 2, "tool": "send_email", "depends_on": [1]}]}
```

## Evaluation Criteria

| Metric | Target | How to Measure |
|--------|--------|----------------|
| Goal coverage | > 90% | Plan steps address all parts of goal |
| Tool validity | 100% | Only listed tools referenced |
| Executability | > 85% | Plan completes without replanning |
| Step efficiency | ≤ max_steps | No redundant steps |
| Risk identification | Human review | Material risks flagged upfront |

## Tips and Pitfalls

- Document tools with input schemas; keep runtime catalog in sync with the prompt.
- Pass `{{prior_results}}` when replanning; cap `{{max_steps}}` to prevent runaway plans.
- Route single-step goals to direct execution — do not over-plan simple tasks.
