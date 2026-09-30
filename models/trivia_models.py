from pydantic import BaseModel
from typing import List

class TriviaQuestion(BaseModel):
    type: str
    difficulty: str
    category: str
    question: str
    correct_answer: str
    incorrect_answers: List[str]  # Ou apenas list[str] no Python 3.9+

class TriviaResponse(BaseModel):
    response_code: int
    results: List[TriviaQuestion]

class DifficultyType: "easy" or "medium" or "hard"

class QuestionType: "multiple" or "boolean"