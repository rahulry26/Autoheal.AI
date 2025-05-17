from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.base import Embeddings

import os

# Set Chroma directory
CHROMA_DIR = "chroma_db"

def find_best_fix(user_query: str) -> str:
    """
    Given a user query (e.g., error or log message),
    returns the most relevant fix from the vector store.
    """
    # Ensure Chroma directory exists
    if not os.path.exists(CHROMA_DIR):
        raise FileNotFoundError(f"Chroma DB directory '{CHROMA_DIR}' not found")

    # Load the embedding model
    embeddings: Embeddings = OpenAIEmbeddings()

    # Load the Chroma vector store
    db = Chroma(persist_directory=CHROMA_DIR, embedding_function=embeddings)

    # Search for the most relevant fix
    results = db.similarity_search(user_query, k=1)

    if results:
        return results[0].page_content
    else:
        return "No relevant fix found in the knowledge base."

