# API para manipulação de autômatos
Esta API permite criar, testar, visualizar e manipular autômatos finitos, autômatos com pilha e máquinas de Turing.

## Configuração
- Clonar o repositório.
- Criar um ambiente virtual com `python3 -m venv venv` ou `python -m venv venv`
- Ativar o ambiente virtual com `source venv/bin/activate`
- Instalar as dependências com o seguinte comando: `pip install fastapi uvicorn automata-lib graphviz pygraphviz coloraide "fastapi[standard]"`.
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

