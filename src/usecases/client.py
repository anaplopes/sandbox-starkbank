import json
from fastapi import Depends
from src.models.client import ClientModel
from src.schemas.client import Client, ClientSchema
from src.repositories.client import ClientRepository
from src.infra.geradorbrasileiro.client import GeradorBrasileiroClient
from src.infra.geradorbrasileiro.exceptions import (
    GeradorBrasileiroException,
    GeradorBrasileiroRequestException,
)


class ClientUseCase:
    def __init__(
        self,
        geradorbrasileiro_client: GeradorBrasileiroClient = Depends(),
        repository: ClientRepository = Depends(),
    ) -> None:
        self.geradorbrasileiro_client = geradorbrasileiro_client
        self.repository = repository

    async def generate_client(self) -> Client | None:
        try:
            send = self.geradorbrasileiro_client.get_person()
            data: ClientSchema = json.loads(send.response)
            return data.values
        except GeradorBrasileiroRequestException or GeradorBrasileiroException:
            return

    async def save_client(self, client: Client) -> None:
        record = self.repository.filter_by_cpf(cpf=client.cpf)
        if not record:
            self.repository.add(
                reseller=ClientModel(
                    name=client.nome,
                    cpf_cnpj=client.cpf,
                    phone=client.celular,
                    email=client.email,
                    cep=client.endereco.cep,
                    address=client.endereco.logradouro,
                    complement=client.endereco.complemento,
                    number=client.endereco.numero,
                    neighborhood=client.endereco.bairro,
                    city=client.endereco.cidade,
                    state=client.endereco.estadoSigla,
                )
            )

    async def get_client(self) -> Client:
        client: Client = self.generate_client()
        if not client:
            self.get_client()

        self.save_client(client)
        return client
