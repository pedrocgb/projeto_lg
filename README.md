
# Sistema RAG com FastAPI + FAISS + Ollama

Este projeto implementa um sistema de Perguntas e Respostas (RAG) que:
- Indexa documentos locais com FAISS
- Usa um modelo LLM local via Ollama
- Expõe uma API com FastAPI
- Também possui interfaces CLI e Gradio

---
### Requisitos

- [Python 3.11+](https://www.python.org/downloads/)
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

- Abra o CMD (command prompt) no diretório do projeto
- Crie o ambiente virtual inserindo as linhas de códigos:
```
python -m venv rag_env
```
- Depois basta ativar o ambiente virtual (você também pode executar o arquivo Start.bat para inicializar o terminal com maior facilidade):
```
rag_env\Scripts\activate
```
- Após inicialização do ambiente, vamos instalar todas as depedências:
```
pip install fastapi uvicorn faiss-cpu langchain langchain-community langchain-ollama gradio
```
- Após criado o ambiente virtual, vamos instalar o modelo mistral no Ollama.
```bash
ollama pull mistral
```

---

### Inicializando
Conforme descrito acima, precisamos do Ollama instalado e rodando em sua máquina.
Após feito a instalação, certifique-se que o Ollama está aberto e rodando corretamente.
Use o comando 'ollama serve' no terminal ou PowerShell para inicializa-lo.

---

### Indexar documentos (ingestão)
Para utilização desta IA, você primeiro precisa fazer a ingestão do documento (dados.txt).
Para isso. rodamos o script ingest.py, ele é responsável pelo indexamento do documento.
Esse comando deve ser utilizado dentro da pasta scripts.

```bash
python ingest.py
```

---
Para a utilização dessa IA, você possui 3 alternativas de interface, sendo elas:
- CLI (terminal)
- Fast API (interface simples)
- Gradio (interface mais robusta)
Escolha umas delas e rode usando seu respectivo script.
Lembrando que eles devem ser utilizados dentro da pasta scripts.

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
## Exemplo de uso
O documento a ser indexado (dados.txt) é um documento com definições gerais sobre IA's Large Language Models (LLM). Você pode fazer perguntas seguindo este modelo:
- Qual o significado de LLM?
- Cite alguns exemplos de aplicações de uma LLM
- Como funcionam as LLMs?

### Requisição:
```json
POST /question
{
  "question": "Como funcionam as LLMs?"
}
```

### Resposta:
```json
{
  "answer": "As LLMs têm uma ampla gama de aplicações, incluindo: tradução automática, resumo de textos, analise de sentimentos em textos, assistência pessoal virtual e assistência às empresas. Além disso, eles também podem ser usados para gerar conteúdos como notícias, artigos e histórias."
}
```
