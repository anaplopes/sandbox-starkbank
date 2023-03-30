from fastapi import APIRouter, Depends
from src.usecases.payment import PaymentUseCase
from src.usecases.invoice import InvoiceUseCase


payment_router = APIRouter(prefix="/payment", tags=["payment"])


@payment_router.post("/invoice")
async def invoice(payment, service: PaymentUseCase = Depends()):
    return await service.receive_payment(payment=payment)


@payment_router.get("/test")
async def test(service: InvoiceUseCase = Depends()):
    return await service.send_invoices()
