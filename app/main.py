
# main.py

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from utils.search_fix import find_similar_logs_and_suggest_fix

app = FastAPI(
    title="AutoHeal.AI - Intelligent Auto Healing API",
    version="1.0.0"
)

class LogRequest(BaseModel):
    log_text: str

class FixResponse(BaseModel):
    similar_logs: List[str]
    suggested_fix: str

@app.post("/heal-log", response_model=FixResponse)
def heal_log(request: LogRequest):
    log_text = request.log_text
    similar_logs, fix = find_similar_logs_and_suggest_fix(log_text)
    return FixResponse(similar_logs=similar_logs, suggested_fix=fix)

