from flask import Flask, request, jsonify
from flask_cors import CORS
import uuid
import json
import os

app = Flask(__name__)
CORS(app)  # Habilitar CORS para todas as rotas

# Arquivo de dados persistente
DADOS_FILE = "dados_jogos.json"

# Dados iniciais padrão
DADOS_PADRAO = {
    "jogos": {
        "1": {
            "id": 1,
            "nome": "The Legend of Zelda",
            "tipo": "Aventura",
            "nota": 10,
            "review": "Um clássico absoluto."
        },
        "2": {
            "id": 2,
            "nome": "FIFA 23",
            "tipo": "Esporte",
            "nota": 7,
            "review": "Bom para jogar com amigos."
        }
    },
    "proximo_id": 3
}

def carregar_dados():
    """Carrega dados do arquivo JSON ou cria arquivo com dados padrão."""
    if os.path.exists(DADOS_FILE):
        try:
            with open(DADOS_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            print(f"Erro ao ler {DADOS_FILE}, usando dados padrão")
            salvar_dados(DADOS_PADRAO)
            return DADOS_PADRAO
    else:
        # Criar arquivo com dados padrão
        salvar_dados(DADOS_PADRAO)
        return DADOS_PADRAO

def salvar_dados(dados):
    """Salva dados em arquivo JSON."""
    try:
        with open(DADOS_FILE, 'w', encoding='utf-8') as f:
            json.dump(dados, f, ensure_ascii=False, indent=2)
    except IOError as e:
        print(f"Erro ao salvar dados: {e}")

# Carregar dados ao iniciar
dados = carregar_dados()
jogos_db = {int(k): v for k, v in dados["jogos"].items()}
proximo_id = [dados["proximo_id"]]

# Credenciais válidas
CREDENCIAIS_VALIDAS = {
    "email": "usuario@esoft.com",
    "password": "Abc123"
}

def persistir_dados():
    """Salva o estado atual da memória no arquivo JSON."""
    dados_para_salvar = {
        "jogos": {str(k): v for k, v in jogos_db.items()},
        "proximo_id": proximo_id[0]
    }
    salvar_dados(dados_para_salvar)

# ==================== ENDPOINTS ====================

@app.route("/login", methods=["POST"])
def login():
    """
    Realiza a autenticação básica para uso da API.
    
    Credenciais válidas:
    - email: usuario@esoft.com
    - password: Abc123
    """
    data = request.get_json()
    
    if not data or "email" not in data or "password" not in data:
        return jsonify({"detail": "Email e password são obrigatórios"}), 400
    
    email = data.get("email")
    password = data.get("password")
    
    if email == CREDENCIAIS_VALIDAS["email"] and password == CREDENCIAIS_VALIDAS["password"]:
        # Gera um UUID aleatório
        token = str(uuid.uuid4())
        return jsonify({"token": token}), 200
    else:
        return jsonify({"detail": "Email ou senha inválidos"}), 401

@app.route("/jogos", methods=["GET"])
def listar_jogos():
    """
    Retorna a lista completa de jogos e reviews cadastrados.
    """
    return jsonify(list(jogos_db.values())), 200

@app.route("/jogos/<int:id>", methods=["GET"])
def obter_jogo(id):
    """
    Busca os detalhes de um jogo específico pelo seu identificador único.
    """
    if id not in jogos_db:
        return jsonify({"detail": f"Jogo com id {id} não encontrado"}), 404
    
    return jsonify(jogos_db[id]), 200

@app.route("/jogos", methods=["POST"])
def criar_jogo():
    """
    Cadastra uma nova review de jogo.
    """
    data = request.get_json()
    
    if not data or "nome" not in data or "tipo" not in data or "nota" not in data or "review" not in data:
        return jsonify({"detail": "Nome, tipo, nota e review são obrigatórios"}), 400
    
    novo_jogo = {
        "id": proximo_id[0],
        "nome": data.get("nome"),
        "tipo": data.get("tipo"),
        "nota": data.get("nota"),
        "review": data.get("review")
    }
    
    jogos_db[proximo_id[0]] = novo_jogo
    proximo_id[0] += 1
    
    # ✅ Salvar dados no arquivo
    persistir_dados()
    
    return jsonify(novo_jogo), 201

@app.route("/jogos/<int:id>", methods=["PUT"])
def atualizar_jogo(id):
    """
    Atualiza todos os dados de um jogo existente.
    Obrigatório preencher todos os campos no request.
    """
    if id not in jogos_db:
        return jsonify({"detail": f"Jogo com id {id} não encontrado"}), 404
    
    data = request.get_json()
    
    if not data or "nome" not in data or "tipo" not in data or "nota" not in data or "review" not in data:
        return jsonify({"detail": "Nome, tipo, nota e review são obrigatórios"}), 400
    
    jogos_db[id] = {
        "id": id,
        "nome": data.get("nome"),
        "tipo": data.get("tipo"),
        "nota": data.get("nota"),
        "review": data.get("review")
    }
    
    # ✅ Salvar dados no arquivo
    persistir_dados()
    
    return jsonify(jogos_db[id]), 200

@app.route("/jogos/<int:id>", methods=["DELETE"])
def deletar_jogo(id):
    """
    Remove a review do sistema.
    Retorna 204 No Content (sem corpo de resposta).
    """
    if id not in jogos_db:
        return jsonify({"detail": f"Jogo com id {id} não encontrado"}), 404
    
    del jogos_db[id]
    
    # ✅ Salvar dados no arquivo
    persistir_dados()
    
    return "", 204

# ==================== TRATAMENTO DE ERROS ====================

@app.errorhandler(404)
def nao_encontrado(error):
    return jsonify({"detail": "Rota não encontrada"}), 404

@app.errorhandler(405)
def metodo_nao_permitido(error):
    return jsonify({"detail": "Método não permitido"}), 405

# ==================== INICIALIZAÇÃO ====================

if __name__ == "__main__":
    print("=" * 50)
    print("🚀 Iniciando API Biblioteca de Jogos")
    print("=" * 50)
    print(f"📁 Arquivo de dados: {DADOS_FILE}")
    print(f"📊 Jogos carregados: {len(jogos_db)}")
    print(f"🔄 Próximo ID disponível: {proximo_id[0]}")
    print("=" * 50)
    print("🌐 API disponível em: http://0.0.0.0:8000")
    print("💾 Dados persistidos em: dados_jogos.json")
    print("=" * 50)
    app.run(host="0.0.0.0", port=8000, debug=False)
