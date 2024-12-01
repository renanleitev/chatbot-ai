# Artemis - Chatbot de Acidente de Trânsito

Artemis é um chatbot desenvolvido em Python com uma interface gráfica simples usando a biblioteca `customtkinter`. Ele consulta informações sobre acidentes de trânsito no ano de 2024 a partir de uma tabela pública no Google Sheets e fornece dados como Data, Hora, Natureza, Situação, Bairro e Endereço a partir de um número de Protocolo ou data.

## Base de Dados

A base de dados é referente aos acidentes de trânsito que ocorreram em Recife no ano de 2024.

Fonte: http://dados.recife.pe.gov.br/dataset/acidentes-de-transito-com-e-sem-vitimas/resource/29afbf42-a36c-475c-8b75-761e17e67679

Base de Dados (Google Docs): https://docs.google.com/spreadsheets/d/e/2PACX-1vRcWiuMO_XIUBLdF-11eT8Y-8aaI17b7SwwPvK90yfnMjdTna32DOkXCqlmqe-ODXyoo5LqY0gYlrQx/pubhtml

## Pré-requisitos

- **Python 3.7+**: Verifique se o Python está instalado executando `python --version`.
- **Pip**: Verifique se o Pip está instalado executando `pip --version`.
- **Tkinter**: Verifique se o Tkinter está instalado (e.g. `sudo apt install python3-tk`)
- **Bibliotecas**: `customtkinter`, `requests`, `beautifulsoup4`, `pyinstaller`, `cx-Freeze`

## Clonando o repositório

Para obter a aplicação em seu computador, clone o repositório com o comando abaixo;

    git clone https://github.com/renanleitev/chatbot-ai.git

Depois, vá até a pasta que foi clonada:

    cd chatbot-ai

## Configurando um ambiente virtual (opcional)

Para instalar as dependências localmente, crie um ambiente virtual com o comando abaixo:

    python3 -m venv venv

## Instalando as dependências

Para instalar as dependências, execute o comando abaixo no terminal:

    pip install -r requirements.txt

## Iniciando o chatbot

Para iniciar o chatbot, execute o comando abaixo no terminal:

    python3 chatbot.py

## Gerando um executável

Para gerar um executável (.exe), execute o comando abaixo no terminal:

    python3 setup.py build

O código executável será salvo na pasta `/build` na raiz da aplicação.

Obs: O arquivo executável será gerado de acordo com o sistema operacional utilizado (Linux ou Windows).

Obs: Por padrão, o arquivo `.gitignore` irá excluir a pasta `/build` pois ela é muito pesada para fazer upload no Github.