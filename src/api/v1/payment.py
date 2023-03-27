from fastapi import APIRouter, Depends
from src.schemas.payment import Payment
from src.usecases.payment import PaymentUseCase


payment_router = APIRouter(prefix="/payment", tags=["payment"])


@payment_router.post("/invoice")
async def invoice(payment: Payment, service: PaymentUseCase = Depends()):
    return await service.save_payment(payment=payment)
