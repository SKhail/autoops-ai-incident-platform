from database import Base
from sqlalchemy import Column, Integer, String, DateTime, Enum
from datetime import datetime
from enums import Severity
class Log(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    service = Column(String)
    severity = Column(Enum(Severity))
    message = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
