import json
import random
from fastapi import Depends
from starkbank import Invoice
from datetime import date, timedelta
from src.models.invoice import InvoiceModel
from src.schemas.constant import OutgoingType, State, InvoiceTag
from src.repositories.invoice import InvoiceRepository
from src.schemas.client import ClientSchema, ClientEntity
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
            data: ClientSchema = json.loads(send.response)
            return data.values
        except GeradorBrasileiroRequestException or GeradorBrasileiroException:
            return

    async def generate_invoice(self, client: ClientEntity) -> Invoice:
        return Invoice(
            amount=random.randint(1, 1000),
            due=date.today() + timedelta(days=10),
            name=client.nome,
            taxId=client.cpf,
            tags=[InvoiceTag.SCHEDULED],
        )

    async def save_invoices(self, invoices: list) -> None:
        for invoice in invoices:
            self.repository.add(
                invoice=InvoiceModel(
                    type=OutgoingType.INVOICE,
                    state=State.SENT,
                    correlation_id=None,
                    extradata=invoice,
                )
            )

    async def task(self):
        # invoices = []
        clients: ClientEntity = self.generate_client(quantity=8)
        print(clients)
        # if clients:
        #     for client in clients:
        #         invoices.append(self.generate_invoice(client=client))

        #     create_invoices = self.send_invoices(invoices=invoices)
        #     self.save_invoices(invoices=create_invoices)
