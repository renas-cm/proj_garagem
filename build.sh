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

echo "Atualizando pip (não estritamente necessário se PDM gerencia, mas não custa)"
pip install --upgrade pip

echo "Instalando PDM para garantir que esteja disponível no ambiente de build do Render"
pip install pdm

echo "Instalando dependências do projeto com PDM"
# O comando 'pdm install' ou 'pdm sync' irá instalar as dependências de pyproject.toml/pdm.lock
# 'pdm sync --prod' é uma boa opção para garantir apenas dependências de produção
pdm sync --prod

echo "Coleta os arquivos estáticos"
pdm run python manage.py collectstatic --no-input

echo "Aplica as migrações"
pdm run python manage.py migrate

# Opcional: Se você precisa criar um superusuário ou algo do tipo
# echo "Criando superusuário (se necessário)"
# pdm run python manage.py createsuperuser --noinput || true # Use --noinput e || true para não parar o build