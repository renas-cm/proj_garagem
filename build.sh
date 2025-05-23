#!/usr/bin/env bash
# Sai do script se houver algum erro
set -o errexit

# Atualiza o pip
pip install --upgrade pip

# Instala as dependências
pip install -r requirements.txt

ls
# Coleta os arquivos estáticos
python src/manage.py collectstatic --no-input


# Aplica as migrações
python src/manage.py migrate