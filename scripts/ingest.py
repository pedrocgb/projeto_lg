from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OllamaEmbeddings


def ingest(file_path: str):
    print(f"Iniciando ingestão de: {file_path}")
    loader = TextLoader(file_path)
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(documents)

    embeddings = OllamaEmbeddings(model="mistral")

    db = FAISS.from_documents(chunks, embeddings)

    db.save_local("../faiss_index")
    print("Ingestão concluída com sucesso.")

if __name__ == "__main__":
    ingest("../data/dados.txt")