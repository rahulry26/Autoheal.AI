# app/utils/search_fix.py

from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

persist_directory = './db'
embedding = OpenAIEmbeddings()
vectordb = Chroma(persist_directory=persist_directory, embedding_function=embedding)

def search_fixes(new_log_text):
    similar_docs = vectordb.similarity_search(new_log_text, k=2)
    similar_logs = [doc.page_content for doc in similar_docs]

    prompt_template = """
    You are an intelligent DevOps engineer. Based on the following similar past logs:

    {logs}

    and the current new log:

    {current_log}

    Suggest the most probable root cause and a smart fix.
    """

    prompt = PromptTemplate(
        input_variables=["logs", "current_log"],
        template=prompt_template
    ).format(logs="\n\n".join(similar_logs), current_log=new_log_text)

    llm = ChatOpenAI(model_name="gpt-3.5-turbo")
    response = llm.invoke(prompt)

    return similar_logs, response.content

