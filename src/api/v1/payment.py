from fastapi import APIRouter, Depends
from src.usecases.payment import PaymentUseCase


payment_router = APIRouter(prefix="/payment", tags=["payment"])


@payment_router.post("/invoice")
async def invoice(payment, service: PaymentUseCase = Depends()):
    return await service.receive_payment(payment=payment)
