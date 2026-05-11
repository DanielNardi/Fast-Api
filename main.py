from flask import Flask, request, jsonify
from flask_cors import CORS
import uuid
import json

app = Flask(__name__)
CORS(app)  # Habilitar CORS para todas as rotas

# Armazenamento em memória
jogos_db = {
    1: {
        "id": 1,
        "nome": "The Legend of Zelda",
        "tipo": "Aventura",
        "nota": 10,
        "review": "Um clássico absoluto."
    },
    2: {
        "id": 2,
        "nome": "FIFA 23",
        "tipo": "Esporte",
        "nota": 7,
        "review": "Bom para jogar com amigos."
    }
}

proximo_id = [3]  # Usar lista para modificação em função

# Credenciais válidas
CREDENCIAIS_VALIDAS = {
    "email": "usuario@esoft.com",
    "password": "Abc123"
}

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
    app.run(host="0.0.0.0", port=8000, debug=False)
