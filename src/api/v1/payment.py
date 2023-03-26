from fastapi import APIRouter, Depends
from src.schemas.payment import Payment
from src.usecases.payment import PaymentUseCase


payment_router = APIRouter(prefix="/payment", tags=["payment"])


@payment_router.post("/invoices")
async def invoice(payment: Payment, service: PaymentUseCase = Depends()):
    return await service.update_invoice(payment=payment)
