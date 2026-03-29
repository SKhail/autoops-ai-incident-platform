from fastapi import FastAPI
from database import engine, Base
from models import Log

Base.metadata.create_all(engine)

app = FastAPI()

# @app.post("/logs")
# async def create_log(log: Log):
#    return {
#     "status": "log received",
#     "log": log
#    }

