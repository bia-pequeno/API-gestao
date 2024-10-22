#Definição de rotas - Endpoints
# POST, PUT, GET, DELETE

#Armazenar dados
#Pessoa: nome, nascimento, endereço, cpf, estado_civil

#Validação de dados
#Pydantic pra validação dos tipos e formatos de dados.

#Operações de CRUID
#implementação das operações de Create, Read, Update e Delete com os métodos (POST, GET, PUT, DELETE).

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware 
from pydantic import BaseModel, Field
from typing import List
from datetime import date
from starlette.responses import JSONResponse

app = FastAPI(
    title="API de Gestão de Pessoas",
    description="Essa API permite o cadastro e a gestão de informações de pessoas. "
                "Inclui funcionalidades como cadastro, consulta, atualização e exclusão.",
    version="1.0.0",
    contact={
        "name": "Beatriz",
        "email": "bia.2017pequeno@gmail.com",
    },
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_methods=["*"], 
)

#'Banco de dados' em memória
database = {}

#Pessoa
class Pessoa(BaseModel):
    nome_completo: str
    data_nascimento: date
    endereco: str
    cpf: str = Field(..., pattern="^\\d{3}\\.\\d{3}\\.\\d{3}\\-\\d{2}$"
)
    estado_civil: str

#Listar todas as pessoas
@app.get("/", response_model=List[Pessoa])
def home():
    return list(database.values())

#Criar Pessoa
@app.post("/pessoa/inserir", response_model=Pessoa)
def criar_pessoa(pessoa: Pessoa):
    print(pessoa)
    if pessoa.cpf in database:
        raise HTTPException(status_code=400, detail="CPF já cadastrado.")
    database[pessoa.cpf] = pessoa

    return JSONResponse(content={"mensagem": "CPF cadastrado com sucesso"}, status_code=201)

#Buscar Pessoa
@app.get("/pessoa/buscar/{cpf}")
def buscar_pessoa(cpf: str):
    pessoa = database.get(cpf)
    if pessoa is None:
        raise HTTPException(status_code=404, detail="Pessoa não encontrada.")

    return pessoa

#Editar/Att dados de pessoa
@app.put("/pessoa/editar{cpf}", response_model=Pessoa)
def editar_dados(cpf: str, dados_atualizados: Pessoa):
    if cpf not in database:
        raise HTTPException(status_code=404, detail="Pessoa não encontrada.")
    database[cpf] = dados_atualizados

    return JSONResponse(content={"mensagem": "Dados atualizados com sucesso"}, status_code=201)

#Deletar
@app.delete('/pessoa/apagar{cpf}', response_model=Pessoa)
def deletar_pessoa(cpf:str):
    if cpf not in database:
        raise HTTPException(status_code=404, detail="Pessoa não encontrada.")
    del database[cpf]

    return JSONResponse(content={"mensagem": "CPF deletado do sistema com sucesso"}, status_code=201)