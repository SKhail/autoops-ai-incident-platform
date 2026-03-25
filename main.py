from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from enum import Enum 


class Severity(str, Enum):
    INFO = "INFO"
    WARN = "WARN"
    ERROR = "ERROR"

class Log(BaseModel):
    service: str
    severity: Severity
    message: str
    timestamp: datetime

app = FastAPI()

@app.post("/logs/")
async def create_log(log: Log):
   return {
       "status": "log received",
       "log": log
   }