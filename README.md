# Automação WhatsApp Supabase + Z-API

Projeto desenvolvido em Python para buscar contatos no Supabase e enviar mensagens personalizadas via Z-API.

## Tecnologias

- Python
- Supabase
- Z-API
- Requests
- dotenv


## Banco

Criar tabela:

contatos

Campos:

id
nome
telefone


## Variáveis de ambiente

Criar arquivo .env:

SUPABASE_URL=
SUPABASE_KEY=

ZAPI_INSTANCE=
ZAPI_TOKEN=
ZAPI_CLIENT_TOKEN=


## Instalação

Executar:

pip install -r requirements.txt


## Rodar

python main.py


## Funcionamento

O sistema busca até 3 contatos no Supabase e envia:

"Olá, <nome_contato> tudo bem com você?"
