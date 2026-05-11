# 🐳 Guia Completo: Deploy da API em Docker no Render

## 📋 Pré-requisitos

1. **Docker** instalado (https://www.docker.com/)
2. **Conta GitHub** com o repositório da API
3. **Conta Render** (https://render.com/) - gratuita
4. **Git** configurado

---

## 🚀 Fase 1: Testar Localmente com Docker

### 1.1 Construir a Imagem Docker Localmente

```bash
cd c:\Users\danie\Downloads\Fast-Api
docker build -t fast-api-jogos .
```

### 1.2 Rodar o Container

```bash
docker run -p 8000:8000 fast-api-jogos
```

A API estará em: `http://localhost:8000`

### 1.3 Testar

```bash
curl http://localhost:8000/login -X POST -H "Content-Type: application/json" -d '{"email":"usuario@esoft.com","password":"Abc123"}'
```

---

## 📤 Fase 2: Push para GitHub

### 2.1 Inicializar Repositório Git

```bash
cd c:\Users\danie\Downloads\Fast-Api
git init
git config user.name "Seu Nome"
git config user.email "seu.email@example.com"
git add .
git commit -m "Initial commit: API Flask com Docker"
```

### 2.2 Criar Repositório no GitHub

1. Vá para https://github.com/new
2. Nome: `Fast-Api`
3. Descrição: `API de Biblioteca de Jogos`
4. Deixe como **Public** ou **Private**
5. Clique em **Create Repository**

### 2.3 Fazer Push

```bash
git remote add origin https://github.com/SEU_USUARIO/Fast-Api.git
git branch -M main
git push -u origin main
```

---

## 🌐 Fase 3: Deploy no Render

### 3.1 Criar Conta e Conectar GitHub

1. Vá para https://render.com/
2. Clique em **Sign up** (com GitHub é mais fácil)
3. Autorize o Render para acessar seu GitHub
4. Clique em **Dashboard**

### 3.2 Criar Novo Serviço Web

1. Clique em **New +**
2. Selecione **Web Service**
3. Conecte seu repositório GitHub `Fast-Api`
4. Preencha os dados:
   - **Name**: `fast-api-jogos`
   - **Environment**: `Docker`
   - **Build Command**: `docker build -t fast-api-jogos .` (deixe em branco, Render detecta)
   - **Start Command**: `python main.py`
   - **Instance Type**: `Free` (gratuito)

### 3.3 Configurar Variáveis de Ambiente

1. Na aba **Environment**, adicione (opcional):
   - `FLASK_ENV`: `production`
   - `FLASK_APP`: `main.py`

### 3.4 Deploy

1. Clique em **Create Web Service**
2. Render vai:
   - ✅ Detectar o Dockerfile
   - ✅ Construir a imagem
   - ✅ Fazer o deploy
   - ✅ Gerar uma URL pública

---

## 🔗 Fase 4: Acessar a API Online

Após o deploy, você receberá uma URL como:
```
https://fast-api-jogos.onrender.com
```

**Teste:**
```bash
# Login
curl https://fast-api-jogos.onrender.com/login \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{"email":"usuario@esoft.com","password":"Abc123"}'

# Listar jogos
curl https://fast-api-jogos.onrender.com/jogos
```

---

## 📝 Estrutura de Arquivos Necessária

```
Fast-Api/
├── main.py                 ✅ Código principal da API
├── requirements.txt        ✅ Dependências Python
├── Dockerfile              ✅ Configuração Docker
├── .dockerignore            ✅ Arquivos a ignorar
├── docker-compose.yml      ✅ (Opcional) Para teste local
├── README.md               ✅ Documentação
├── .gitignore              ✅ Git ignore
└── .git/                   ✅ Repositório Git
```

---

## 🔄 Atualizar a API no Render

Sempre que você fizer mudanças:

```bash
git add .
git commit -m "Descrição da mudança"
git push origin main
```

**Render detecta automaticamente** e faz o redeploy! 🚀

---

## ⚙️ Dockerfile Explicado

```dockerfile
# Usa Python 3.11 slim (menor tamanho)
FROM python:3.11-slim

# Define pasta de trabalho no container
WORKDIR /app

# Copia requirements
COPY requirements.txt .

# Instala dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia código
COPY . .

# Porta que a API usa
EXPOSE 8000

# Comando para iniciar
CMD ["python", "main.py"]
```

---

## 🔧 Troubleshooting

### ❌ "Build failed"
- Verifique se o Dockerfile está na raiz do repositório
- Confirme que `requirements.txt` existe
- Teste localmente: `docker build -t test .`

### ❌ "Connection refused"
- Verifique se a porta 8000 está aberta
- No Render, a aplicação deve escutar em `0.0.0.0:8000`

### ❌ "500 Internal Server Error"
- Verifique logs: Render → Logs
- Procure por erros de importação ou sintaxe

### ❌ "Free instance sleeping"
- Plano Free do Render coloca apps em sleep após 15 min de inatividade
- Primeira requisição pode demorar 30 segundos
- Para produção, use plano pago

---

## 📊 Monitorar a API

### No Render Dashboard:
- Clique no seu serviço `fast-api-jogos`
- Abas úteis:
  - **Logs**: Ver logs da aplicação em tempo real
  - **Metrics**: CPU, Memória, Requisições
  - **Settings**: Configurar variáveis de ambiente
  - **Deploy**: Histórico de deployments

---

## 🎯 Resumo do Fluxo

```
┌─────────────────────────────────┐
│  1. Código Local (main.py)      │
│     + requirements.txt          │
│     + Dockerfile                │
└────────────┬────────────────────┘
             │
             ▼
┌─────────────────────────────────┐
│  2. Push para GitHub            │
│     git push origin main        │
└────────────┬────────────────────┘
             │
             ▼
┌─────────────────────────────────┐
│  3. Render Detects              │
│     Pull from GitHub            │
│     Build Docker Image          │
│     Start Container             │
└────────────┬────────────────────┘
             │
             ▼
┌─────────────────────────────────┐
│  4. API Online                  │
│     https://fast-api-xxx.com    │
│     Acessível ao mundo!         │
└─────────────────────────────────┘
```

---

## ✅ Checklist Final

- [ ] Dockerfile criado e testado localmente
- [ ] requirements.txt tem todas as dependências
- [ ] Código está no GitHub
- [ ] Conta Render criada
- [ ] Web Service criado no Render
- [ ] Deploy realizado com sucesso
- [ ] API respondendo em https://fast-api-jogos.onrender.com
- [ ] Endpoints testados online

---

## 🚀 Próximos Passos (Opcional)

Para produção profissional:
- Usar `gunicorn` em vez de dev server
- Adicionar SSL/HTTPS
- Usar banco de dados persistente (PostgreSQL)
- Implementar JWT para autenticação real
- CI/CD com GitHub Actions

```bash
# Instalar gunicorn
pip install gunicorn

# Usar no Dockerfile
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "main:app"]
```

---

**Pronto! Sua API estará online em minutos! 🎉**
