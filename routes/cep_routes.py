from fastapi import APIRouter
from controllers.conversao_controller import ConversaoController

router = APIRouter()
conversao_controller = ConversaoController()

@router.get("/conversao/{moedas}")
async def retrieve_conversao(moedas: str):
    return await conversao_controller.convert_currency(moedas)