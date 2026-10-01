from pydantic import BaseModel
from typing import List
from typing import Optional
from pydantic import BaseModel, Field
from enum import Enum

class TriviaQuestion(BaseModel):
    type: str
    difficulty: str
    category: str
    question: str
    correct_answer: str
    incorrect_answers: List[str]

class TriviaResponse(BaseModel):
    response_code: int
    results: List[TriviaQuestion]

from enum import Enum

class DifficultyType(str, Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"

class QuestionType(str, Enum):
    MULTIPLE = "multiple"
    BOOLEAN = "boolean"

class TriviaQueryParams(BaseModel):
    amount: int = Field(..., description="Quantidade de perguntas desejadas (obrigatório)")
    category: Optional[int] = Field(None, description="ID da categoria")
    difficulty: Optional[DifficultyType] = Field(None, description="Dificuldade das perguntas")
    type_of_question: Optional[QuestionType] = Field(
        None,
        alias="type",
        description="Tipo das perguntas")