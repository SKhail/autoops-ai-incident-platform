from database import Base
from sqlalchemy import Column, Integer, String, DateTime, Enum
from enums import Severity


class LogRecord(Base):
    __tablename__ = 'logs'

    id = Column(Integer, primary_key=True)
    service = Column(String)
    severity = Column(Enum(Severity))
    message = Column(String)
    timestamp = Column(DateTime)
