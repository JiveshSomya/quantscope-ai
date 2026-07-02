from fastapi import APIRouter
import httpx

router = APIRouter(prefix="/system", tags=["System"])


@router.get("/health")
async def health():

    async with httpx.AsyncClient() as client:

        rust = await client.get("http://localhost:8081/health")

    return {
        "backend": "OK",
        "rust": rust.text
    }