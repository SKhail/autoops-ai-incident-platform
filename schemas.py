from pydantic import BaseModel
from enums import Severity

class LogCreate(BaseModel):
    service: str
    severity : Severity
    message: str
