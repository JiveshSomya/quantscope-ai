import httpx

RUST_ENGINE_URL = "http://localhost:8081"


async def analyze_portfolio(payload):

    async with httpx.AsyncClient(timeout=20.0) as client:

        try:

            response = await client.post(
                f"{RUST_ENGINE_URL}/analyze",
                json=payload,
            )

            response.raise_for_status()

            return response.json()

        except httpx.HTTPError as e:

            return {
                "error": str(e)
            }