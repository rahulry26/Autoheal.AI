from fastapi import FastAPI
from pydantic import BaseModel
from app.utils.search_fix import find_best_fix

app = FastAPI()

class LogInput(BaseModel):
    log_text: str

@app.post("/suggest_fix")
async def suggest_fix(log: LogInput):
    result = find_best_fix(log.log_text)
    return {"suggested_fix": result}

