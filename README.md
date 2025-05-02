
# Sistema RAG com FastAPI + FAISS + Ollama

Este projeto implementa um sistema de Perguntas e Respostas (RAG) que:
- Indexa documentos locais com FAISS
- Usa um modelo LLM local via Ollama
- Expõe uma API com FastAPI
- Também possui interfaces CLI e Gradio

---
### Requisitos

- Python 3.11+
- [Ollama](https://ollama.com/download) instalado e com modelo (`mistral`) baixado

---

### Estrutura dos Arquivos

| Arquivo       | Descrição |
|---------------|-----------|
| `ingest.py`   | Indexa um documento `.txt` usando FAISS |
| `main.py`     | API FastAPI com rota POST `/question` |
| `rag.py`      | Interface de terminal (CLI) para perguntas |
| `frontend.py` | Interface gráfica com Gradio |
| `faiss_index/`| Diretório criado após ingestão com índice vetorial |

---

## Instalação (passo a passo)

Abra o CMD (command prompt) no diretório do projeto,
Crie o ambiente virtual:
```
python -m venv rag_env
rag_env\Scripts\activate 
pip install fastapi uvicorn faiss-cpu langchain langchain-community langchain-ollama gradio
```

### Instale o modelo no Ollama:

```bash
ollama pull mistral
```

---

### Indexar documentos (ingestão)

Antes de usar a API ou interface, indexe seus documentos:

```bash
python ingest.py
```

---

### Usar via API (FastAPI)

```bash
uvicorn main:app --reload
```

Acesse a interface em: [http://localhost:8000/docs](http://localhost:8000/docs)

---

### Usar via CLI

```bash
python rag.py
```

---

### Usar via Gradio

```bash
python frontend.py
```

Interface abrirá em: [http://localhost:7860](http://localhost:7860)

---

### Importações usadas

```python
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OllamaEmbeddings
from langchain_ollama import OllamaLLM
from langchain.chains import RetrievalQA
from fastapi import FastAPI
from gradio import Interface
from pydantic import BaseModel
```

---
Exemplo de uso

### Requisição:
```json
POST /question
{
  "question": "Qual o prazo para reembolso?"
}
```

### Resposta:
```json
{
  "answer": "O prazo para reembolso é de até 30 dias após a compra..."
}
```
