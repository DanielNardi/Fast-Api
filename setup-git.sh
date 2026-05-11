#!/bin/bash
# Script para setup inicial do repositório Git e fazer primeiro commit

echo "================================"
echo "  Setup Repositório Fast-Api"
echo "================================"
echo ""

# Verificar se Git está instalado
if ! command -v git &> /dev/null; then
    echo "❌ Git não está instalado!"
    exit 1
fi

# Configurar Git (se necessário)
read -p "Digite seu nome completo (ou pressione Enter para pular): " git_name
if [ ! -z "$git_name" ]; then
    git config --global user.name "$git_name"
fi

read -p "Digite seu email (ou pressione Enter para pular): " git_email
if [ ! -z "$git_email" ]; then
    git config --global user.email "$git_email"
fi

# Inicializar repositório
echo "Inicializando repositório Git..."
git init

# Adicionar todos os arquivos
echo "Adicionando arquivos..."
git add .

# Criar commit inicial
echo "Criando commit inicial..."
git commit -m "Chore: Configuração inicial do projeto com Docker"

echo ""
echo "✅ Repositório inicializado com sucesso!"
echo ""
echo "Próximos passos:"
echo "1. Crie um repositório em https://github.com/new"
echo "2. Execute:"
echo "   git remote add origin https://github.com/SEU_USUARIO/Fast-Api.git"
echo "   git branch -M main"
echo "   git push -u origin main"
echo ""
