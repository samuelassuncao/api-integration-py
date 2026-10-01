from fastapi import APIRouter, Query
from controllers.trivia_controller import TriviaController
from models.trivia_models import TriviaQueryParams

router = APIRouter()
trivia_controller = TriviaController()

@router.get("/trivia")
async def get_trivia_questions(params: TriviaQueryParams = Query()):
    return await trivia_controller.get_trivia_questions(params)