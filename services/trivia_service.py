import httpx
from models.trivia_models import TriviaQueryParams, TriviaResponse

class TriviaService:
    async def get_trivia_questions(self, params: TriviaQueryParams) -> TriviaResponse:
        
        query_params = params.model_dump(exclude_none=True, mode="json", by_alias=True)

        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.get("https://opentdb.com/api.php", params=query_params)

            response.raise_for_status()

            data = response.json()

            if data.get("response_code") != 0:
                raise Exception("Error fetching trivia questions from external provider.")

            return data