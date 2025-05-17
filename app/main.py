
from fastapi import FastAPI, Request
from pydantic import BaseModel
from app.utils.search_fix import find_best_fix

app = FastAPI()

class FixRequest(BaseModel):
    query: str

@app.get("/")
def read_root():
    return {"message": "🚀 AutoHeal.AI is live. Use POST /get-fix to get solutions."}

@app.post("/get-fix")
async def get_fix(req: FixRequest):
    try:
        fix = find_best_fix(req.query)
        return {"query": req.query, "fix": fix}
    except Exception as e:
        return {"error": str(e)}
