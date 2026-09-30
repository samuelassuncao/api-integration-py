from fastapi import FastAPI
from routes.conversao_routes import router as conversao_router
from routes.cep_routes import router as cep_routes

app = FastAPI()

# Inclui as rotas do arquivo de rotas. 
# Se quiser o prefixo de volta no futuro, basta usar: app.include_router(cep_router, prefix="/api")
app.include_router(conversao_router)
app.include_router(cep_routes)

# Mensagem opcional para verificar se o arquivo principal está online
@app.get("/")
def raiz():
    return {"mensagem": "API Python está online!"}