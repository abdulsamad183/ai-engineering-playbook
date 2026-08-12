# From mini ReAct → agent starter

> Path from the offline toy agent to the agent template.

## 1. Run the mini (no API keys)

```bash
python3 examples/agents/mini_react/run.py
```

What you learn: thought → tool → observation → final answer, with a sandboxed calculator.

## 2. Graduate to the starter

```bash
cp -r templates/engineering/agent-starter my-agent
cd my-agent
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
```

Read [agent-starter README](../../templates/engineering/agent-starter/README.md).

## 3. Next hardening

- [AI Agents handbook](../../domains/ai-agents/README.md)
- [MCP](../../domains/mcp/README.md)
- [Agent evaluation](../../domains/ai-evaluation/surface-areas/03-agent-evaluation.md)
