from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import TextLoader
import os

persist_directory = "./chroma_db"

def find_similar_logs_and_suggest_fix(log: str) -> str:
    embedding = OpenAIEmbeddings()
    vectordb = Chroma(
        persist_directory=persist_directory,
        embedding_function=embedding
    )
    docs = vectordb.similarity_search(log, k=1)
    if docs:
        return docs[0].page_content
    else:
        return "No similar log found. Please check input or enrich your vector store."

