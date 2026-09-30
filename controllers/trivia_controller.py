from fastapi import HTTPException
from services.trivia_service import TriviaService
from models.trivia_models import DifficultyType, QuestionType

trivia_service = TriviaService()

class TriviaController:
    async def get_random_trivia_questions(self, amount: int):
        try:
            questions = await trivia_service.get_random_trivia_questions(amount)
            return questions
        except Exception as error:
            raise HTTPException(status_code=404, detail=str(error))
    async def get_trivia_with_category(self, amount: int, category: int):
        try:
            questions = await trivia_service.get_trivia_with_category(amount, category)
            return questions
        except Exception as error:
            raise HTTPException(status_code=404, detail=str(error))
    async def get_trivia_with_questions_category_difficulty(self, amount: int, category: int, difficulty: DifficultyType):
        try:
            questions = await trivia_service.get_trivia_with_category_difficulty(amount, category, difficulty)
            return questions
        except Exception as error:
            raise HTTPException(status_code=404, detail=str(error))
    async def get_trivia_with_questions_category_difficulty_type(self, amount: int, category: int, difficulty: DifficultyType, type_of_question: QuestionType):
        try:
            questions = await trivia_service.get_trivia_with_category_difficulty_type(amount, category, difficulty, type_of_question)
            return questions
        except Exception as error:
            raise HTTPException(status_code=404, detail=str(error))