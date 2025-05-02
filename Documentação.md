
# Documentação Técnica dos Scripts - Projeto RAG com LangChain, FAISS e Ollama

Este projeto contém 4 scripts principais que compõem um sistema de Recuperação Aumentada por Geração (RAG) com FastAPI, Gradio e integração com modelos locais via Ollama.

---

## Estrutura dos Scripts

### 1. `ingest.py` - Ingestão e Indexação
Responsável por carregar arquivos de texto (.txt), dividir em chunks e criar um índice vetorial com FAISS.

- Carrega documentos com `TextLoader` (codificação UTF-8)
- Usa `RecursiveCharacterTextSplitter` para segmentar texto
- Gera embeddings com `OllamaEmbeddings` (modelo mistral)
- Salva o índice FAISS localmente em `faiss_index/`
- Deve ser executado sempre que novos documentos forem adicionados

Exemplo de uso:
```bash
python ingest.py
```

---

### 2. `main.py` – API FastAPI
Implementa uma API com FastAPI para responder perguntas sobre os documentos indexados.

- Carrega índice FAISS existente
- Usa `RetrievalQA` para responder perguntas com contexto
- Expõe uma rota POST `/perguntar`
- A documentação interativa pode ser acessada em `/docs`

Exemplo de execução:
```bash
uvicorn main:app --reload
```

---

### 3. `frontend.py` – Interface Gradio
Fornece uma interface gráfica via navegador usando Gradio.

- Carrega o mesmo índice FAISS
- Usa o mesmo `RetrievalQA`
- Permite enviar perguntas por uma interface simples em `http://localhost:7860`
- É ideal para demonstrações locais sem API

Exemplo de execução:
```bash
python frontend.py
```

---

### 4. `rag.py` – Interface de Terminal (CLI)
Versão de linha de comando para testar perguntas e respostas diretamente no terminal.

- Executa um loop interativo de perguntas
- Usa `RetrievalQA` com o modelo e índice local
- Útil para testes rápidos ou desenvolvimento offline

Exemplo:
```bash
python rag.py
```

---

## Notas sobre o ambiente

- Requer que o modelo Mistral esteja disponível no Ollama:
  ```bash
  ollama pull mistral
  ```

- Requer FAISS e LangChain instalados:
  ```bash
  pip install fastapi uvicorn faiss-cpu langchain langchain-community langchain-ollama gradio
  ```

- Todos os arquivos `.txt` usados para ingestão devem estar codificados em UTF-8

---

