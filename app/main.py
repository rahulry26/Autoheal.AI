from fastapi import FastAPI
from app.models.input_model import LogInput
from app.utils.search_fix import find_similar_logs_and_suggest_fix

app = FastAPI()

@app.post("/suggest-fix/")
async def suggest_fix(log_input: LogInput):
    log_text = log_input.log
    suggestion = find_similar_logs_and_suggest_fix(log_text)
    return {"suggestion": suggestion}

