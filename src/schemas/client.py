from typing import List
from pydantic import BaseModel, EmailStr


class Address(BaseModel):
    cep: str
    logradouro: str
    complemento: str
    numero: int
    bairro: str
    cidade: str
    estado: str
    estadoSigla: str


class Client(BaseModel):
    nome: str
    mae: str
    pai: str
    site: str
    email: EmailStr
    senha: str
    rg: str
    cpf: str
    telefone: str
    celular: str
    dataNascimento: str
    endereco: Address
    usuario: str
    signo: str
    tipoSanguineo: str
    altura: str
    peso: int


class ClientSchema(BaseModel):
    type: str
    limit: int
    values: List[Client]
