from fastapi import FastAPI
from pydantic import BaseModel
from app.utils.search_fix import find_best_fix

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.post("/get-fix")
def get_fix(request: QueryRequest):
    query = request.query
    fix = find_best_fix(query)
    return {"query": query, "fix": fix}

