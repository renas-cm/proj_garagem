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

echo "Instalando dependências do sistema para Graphviz..."
# Atualiza a lista de pacotes e instala Graphviz e suas bibliotecas de desenvolvimento
apt-get update
apt-get install -y graphviz libgraphviz-dev pkg-config

echo "Atualizando pip (não estritamente necessário se PDM gerencia, mas não custa)"
pip install --upgrade pip

echo "Instalando PDM para garantir que esteja disponível no ambiente de build do Render"
pip install pdm

echo "Instalando dependências do projeto com PDM"
pdm sync --prod

echo "Coleta os arquivos estáticos"
pdm run python manage.py collectstatic --no-input

echo "Aplica as migrações"
pdm run python manage.py migrate