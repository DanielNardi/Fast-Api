
## Requisitos

- Python 3.8+
- pip

## Instalação

1. Navegue até o diretório do projeto:
```bash
cd Fast-Api
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Executar a API

```bash
python main.py
```

A API estará disponível em: `http://localhost:8000`

## Documentação Interativa

Após iniciar a API, acesse:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Endpoints

### 1. Login
**POST** `/login`

Realiza autenticação básica.

**Credenciais válidas:**
- Email: `usuario@esoft.com`
- Password: `Abc123`

**Request:**
```json
{
  "email": "usuario@esoft.com",
  "password": "Abc123"
}
```

**Response (200 OK):**
```json
{
  "token": "550e8400-e29b-41d4-a716-446655440000"
}
```

### 2. Listar Jogos
**GET** `/jogos`

Retorna a lista completa de jogos e reviews cadastrados.

**Response (200 OK):**
```json
[
  {
    "id": 1,
    "nome": "The Legend of Zelda",
    "tipo": "Aventura",
    "nota": 10,
    "review": "Um clássico absoluto."
  },
  {
    "id": 2,
    "nome": "FIFA 23",
    "tipo": "Esporte",
    "nota": 7,
    "review": "Bom para jogar com amigos."
  }
]
```

### 3. Obter Jogo por ID
**GET** `/jogos/{id}`

Busca os detalhes de um jogo específico pelo seu identificador único.

**Response (200 OK):**
```json
{
  "id": 1,
  "nome": "The Legend of Zelda",
  "tipo": "Aventura",
  "nota": 10,
  "review": "Um clássico absoluto."
}
```

### 4. Criar Jogo
**POST** `/jogos`

Cadastra uma nova review de jogo.

**Request:**
```json
{
  "nome": "Elden Ring",
  "tipo": "RPG",
  "nota": 9,
  "review": "Desafiador e visualmente impecável."
}
```

**Response (201 Created):**
```json
{
  "id": 3,
  "nome": "Elden Ring",
  "tipo": "RPG",
  "nota": 9,
  "review": "Desafiador e visualmente impecável."
}
```

### 5. Atualizar Jogo
**PUT** `/jogos/{id}`

Atualiza todos os dados de um jogo existente. Obrigatório preencher todos os campos.

**Request:**
```json
{
  "nome": "Elden Ring - DLC",
  "tipo": "RPG",
  "nota": 10,
  "review": "Melhorou o que já era perfeito."
}
```

**Response (200 OK):**
```json
{
  "id": 3,
  "nome": "Elden Ring - DLC",
  "tipo": "RPG",
  "nota": 10,
  "review": "Melhorou o que já era perfeito."
}
```

### 6. Deletar Jogo
**DELETE** `/jogos/{id}`

Remove a review do sistema.

**Response (204 No Content):**
Sem corpo de resposta.

## Características

✅ Autenticação com UUID aleatório
✅ CRUD completo de jogos
✅ Validação de dados com Pydantic
✅ Documentação automática com Swagger UI
✅ Armazenamento em memória
✅ Códigos de status HTTP corretos
✅ Tratamento de erros

## Exemplos de Teste

### Usando cURL

**Login:**
```bash
curl -X POST "http://localhost:8000/login" \
  -H "Content-Type: application/json" \
  -d '{"email":"usuario@esoft.com","password":"Abc123"}'
```

**Listar jogos:**
```bash
curl -X GET "http://localhost:8000/jogos"
```

**Criar jogo:**
```bash
curl -X POST "http://localhost:8000/jogos" \
  -H "Content-Type: application/json" \
  -d '{"nome":"Hollow Knight","tipo":"Plataforma","nota":8,"review":"Excelente jogo de plataforma"}'
```

**Obter jogo:**
```bash
curl -X GET "http://localhost:8000/jogos/1"
```

**Atualizar jogo:**
```bash
curl -X PUT "http://localhost:8000/jogos/1" \
  -H "Content-Type: application/json" \
  -d '{"nome":"The Legend of Zelda Remaster","tipo":"Aventura","nota":10,"review":"Ainda é um clássico"}'
```

**Deletar jogo:**
```bash
curl -X DELETE "http://localhost:8000/jogos/1"
```
