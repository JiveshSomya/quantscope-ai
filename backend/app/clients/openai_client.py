from openai import OpenAI

from app.config import settings

client = OpenAI(
    api_key=settings.OPENAI_API_KEY
)


dimport json

from openai import OpenAI

from app.config import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)


def ask_llm(prompt: str):

    response = client.chat.completions.create(

        model="gpt-4.1-mini",

        response_format={"type": "json_object"},

        messages=[
            {
                "role": "system",
                "content": """
Return ONLY JSON.

Format:

{
 "risk":"",
 "summary":"",
 "strengths":[],
 "weaknesses":[],
 "recommendations":[]
}
"""
            },

            {
                "role":"user",
                "content":prompt
            }

        ],
    )

    return json.loads(
        response.choices[0].message.content
    )