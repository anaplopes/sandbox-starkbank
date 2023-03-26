from typing import List, Optional
from pydantic import BaseModel


class DiscountsEntity(BaseModel):
    percentage: int
    due: str


class DescriptionEntity(BaseModel):
    key: str
    value: str


class InvoiceEntityReq(BaseModel):
    amount: int
    due: Optional[str]
    expiration: Optional[int]
    name: str
    taxId: str
    fine: Optional[float]
    interest: Optional[float]
    descriptions: Optional[List[DescriptionEntity]]
    discounts: Optional[List[DiscountsEntity]]
    tags: Optional[List[str]]


class InvoiceEntityResp(BaseModel):
    status: str
    updated: str
    fee: int
    taxId: str
    interest: float
    tags: List[str]
    interestAmount: int
    created: str
    due: str
    descriptions: List[DescriptionEntity]
    nominalAmount: int
    discounts: List[DiscountsEntity]
    amount: int
    brcode: str
    expiration: int
    fineAmount: int
    pdf: str
    discountAmount: int
    fine: float
    id: str
    name: str


class InvoicesSchemaResp(BaseModel):
    invoices: List[InvoiceEntityResp]
    message: str


class InvoicesSchemaReq(BaseModel):
    invoices: List[InvoiceEntityReq]
