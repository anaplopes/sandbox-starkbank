import json
import random
import starkbank
from typing import List
from fastapi import Depends
from starkbank import Invoice
from datetime import date, timedelta
from src.models.invoice import InvoiceModel
from src.infra.starkbank.credential import project
from src.repositories.invoice import InvoiceRepository
from src.schemas.client import ClientSchema, ClientEntity
from src.schemas.constant import OutgoingType, State, InvoiceTag
from src.infra.geradorbrasileiro.client import GeradorBrasileiroClient
from src.infra.geradorbrasileiro.exceptions import (
    GeradorBrasileiroException,
    GeradorBrasileiroRequestException,
)


class InvoiceUseCase:
    def __init__(
        self,
        geradorbrasileiro_client: GeradorBrasileiroClient = Depends(),
        repository: InvoiceRepository = Depends(),
    ) -> None:
        self.geradorbrasileiro_client = geradorbrasileiro_client
        self.repository = repository

    async def generate_client(self, quantity: int = 1) -> ClientEntity | None:
        try:
            send = self.geradorbrasileiro_client.get_person(limit=quantity)
            data = ClientSchema(**send.response)
            return data.values
        except GeradorBrasileiroRequestException or GeradorBrasileiroException:
            return

    async def generate_invoice(self, client: ClientEntity) -> Invoice:
        return Invoice(
            amount=random.randint(1, 500),
            due=date.today() + timedelta(days=10),
            name=client.nome,
            tax_id=client.cpf,
            fine=2,
            interest=1,
            tags=[InvoiceTag.SCHEDULED],
        )

    async def save_invoices(self, invoices: List[Invoice]) -> None:
        for invoice in invoices:
            self.repository.add(
                invoice=InvoiceModel(
                    datatype=OutgoingType.INVOICE,
                    state=State.SENT,
                    extradata=json.dumps(invoice, default=str),
                )
            )

    async def send_invoices(self) -> str:
        invoices = []
        clients = await self.generate_client(quantity=8)
        if clients:
            for client in clients:
                invoice = await self.generate_invoice(client=client)
                invoices.append(invoice)

            create_invoices = starkbank.invoice.create(user=project, invoices=invoices)
            await self.save_invoices(invoices=create_invoices)
            return "Invoices successfully registered"
        return "No client found"
