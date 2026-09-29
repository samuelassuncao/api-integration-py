import httpx

CACHE_TTL_SECONDS = 180
_cep_cache = {}

class ConversaoService:
    async def convert_currency(self, moedas: str) -> dict:
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.get(f"https://economia.awesomeapi.com.br/json/last/{moedas}")

            response.raise_for_status()

            data = response.json()

            if data.get("erro") in ["true", True]:
                raise Exception("Moeda não encontrada")

            return data
        
    async def get_previous_days_currency(self, moedas: str, numero_dias: int) -> list[dict]:
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.get(f"https://economia.awesomeapi.com.br/json/daily/{moedas}/{numero_dias}")

            response.raise_for_status()

            data = response.json()

            if isinstance(data, dict) and data.get("erro") in ["true", True]:
                raise Exception("Moeda não encontrada")

            return data

    