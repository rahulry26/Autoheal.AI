# search_fix.py

import os
from langchain_community.vectorstores import Chroma
from utils.embeddings import get_openai_embeddings
from utils.preprocessor import clean_log_text
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

def main():
    # Load Vector DB
    embeddings = get_openai_embeddings()
    db = Chroma(
        embedding_function=embeddings,
        persist_directory="./db/chroma"
    )

    # Take a new log (simulate input)
    new_log = input("Paste the new log to diagnose: ")
    cleaned_log = clean_log_text(new_log)

    # Search for similar logs
    docs = db.similarity_search(cleaned_log, k=2)  # Top 2 matches
    if not docs:
        print("❌ No similar logs found!")
        return

    context = "\n\n".join([doc.page_content for doc in docs])

    # Use ChatGPT to suggest a fix
    chat = ChatOpenAI(
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        temperature=0.2
    )

    prompt = f"""
    You are a DevOps AI. Based on the following previous logs:

    {context}

    And the new log:

    {cleaned_log}

    Suggest a fix or next troubleshooting steps.
    """

    response = chat.invoke(prompt)
    print("\n🔧 Suggested Fix:\n")
    print(response.content)

if __name__ == "__main__":
    main()

