import re
from fastapi import HTTPException
from services.conversao_service import ConversaoService

conversao_service = ConversaoService()

class ConversaoController:
    async def convert_currency(self, moedas:str):
        try:
            conversao = await conversao_service.convert_currency(moedas)
            return conversao
        except Exception as error:
            raise HTTPException(status_code=404, detail=str(error))