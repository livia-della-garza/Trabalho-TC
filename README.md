# API para manipulação de autômatos
Esta API permite criar, testar, visualizar e manipular autômatos finitos, autômatos com pilha e máquinas de Turing.

## Requisitos
Para a execução deste projeto, é necessário ter o [Python 3](https://www.python.org/) instalado no seu sistema. O projeto foi testado com o Python 3.10.12.

## Configuração
- Clonar o repositório.
- Criar um ambiente virtual com `python3 -m venv venv` ou `python -m venv venv`
- Ativar o ambiente virtual com `source venv/bin/activate`
- Instalar as dependências com o seguinte comando: `pip install -r requirements.txt`.
- Rodar a API com `fastapi dev main.py`.
- Clicar no link indicado no terminal.
- Para acessar a documentação, adicionar `/docs` ao final da URL.

## Utilização da API
### POST /mt/, POST /fa/, POST /pda/
- Cria uma máquina de Turing, um autômato finito ou um autômato com pilha.
- Passar as configurações da máquina em JSON no corpo da requisição.
### GET /mt/image/, GET /fa/image/, GET /pda/image/
- Exibe a imagem da máquina.
- É preciso que a máquina já tenha sido criada.
### GET /mt/, GET /fa/, GET /pda/
- Exibe informações sobre as máquinas.
- É preciso que a máquina já tenha sido criada.
### POST /mt/test/, POST /fa/test/, POST /pda/test/
- Verifica se a máquina armazenada aceita um determinado input.
- Passar o input em JSON no corpo da requisição.

## Exemplos
Acessar a pasta "exemplos" para ter acesso a um exemplo de uso de cada tipo de máquina.

