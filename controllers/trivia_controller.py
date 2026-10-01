from typing import Optional
from fastapi import HTTPException
from services.trivia_service import TriviaService
from models.trivia_models import TriviaQueryParams

trivia_service = TriviaService()

class TriviaController:
    async def get_trivia_questions(self, params: TriviaQueryParams):
        try:
            questions = await trivia_service.get_trivia_questions(params)
            return questions
        except Exception as error:
            raise HTTPException(status_code=400, detail=str(error))