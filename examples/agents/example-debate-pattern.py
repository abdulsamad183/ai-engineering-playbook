"""Debate pattern — two agents argue, supervisor synthesizes.

Run: python example-debate-pattern.py
"""

from __future__ import annotations


async def debate(topic: str, pro_agent, con_agent, judge) -> str:
    pro = await pro_agent(f"Argue FOR: {topic}")
    con = await con_agent(f"Argue AGAINST: {topic}")
    return await judge(f"Topic: {topic}\nPro: {pro}\nCon: {con}\nSynthesize balanced answer.")


async def mock_llm(prompt: str) -> str:
    if "FOR" in prompt:
        return "Pro: Automation improves efficiency."
    if "AGAINST" in prompt:
        return "Con: Automation risks job displacement without guardrails."
    return "Balanced: Adopt automation with retraining programs."


if __name__ == "__main__":
    import asyncio
    print(asyncio.run(debate("AI automation in factories", mock_llm, mock_llm, mock_llm)))
