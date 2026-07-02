from fastapi import APIRouter

from app.advisor.service import generate_advice

router = APIRouter(
    prefix="/advisor",
    tags=["Advisor"]
)


@router.post("/")
def advisor(data: dict):

    return generate_advice(
        data["summary"],
        data["analysis"],
    )