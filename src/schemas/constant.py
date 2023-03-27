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
    CREATED = "created"
    OPEN = "open"
    PAID = "paid"
    OVERDUE = "overdue"  # atrasada
    CANCELED = "canceled"
    VOIDED = "voided"  # anulada
    EXPIRED = "expired"


class Output(BaseModel):
    data: Optional[List[Any]] = []
    message: str
    error: Optional[str] = None
    statusCode: int
