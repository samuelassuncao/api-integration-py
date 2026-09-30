from fastapi import FastAPI
from routes.conversao_routes import router as conversao_router
from routes.cep_routes import router as cep_router
from routes.trivia_routes import router as trivia_router

app = FastAPI()

app.include_router(conversao_router)
app.include_router(cep_router)
app.include_router(trivia_router)

# Mensagem opcional para verificar se o arquivo principal está online
@app.get("/")
def raiz():
    return {"mensagem": "API Python está online!"}