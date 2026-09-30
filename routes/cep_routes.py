from fastapi import APIRouter
from controllers.cep_controller import CepController

router = APIRouter()
cep_controller = CepController()

@router.get("/cep/{cep}")
async def retrieve_cep(cep: str):
    return await cep_controller.search_adress(cep)