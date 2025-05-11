from fastapi import FastAPI, Request
from pydantic import BaseModel
from utils.search_fix import find_similar_logs_and_suggest_fix
import traceback

app = FastAPI()

class LogRequest(BaseModel):
    log_text: str

@app.get("/")
def root():
    return {"message": "AutoHeal.AI is live!"}

@app.post("/analyze")
async def analyze_log(request: LogRequest):
    try:
        similar_logs, fix = find_similar_logs_and_suggest_fix(request.log_text)
        return {
            "similar_logs": similar_logs,
            "suggested_fix": fix
        }
    except Exception as e:
        print("⚠️ Exception occurred:", e)
        traceback.print_exc()  # shows full stack trace
        return {
            "error": str(e),
            "details": traceback.format_exc()
        }

