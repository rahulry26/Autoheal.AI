# app/main.py

from fastapi import FastAPI
from app.schemas import LogRequest, FixResponse
from utils.search_fix import find_similar_logs_and_suggest_fix
import os
import uvicorn

app = FastAPI(
    title="AutoHeal.AI - Intelligent Auto Healing API",
    version="1.0.0"
)

@app.post("/heal-log", response_model=FixResponse)
def heal_log(request: LogRequest):
    log_text = request.log_text
    similar_logs, fix = find_similar_logs_and_suggest_fix(log_text)
    return FixResponse(similar_logs=similar_logs, suggested_fix=fix)

# Make sure this block is added
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Default fallback
    uvicorn.run("main:app", host="0.0.0.0", port=port)

