from app.advisor.prompt import build_prompt

from app.clients.openai_client import ask_llm


def generate_advice(summary, analysis):

    prompt = build_prompt(
        summary,
        analysis,
    )

    report = ask_llm(prompt)

    return {

        "report": report
    }