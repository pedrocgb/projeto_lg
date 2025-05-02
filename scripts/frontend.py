from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings, OllamaLLM
from langchain.chains import RetrievalQA
import gradio as gr
from pathlib import Path

embeddings = OllamaEmbeddings(model="mistral")
index_path = Path(__file__).resolve().parent.parent / "faiss_index"
db = FAISS.load_local(str(index_path), embeddings, allow_dangerous_deserialization=True)
retriever = db.as_retriever()

from langchain.prompts import PromptTemplate

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

def responder_gradio(pergunta):
    return qa.run(pergunta)

gr.Interface(
    fn=responder_gradio,
    inputs="text",
    outputs="text",
    title="Assistente RAG",
    description="Digite sua pergunta sobre os documentos e receba uma resposta gerada pelo modelo local.",
).launch()
