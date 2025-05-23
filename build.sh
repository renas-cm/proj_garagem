#!/usr/bin/env bash
set -o errexit

# Atualiza o PDM
pdm self update

# Instala as dependências
pdm install

# Coleta os arquivos estáticos
pdm run python manage.py collectstatic --no-input

# Aplica as migrações
pdm run python manage.py migrate
