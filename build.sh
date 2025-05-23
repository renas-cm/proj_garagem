# #!/usr/bin/env bash
# # Sai do script se houver algum erro
# set -o errexit

# # Atualiza o pip
# pip install --upgrade pip

# # Instala as dependências
# pip install -r requirements.txt

# # Coleta os arquivos estáticos
# python manage.py collectstatic --no-input

# # Aplica as migrações
# python manage.py migrate


#!/usr/bin/env bash
# Sai do script se houver algum erro
set -e

echo "Atualizando pip (opcional, mas seguro)"
pip install --upgrade pip

echo "Instalando PDM no ambiente de build"
pip install pdm

echo "Instalando dependências do projeto com PDM"
pdm sync --prod  # Use --prod para instalar apenas dependências de produção

echo "Coleta os arquivos estáticos"
pdm run python manage.py collectstatic --no-input

echo "Aplica as migrações"
pdm run python manage.py migrate

# Se você tiver testes que quer rodar no build, pode adicionar aqui:
# echo "Rodando testes"
# pdm run python manage.py test