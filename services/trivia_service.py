import httpx
from models.trivia_models import DifficultyType, QuestionType, TriviaResponse

class TriviaService:
    async def get_random_trivia_questions(self, amount: int) -> TriviaResponse:
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.get(f"https://opentdb.com/api.php?amount={amount}")

            response.raise_for_status()

            data = response.json()

            if data.get("response_code") != 0:
                raise Exception("Request error")

            return data
    async def get_trivia_with_category(self, amount: int, category: int) -> TriviaResponse:
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.get(f"https://opentdb.com/api.php?amount={amount}&category={category}")

            response.raise_for_status()

            data = response.json()

            if data.get("response_code") != 0:
                raise Exception("Request error")

            return data
    async def get_trivia_with_category_difficulty(self, amount: int, category: int, difficulty: DifficultyType) -> TriviaResponse:
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.get(f"https://opentdb.com/api.php?amount={amount}&category={category}&difficulty{difficulty}")

            response.raise_for_status()

            data = response.json()

            if data.get("response_code") != 0:
                raise Exception("Request error")

            return data
    async def get_trivia_with_category_difficulty_type(self, amount: int, category: int, difficulty: DifficultyType, type_of_question: QuestionType) -> TriviaResponse:
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.get(f"https://opentdb.com/api.php?amount={amount}&category={category}&difficulty{difficulty}&type={type_of_question}")

            response.raise_for_status()

            data = response.json()

            if data.get("response_code") != 0:
                raise Exception("Request error")

            return data