from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings, OllamaLLM
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

def main():
    embeddings = OllamaEmbeddings(model="mistral")
    db = FAISS.load_local("../faiss_index", embeddings, allow_dangerous_deserialization=True)
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

    print("Digite sua pergunta (ou 'sair' para encerrar):\n")
    while True:
        pergunta = input("Pergunta: ")
        if pergunta.strip().lower() in ["sair", "exit", "quit"]:
            break
        resposta = qa.run(pergunta)
        print("Resposta:", resposta)

if __name__ == "__main__":
    main()
