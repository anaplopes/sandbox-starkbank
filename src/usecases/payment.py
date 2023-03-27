from src.models.invoice import InvoiceModel
from fastapi import Depends, status, HTTPException
from src.schemas.constant import IncomingType, Output
from src.repositories.invoice import InvoiceRepository
from src.infra.starkbank.client import StarkbankClient


class PaymentUseCase:
    def __init__(
        self,
        starkbank_client: StarkbankClient = Depends(),
        repository: InvoiceRepository = Depends(),
    ) -> None:
        self.starkbank_client = starkbank_client
        self.repository = repository

    async def save_payment(self, payment):
        invoice: InvoiceModel = self.repository.filter(id=payment.id)
        if not invoice:
            raise HTTPException(
                detail="No invoice found", status_code=status.HTTP_404_NOT_FOUND
            )

        data = self.repository.add(
            invoice=InvoiceModel(
                type=IncomingType.PAYMENT,
                state=payment.status,
                metadata={"correlation_id": invoice.id},
                extradata=payment,
            )
        )
        return Output(
            data=[{"id": data.id}],
            message="Payment successfully registered",
            statusCode=status.HTTP_201_CREATED,
        )
