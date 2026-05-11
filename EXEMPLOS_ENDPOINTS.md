# 📚 Como Usar Todos os Endpoints da API

Guia completo com exemplos práticos de como usar cada endpoint da API.

---

## ✅ Pré-requisitos

- API rodando em `http://localhost:8000`
- **cURL** instalado (ou qualquer cliente HTTP como Postman, Insomnia)

---

## 🔐 1️⃣ LOGIN - Obter Token UUID

Primeiro, faça login para gerar um token aleatório:

```bash
curl -X POST "http://localhost:8000/login" \
  -H "Content-Type: application/json" \
  -d '{"email":"usuario@esoft.com","password":"Abc123"}'
```

**Resposta (200 OK):**
```json
{
  "token": "550e8400-e29b-41d4-a716-446655440000"
}
```

⚠️ **Nota:** Cada vez que faz login, um UUID diferente é gerado!

**Teste com credenciais inválidas:**
```bash
curl -X POST "http://localhost:8000/login" \
  -H "Content-Type: application/json" \
  -d '{"email":"teste@email.com","password":"senha123"}'
```

Resposta (401): `{"detail": "Email ou senha inválidos"}`

---

## 📋 2️⃣ LISTAR TODOS OS JOGOS

Recupera a lista completa de todos os jogos cadastrados:

```bash
curl -X GET "http://localhost:8000/jogos"
```

**Resposta (200 OK):**
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

---

## 🎮 3️⃣ OBTER JOGO POR ID

Busca os dados completos de um jogo específico:

```bash
curl -X GET "http://localhost:8000/jogos/1"
```

**Resposta (200 OK):**
```json
{
  "id": 1,
  "nome": "The Legend of Zelda",
  "tipo": "Aventura",
  "nota": 10,
  "review": "Um clássico absoluto."
}
```

**Se o jogo não existir:**
```bash
curl -X GET "http://localhost:8000/jogos/999"
```

Resposta (404): `{"detail": "Jogo com id 999 não encontrado"}`

---

## ➕ 4️⃣ CRIAR NOVO JOGO

Adiciona uma nova review de jogo à biblioteca:

```bash
curl -X POST "http://localhost:8000/jogos" \
  -H "Content-Type: application/json" \
  -d '{
    "nome": "Elden Ring",
    "tipo": "RPG",
    "nota": 9,
    "review": "Desafiador e visualmente impecável."
  }'
```

**Resposta (201 Created):**
```json
{
  "id": 3,
  "nome": "Elden Ring",
  "tipo": "RPG",
  "nota": 9,
  "review": "Desafiador e visualmente impecável."
}
```

**Criar outro jogo:**
```bash
curl -X POST "http://localhost:8000/jogos" \
  -H "Content-Type: application/json" \
  -d '{
    "nome": "Hollow Knight",
    "tipo": "Plataforma",
    "nota": 8,
    "review": "Excelente metroidvania com arte impressionante."
  }'
```

Resposta (201): ID 4 será atribuído automaticamente

**Se faltar algum campo obrigatório:**
```bash
curl -X POST "http://localhost:8000/jogos" \
  -H "Content-Type: application/json" \
  -d '{"nome": "Teste"}'
```

Resposta (400): `{"detail": "Nome, tipo, nota e review são obrigatórios"}`

---

## ✏️ 5️⃣ ATUALIZAR JOGO

Modifica TODOS os dados de um jogo existente:

```bash
curl -X PUT "http://localhost:8000/jogos/3" \
  -H "Content-Type: application/json" \
  -d '{
    "nome": "Elden Ring - DLC",
    "tipo": "RPG",
    "nota": 10,
    "review": "Melhorou o que já era perfeito. Imprescindível!"
  }'
```

**Resposta (200 OK):**
```json
{
  "id": 3,
  "nome": "Elden Ring - DLC",
  "tipo": "RPG",
  "nota": 10,
  "review": "Melhorou o que já era perfeito. Imprescindível!"
}
```

**Atualizar o jogo com ID 1:**
```bash
curl -X PUT "http://localhost:8000/jogos/1" \
  -H "Content-Type: application/json" \
  -d '{
    "nome": "The Legend of Zelda (Remasterizado)",
    "tipo": "Aventura RPG",
    "nota": 10,
    "review": "A melhor remasterização de um clássico!"
  }'
```

⚠️ **Importante:** Todos os 4 campos são obrigatórios. Se falta algum:

```bash
curl -X PUT "http://localhost:8000/jogos/1" \
  -H "Content-Type: application/json" \
  -d '{"nome": "Novo Nome"}'
```

Resposta (400): `{"detail": "Nome, tipo, nota e review são obrigatórios"}`

---

## 🗑️ 6️⃣ DELETAR JOGO

Remove um jogo da biblioteca:

```bash
curl -X DELETE "http://localhost:8000/jogos/3"
```

**Resposta (204 No Content):**
```
(Sem corpo de resposta)
```

**Deletar outro jogo:**
```bash
curl -X DELETE "http://localhost:8000/jogos/4"
```

**Se o jogo não existir:**
```bash
curl -X DELETE "http://localhost:8000/jogos/999"
```

Resposta (404): `{"detail": "Jogo com id 999 não encontrado"}`

---

## 📝 FLUXO COMPLETO DE USO

Aqui está um exemplo de como usar a API do início ao fim:

```bash
# 1️⃣ Fazer login e gerar token UUID aleatório
curl -X POST "http://localhost:8000/login" \
  -H "Content-Type: application/json" \
  -d '{"email":"usuario@esoft.com","password":"Abc123"}'
# → Resposta: {"token": "550e8400-e29b-41d4-a716-446655440000"}

# 2️⃣ Listar todos os jogos existentes
curl -X GET "http://localhost:8000/jogos"
# → Retorna os 2 jogos pré-carregados

# 3️⃣ Obter detalhes do primeiro jogo
curl -X GET "http://localhost:8000/jogos/1"
# → Retorna dados completos de Zelda

# 4️⃣ Adicionar novo jogo
curl -X POST "http://localhost:8000/jogos" \
  -H "Content-Type: application/json" \
  -d '{
    "nome": "Stardew Valley",
    "tipo": "Simulação",
    "nota": 9,
    "review": "Relaxante e altamente viciante."
  }'
# → Recebe ID 3

# 5️⃣ Obter detalhes do novo jogo
curl -X GET "http://localhost:8000/jogos/3"
# → Confirma que foi criado

# 6️⃣ Atualizar o jogo com nova avaliação
curl -X PUT "http://localhost:8000/jogos/3" \
  -H "Content-Type: application/json" \
  -d '{
    "nome": "Stardew Valley",
    "tipo": "Simulação",
    "nota": 10,
    "review": "Masterpiece! O melhor jogo indie que jogou."
  }'
# → ID 3 é atualizado

# 7️⃣ Listar novamente para confirmar mudanças
curl -X GET "http://localhost:8000/jogos"
# → Agora mostra 3 jogos com Stardew Valley atualizado

# 8️⃣ Deletar o jogo de teste
curl -X DELETE "http://localhost:8000/jogos/3"
# → Jogo removido

# 9️⃣ Verificar lista final
curl -X GET "http://localhost:8000/jogos"
# → Volta para 2 jogos originais
```

---

## 🧪 TESTAR EM INTERFACE GRÁFICA

Se preferir uma interface gráfica em vez de cURL:

### Opção 1: Postman
1. Download: https://www.postman.com/
2. Criar nova requisição
3. Configurar método HTTP, URL e corpo

### Opção 2: Insomnia
1. Download: https://insomnia.rest/
2. Criar workspace
3. Importar endpoints

### Opção 3: Thunder Client (VS Code)
1. Extensão: Thunder Client no VS Code
2. Criar requisições visualmente

### Opção 4: REST Client (VS Code)
Criar arquivo `test.http`:
```http
### Login
POST http://localhost:8000/login
Content-Type: application/json

{
  "email": "usuario@esoft.com",
  "password": "Abc123"
}

### Listar Jogos
GET http://localhost:8000/jogos

### Criar Jogo
POST http://localhost:8000/jogos
Content-Type: application/json

{
  "nome": "Test Game",
  "tipo": "Ação",
  "nota": 7,
  "review": "Teste"
}
```

---

## 📊 RESUMO DOS ENDPOINTS

| # | Método | URL | Função |
|----|--------|-----|--------|
| 1 | POST | `/login` | Gera UUID aleatório |
| 2 | GET | `/jogos` | Lista todos os jogos |
| 3 | GET | `/jogos/{id}` | Obtém jogo específico |
| 4 | POST | `/jogos` | Cria novo jogo |
| 5 | PUT | `/jogos/{id}` | Atualiza jogo existente |
| 6 | DELETE | `/jogos/{id}` | Deleta jogo |

---

## ✅ CÓDIGOS DE STATUS ESPERADOS

- **200 OK** - Requisição bem-sucedida (GET, PUT)
- **201 Created** - Recurso criado (POST)
- **204 No Content** - Requisição bem-sucedida sem corpo (DELETE)
- **400 Bad Request** - Dados inválidos ou campos obrigatórios faltando
- **401 Unauthorized** - Email/senha incorretos no login
- **404 Not Found** - Jogo não encontrado

---

## 💡 DICAS

✅ Use `http://localhost:8000` ao testar localmente
✅ Todos os campos são **case-sensitive**
✅ A nota pode ser qualquer número (não precisa ser 1-10)
✅ IDs são auto-incrementados a partir de 1
✅ Dados são perdidos ao reiniciar o servidor (armazenamento em memória)

---

**Pronto! Agora você sabe usar todos os 6 endpoints da API! 🚀**
