# Usa uma imagem oficial do Python como base
FROM python:3.11-slim

# Atualiza o sistema e instala dependências do sistema
RUN apt-get update && apt-get install -y \
    graphviz \
    graphviz-dev \
    build-essential \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos do projeto
COPY . .

# Instala o PDM e as dependências
RUN pip install --upgrade pip && pip install pdm \
    && pdm install --prod

WORKDIR /app/src
# Coleta arquivos estáticos e aplica migrações
RUN pdm run python manage.py collectstatic --no-input \
    && pdm run python manage.py migrate

# Expõe a porta da aplicação (ajuste conforme necessário)
EXPOSE 8000

# Comando para iniciar o servidor (ajuste conforme seu projeto)
CMD ["pdm", "run", "gunicorn", "proj_garagem.wsgi:application", "--bind", "0.0.0.0:8000"]
