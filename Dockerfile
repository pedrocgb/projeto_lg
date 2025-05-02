# Dockerfile para sistema RAG com FastAPI, FAISS, Ollama
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Instalar dependências básicas
RUN apt-get update && apt-get install -y curl && pip install --upgrade pip

# Criar diretório da aplicação
WORKDIR /app

# Copiar arquivos do projeto
COPY requirements.txt ./
COPY scripts/ ./scripts
COPY faiss_index/ ./faiss_index

# Instalar dependências
RUN pip install -r requirements.txt

# Definir diretório padrão para execução
WORKDIR /app/scripts

# Rodar FastAPI via Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
