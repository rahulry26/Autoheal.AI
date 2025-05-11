from fastapi import FastAPI
from app.schemas import LogRequest, FixResponse
from utils.search_fix import find_similar_logs_and_suggest_fix

app = FastAPI(
    title="AutoHeal.AI - Intelligent Auto Healing API",
    version="1.0.0"
)

@app.post("/heal-log", response_model=FixResponse)
def heal_log(request: LogRequest):
    log_text = request.log_text
    similar_logs, fix = find_similar_logs_and_suggest_fix(log_text)
    return FixResponse(similar_logs=similar_logs, suggested_fix=fix)

