# API de Gestão de Pessoas

Esta é uma API desenvolvida em FastAPI que permite o cadastro e a gestão de informações de pessoas. A API inclui funcionalidades como cadastro, consulta, atualização e exclusão de dados de pessoas.

## Funcionalidades

- **Cadastro de Pessoa:** Permite inserir uma nova pessoa no sistema.
- **Consulta de Pessoa:** Possibilita buscar informações de uma pessoa pelo CPF.
- **Edição de Dados:** Permite atualizar as informações de uma pessoa cadastrada.
- **Exclusão de Pessoa:** Permite remover uma pessoa do sistema.

## Tecnologias Utilizadas

- **FastAPI:** Framework web para construção de APIs.
- **Pydantic:** Biblioteca para validação de dados.
- **CORS Middleware:** Para permitir requisições de diferentes origens.

## Endpoints


```
### 1. Listar Todas as Pessoas
GET /
Retorna uma lista de todas as pessoas cadastradas.

### 2. Criar Pessoa
POST /pessoa/inserir
body
  json{
    "nome_completo": "Nome Completo",
    "data_nascimento": "YYYY-MM-DD",
    "endereco": "Endereço da Pessoa",
    "cpf": "XXX.XXX.XXX-XX",
    "estado_civil": "Estado Civil"
  }
response
 json{
  "mensagem": "CPF cadastrado com sucesso"
}

### 3. Buscar Pessoa
GET /pessoa/buscar/{cpf}
Retorna os dados da pessoa correspondente ao CPF fornecido.

### 4. Editar Dados da Pessoa
PUT /pessoa/editar{cpf}
body
  json{
    "nome_completo": "Nome Atualizado",
    "data_nascimento": "YYYY-MM-DD",
    "endereco": "Novo Endereço",
    "cpf": "XXX.XXX.XXX-XX",
    "estado_civil": "Novo Estado Civil"
  }
Response
  json{
    "mensagem": "Dados atualizados com sucesso"
  }

### 5. Deletar Pessoa
DELETE /pessoa/apagar{cpf}
Retorna uma mensagem de sucesso ao deletar a pessoa correspondente ao CPF fornecido.
```

### Estrutura do Projeto
/api-gestao-pessoas
└── projectpython
    ├── main.py
    └── index.html

### Requisitos
- **Python 3.7 ou superior**
- **FastAPI**
- **Uvicorn**

### Instalação
- **Clone este repositório:**
- git clone https://github.com/bia-pequeno/API-gestao.git
  
###  **Navegue até o diretório do projeto:**
- cd API-gestao-pessoas/projectpython
  
###  **Crie um Virtual Environment:**
- python -m venv myenv
  
###  **Instale as dependências:**
-     pip install fastapi
-     pip install uvicorn
-     pip install starlette

### Execução
- **Para iniciar a API, utilize o comando:**
-     uvicorn main:app --reload

A API estará disponível em http://127.0.0.1:8000.

### Acessando a Documentação da API
- **Acesse a Documentação:**
- Após iniciar o servidor, abra o navegador e digite o seguinte endereço na barra de endereços:
-     http://127.0.0.1:8000/docs
- Essa URL abrirá a interface de documentação gerada automaticamente pelo FastAPI usando Swagger UI.
  - **Explorando a Documentação:**
  - Na interface do Swagger UI, você verá todos os endpoints disponíveis da sua API listados, junto com informações sobre cada um, como método HTTP, descrição, parâmetros e modelos de resposta.
  - Você pode testar os endpoints diretamente na interface clicando nos botões de "Try it out" e preenchendo os campos necessários.
  - **Documentação Alternativa:**
  - Além do Swagger UI, o FastAPI também fornece uma documentação alternativa usando ReDoc. Você pode acessá-la pelo seguinte endereço:
  -     http://127.0.0.1:8000/redoc

    
  

### Autora
  Desenvolvedora: Beatriz Pequeno
