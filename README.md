# Criando o ambiente virtual e Executando o script Python

## Pré-requisitos

- Python 3.11 ou superior instalado no seu sistema.
- Pip instalado no sistema.
- Acesso ao terminal (cmd ou PowerShell).
- O projeto já baixado e dentro de um diretório na sua máquina.

## Passo 1: Criar o Ambiente Virtual

1. Abra o terminal (cmd ou PowerShell).
2. Navegue até o diretório do projeto.
3. Crie um novo ambiente virtual com o comando: `python -m venv .venv`. Isso criará um diretório com o ambiente virtual, o nome do diretório será `.venv`.

## Passo 2: Ativar o Ambiente Virtual

1. Ative o ambiente virtual com o comando: `.venv\Scripts\activate`

## Passo 3: Instalar Dependências

1. Com o ambiente virtual ativado, instale as dependências do seu projeto usando o arquivo `requirements.txt`: `pip install -r requirements.txt`

## Passo 4: Executar o Script Python

1. Com todas as dependências instaladas, você pode executar o seu script Python com o comando: `python manga-scraper.py`
