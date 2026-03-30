from fastapi import Depends, FastAPI
from database import engine, Base
from datetime import datetime
from sqlalchemy.orm import Session
from contextlib import asynccontextmanager
from models import LogRecord
from schemas import LogCreate


def create_database_and_tables():
   Base.metadata.create_all(engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
   create_database_and_tables()
   yield

app = FastAPI(lifespan=lifespan)


def get_session():
    with Session(engine) as session:
        yield session

@app.post("/logs")
def create_log(log: LogCreate, session: Session = Depends(get_session)):
    db_log = LogRecord(
        service=log.service,
        severity=log.severity,
        message=log.message,
        timestamp=datetime.now()
    )
    session.add(db_log)
    session.commit()
    session.refresh(db_log)
    return db_log 


