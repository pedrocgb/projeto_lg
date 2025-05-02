from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings, OllamaLLM
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from pathlib import Path

app = FastAPI()

class Question(BaseModel):
    question: str

index_path = Path(__file__).resolve().parent.parent / "faiss_index"
embeddings = OllamaEmbeddings(model="mistral")
db = FAISS.load_local(str(index_path), embeddings, allow_dangerous_deserialization=True)
retriever = db.as_retriever()

prompt_template = """Você é um assistente útil e direto, que responde em português. 
Mantenha termos técnicos, nomes próprios e marcas no idioma original, mas traduza todo o resto.

Contexto:
{context}

Pergunta:
{question}
"""

custom_prompt = PromptTemplate(
    template=prompt_template,
    input_variables=["context", "question"]
)

qa = RetrievalQA.from_chain_type(
    llm=OllamaLLM(model="mistral"),
    retriever=retriever,
    chain_type_kwargs={"prompt": custom_prompt},
    return_source_documents=False
)

@app.post("/perguntar")
def responder(question: Question):
    try:
        answer = qa.run(question.question)
        return {"resposta": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
