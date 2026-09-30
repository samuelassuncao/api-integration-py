from fastapi import APIRouter
from controllers.trivia_controller import TriviaController

router = APIRouter()
trivia_controller = TriviaController()

@router.get("/trivia/{amount}")
async def get_random_trivia_questions(amount: int):
    return await trivia_controller.get_random_trivia_questions(amount)
@router.get("/trivia/{amount}/{category}")
async def get_given_category_trivia_questions(amount: int, category: int):
    return await trivia_controller.get_trivia_with_category(amount,category)
@router.get("/trivia/{amount}/{category}/{difficulty}")
async def get_trivia_questions_category_difficulty(amount: int, category: int, difficulty: str):
    return await trivia_controller.get_trivia_with_questions_category_difficulty(amount,category, difficulty)
@router.get("/trivia/{amount}/{category}/{difficulty}/{type_of_question}")
async def get_trivia_questions_category_difficulty_type(amount: int, category: int, difficulty: str, type_of_question: str):
    return await trivia_controller.get_trivia_with_questions_category_difficulty_type(amount,category, difficulty, type_of_question)