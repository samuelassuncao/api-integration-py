from fastapi import APIRouter
from controllers.conversao_controller import ConversaoController

router = APIRouter()
conversao_controller = ConversaoController()

@router.get("/conversao/{moedas}")
async def retrieve_conversao(moedas: str):
    return await conversao_controller.convert_currency(moedas)

@router.get("/conversao/{moedas}/{numero_dias}")
async def retrieve_conversao(moedas: str, numero_dias: int):
    return await conversao_controller.get_previous_days_currency(moedas, numero_dias)