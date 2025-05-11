# app/main.py

from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from utils.search_fix import search_fixes

app = FastAPI()

class LogInput(BaseModel):
    log: str

@app.get("/")
def root():
    return {"message": "AutoHeal.AI is live!"}

@app.post("/analyze")
def analyze_log(input: LogInput):
    try:
        similar_logs, suggestion = search_fixes(input.log)
        return {
            "input_log": input.log,
            "similar_logs": similar_logs,
            "suggested_fix": suggestion
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

