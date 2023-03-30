import starkbank
from starkbank import Transfer
from src.models.invoice import InvoiceModel
from src.infra.starkbank.credential import project
from fastapi import Depends, status, HTTPException
from src.repositories.invoice import InvoiceRepository
from src.schemas.constant import (
    OutgoingType,
    IncomingType,
    Output,
    State,
    BankCode,
    AccountType,
    StarkBankAccount,
)


class PaymentUseCase:
    def __init__(
        self,
        repository: InvoiceRepository = Depends(),
    ) -> None:
        self.repository = repository

    async def generate_transfer(self, amount: int) -> Transfer:
        return Transfer(
            amount=amount,
            bank_code=BankCode.PIX,
            branch_code=StarkBankAccount.BRANCH_CODE,
            account_number=StarkBankAccount.ACCOUNT_NUMBER,
            account_type=AccountType.PAYMENT,
            tax_id=StarkBankAccount.TAX_ID,
            name=StarkBankAccount.NAME,
        )

    async def save_transfer(self, transfer, invoice_id) -> None:
        self.repository.add(
            invoice=InvoiceModel(
                type=OutgoingType.TRANSFER,
                state=State.SENT,
                correlation_id=invoice_id,
                extradata=transfer,
            )
        )

    async def save_payment(self, payment, invoice_id):
        self.repository.add(
            invoice=InvoiceModel(
                type=IncomingType.PAYMENT,
                state=payment.status,
                correlation_id=invoice_id,
                extradata=payment,
            )
        )

    async def receive_payment(self, payment):
        invoice = self.repository.filter(id=payment.id)
        if not invoice:
            raise HTTPException(
                detail="No invoice found", status_code=status.HTTP_404_NOT_FOUND
            )

        await self.save_payment(payment=payment, invoice_id=invoice.id)

        if payment.status == State.PAID:
            transfer = await self.generate_transfer(amount=payment.amount)
            starkbank.transfer.create(user=project, transfers=[transfer])
            await self.save_transfer(transfer=transfer, invoice_id=invoice.id)

        return Output(
            detail="Payment successfully registered",
            statusCode=status.HTTP_201_CREATED,
        )
