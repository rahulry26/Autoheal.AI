# app/schemas.py

from pydantic import BaseModel

class LogRequest(BaseModel):
    log_text: str

class FixResponse(BaseModel):
    similar_logs: list
    suggested_fix: str

