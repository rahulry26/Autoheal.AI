from fastapi import FastAPI
from app.utils.search_fix import find_similar_logs_and_suggest_fix
from app.models.input_model import LogInput

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "AutoHeal.AI is live!"}

@app.post("/suggest-fix")
def suggest_fix(log_input: LogInput):
    result = find_similar_logs_and_suggest_fix(log_input.query)
    return {"suggestion": result}

