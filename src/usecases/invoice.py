import json
import random
import starkbank
from typing import List
from fastapi import Depends
from datetime import datetime, timedelta
from src.models.invoice import InvoiceModel
from src.schemas.constant import OutgoingType, State
from src.repositories.invoice import InvoiceRepository
from src.schemas.client import ClientSchema, ClientEntity
from src.infra.geradorbrasileiro.client import GeradorBrasileiroClient
from src.infra.geradorbrasileiro.exceptions import (
    GeradorBrasileiroException,
    GeradorBrasileiroRequestException,
)
from src.schemas.invoice import InvoicesSchemaResp, InvoicesSchemaReq, InvoiceEntityReq


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

    async def generate_invoice(self, client: ClientEntity) -> InvoicesSchemaReq:
        return InvoicesSchemaReq(
            invoices=InvoiceEntityReq(
                amount=random.randint(1, 1000),
                due=(datetime.now() + timedelta(days=20)),
                name=client.nome,
                taxId=client.cpf,
                tags=["scheduled"],
            )
        )

    async def send_invoices(
        self, invoices: List[InvoicesSchemaReq]
    ) -> InvoicesSchemaResp:
        return starkbank.invoice.create(invoices)

    async def save_invoices(self, invoices) -> None:
        for invoice in invoices:
            self.repository.add(
                invoice=InvoiceModel(
                    type=OutgoingType.INVOICE,
                    state=State.SENT,
                    metadata={},
                    extradata=invoice,
                )
            )

    async def task(self):
        invoices = []
        clients: ClientEntity = self.generate_client(quantity=8)
        for client in clients:
            invoices.append(self.generate_invoice(client=client))

        create_invoices = self.send_invoices(invoices=invoices)
        self.save_invoices(invoices=create_invoices)
