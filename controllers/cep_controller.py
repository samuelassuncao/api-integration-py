import re
from fastapi import HTTPException
from services.cep_service import CepService

cep_sevice = CepService()

class CepController:
    async def search_adress(self, cep:str):
        clean_cep = re.sub(r"\D", "", cep)

        if len(clean_cep) != 8:
            raise HTTPException(status_code=400, detail="Formato de CEP inválido")

        try:
            adress = await cep_sevice.consult_cep_with_fallback(clean_cep)
            return adress
        except Exception as error:
            raise HTTPException(status_code=400, detail=str(error))