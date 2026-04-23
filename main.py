from fastapi import Depends, FastAPI, Query
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

# push the logs into the database
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

# get the logs information from the simulated logs
@app.get("/logs")
def read_log(
    session: Session = Depends(get_session),
    offset: int = Query(default=0),
    limit: int = Query(default=50, le=100)
    ): 
    logs = (
        session.query(LogRecord)
        .order_by(LogRecord.timestamp.desc())\
        .offset(offset)\
        .limit(limit).all()
    )
    return logs
    