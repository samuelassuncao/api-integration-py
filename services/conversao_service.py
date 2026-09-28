import httpx
from datetime import datetime, timedelta

CACHE_TTL_SECONDS = 180
_cep_cache = {}

class ConversaoService:
    async def convert_currency(self, moedas: str) -> dict:
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.get(f"https://economia.awesomeapi.com.br/json/last/{moedas}")

            response.raise_for_status()

            data = response.json()

            if data.get("erro") in ["true", True]:
                raise Exception("Moeda não encontrada")

            return data

    async def consult_brasil_api(self, cep: str) -> dict:
        async with httpx.AsyncClient(timeout=5.0) as client:
                    response = await client.get(f"https://brasilapi.com.br/api/cep/v2/{cep}")
        
                    response.raise_for_status()

                    if response.status != 200:
                        raise Exception("Erro ao buscar CEP nos dois serviços")
        
                    data = response.json()
        
                    return {
                        "cep": data.get("cep"),
                        "logradouro": data.get("street"),
                        "bairro": data.get("neighborhood"),
                        "localidade": data.get("city"),
                        "uf": data.get("state"),
                        "origem": "BrasilAPI (Fallback)"
                    }
    async def consult_cep_with_fallback(self, cep:str) -> dict:

        now = datetime.now()

        if cep in _cep_cache:
            cache_item = _cep_cache[cep]
            elapsed_time = now - cache_item["created_at"]

            if elapsed_time < timedelta(seconds=CACHE_TTL_SECONDS):
                remaining_seconds = CACHE_TTL_SECONDS - int(elapsed_time.total_seconds())
                print(f"CEP {cep} encontrado na memória. Expira em {remaining_seconds} segundos")
                return dict(_cep_cache[cep])
            else:
                print(f"[CACHE EXPIRADO] Cache do CEP {cep} expirou. Deletando dados...")
                del _cep_cache[cep]
        print("CEP não está na memória. Buscando na API")
        try:
            print(f"Tentando ViaCEP para o CEP {cep}")
            address = await self.consult_via_cep(cep)
            address["origem"] = "ViaCEP (Principal)"
            _cep_cache[cep] = {
                "data": address,
                "created_at": now
            }
            return address
        except Exception as erro_viacep:
            print(f"ViaCEP falhou pelo motivo: {erro_viacep}. Tentando BrasilAPI")
            try:
                print(f"Tentando BrasilAPI para o CEP {cep}")
                address = await self.consult_brasil_api(cep)
                _cep_cache[cep] = {
                    "data": address,
                    "created_at": now
                }
                return address
            except Exception as final_error:
                raise Exception(str(final_error))