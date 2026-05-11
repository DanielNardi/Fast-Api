@echo off
REM Script para setup inicial do repositório Git no Windows

setlocal enabledelayedexpansion

echo ================================
echo   Setup Repositorio Fast-Api
echo ================================
echo.

REM Verificar se Git está instalado
git --version >nul 2>&1
if errorlevel 1 (
    echo Erro: Git nao esta instalado!
    pause
    exit /b 1
)

REM Configurar Git
echo.
set /p git_name="Digite seu nome completo (ou pressione Enter para pular): "
if not "!git_name!"=="" (
    git config --global user.name "!git_name!"
)

set /p git_email="Digite seu email (ou pressione Enter para pular): "
if not "!git_email!"=="" (
    git config --global user.email "!git_email!"
)

REM Inicializar repositório
echo.
echo Inicializando repositorio Git...
git init

REM Adicionar todos os arquivos
echo Adicionando arquivos...
git add .

REM Criar commit inicial
echo Criando commit inicial...
git commit -m "Chore: Configuracao inicial do projeto com Docker"

echo.
echo ✓ Repositorio inicializado com sucesso!
echo.
echo Proximos passos:
echo 1. Crie um repositorio em https://github.com/new
echo 2. Execute no terminal:
echo    git remote add origin https://github.com/SEU_USUARIO/Fast-Api.git
echo    git branch -M main
echo    git push -u origin main
echo.
pause
