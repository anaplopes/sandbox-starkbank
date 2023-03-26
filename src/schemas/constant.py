from enum import Enum


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
