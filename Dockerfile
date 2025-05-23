# Usa uma imagem oficial do Python como base
FROM python:3.12-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos do projeto
COPY pyproject.toml pdm.lock /app/

# Instala o PDM e as dependências
RUN pip install pdm && \
    pdm install && \
    pdm add django

COPY . .

EXPOSE 8000

CMD ["pdm", "run", "python", "manage.py", "runserver"]
