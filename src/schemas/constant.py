from enum import Enum
from pydantic import BaseModel
from typing import List, Optional, Any


class IncomingType(str, Enum):
    PAYMENT = "payment"


class OutgoingType(str, Enum):
    INVOICE = "invoice"
    TRANSFER = "transfer"


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


class InvoiceTag(str, Enum):
    SCHEDULED = "scheduled"
    IMMEDIATE = "immediate"


class AccountType(str, Enum):
    PAYMENT = "payment"
    SALARY = "salary"


class BankCode(str, Enum):
    TED = "033"
    PIX = "20018183"


class StarkBankAccount(str, Enum):
    BRANCH_CODE = ("0001",)
    ACCOUNT_NUMBER = ("6341320293482496",)
    TAX_ID = ("20.018.183/0001-80",)
    NAME = "Stark Bank S.A."


class Output(BaseModel):
    data: Optional[List[Any]] = []
    message: str
    error: Optional[str] = None
    statusCode: int
