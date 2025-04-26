
# utils/embeddings.py

import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings

load_dotenv()

def get_openai_embeddings():
    """
    Returns an instance of OpenAI Embeddings with your API key loaded.
    """
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        raise ValueError("OpenAI API Key not found in environment variables!")

    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
    return embeddings

