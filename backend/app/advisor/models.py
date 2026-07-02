from pydantic import BaseModel


class AIReport(BaseModel):
    risk: str
    summary: str
    strengths: list[str]
    weaknesses: list[str]
    recommendations: list[str]