from enum import Enum
from pydantic import BaseModel
from typing import List, Optional, Any


class IncomingType(str, Enum):
    PAYMENT = "payment"


class OutgoingType(str, Enum):
    INVOICE = "invoice"


class State(str, Enum):
    SENT = "sent"
    FAILED = "failed"
    OPEN = "open"
    PAID = "paid"
    ISSUED = "issued"
    CREDITED = "credited"


class Output(BaseModel):
    data: Optional[List[Any]] = []
    message: str
    error: Optional[str] = None
    statusCode: int
