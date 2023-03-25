from fastapi import Depends
from sqlalchemy.orm import Session
from src.models.client import ClientModel
from src.infra.database.connection import db_connection


class ClientRepository:
    def __init__(self, db: Session = Depends(db_connection)) -> None:
        self.db = db

    def add(self, client: ClientModel) -> ClientModel:
        self.db.add(client)
        self.db.commit()
        self.db.refresh(client)
        return client

    def filter_by_cpf(self, cpf: str) -> ClientModel:
        return self.db.query(ClientModel).filter_by(cpf=cpf).first()
