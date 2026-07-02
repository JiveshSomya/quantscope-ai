from app.advisor.knowledge import KNOWLEDGE


def build_prompt(summary, analysis):

    return f"""
You are an expert financial advisor.

Knowledge

{KNOWLEDGE}

Portfolio Summary

{summary}

Risk Analysis

{analysis}

Write

- Portfolio health
- Risk explanation
- Diversification advice
- Improvement suggestions
- Keep under 150 words.
"""