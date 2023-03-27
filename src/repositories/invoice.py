from fastapi import Depends
from sqlalchemy.orm import Session
from src.models.invoice import InvoiceModel
from src.infra.database.connection import db_connection


class InvoiceRepository:
    def __init__(self, db: Session = Depends(db_connection)) -> None:
        self.db = db

    def add(self, invoice: InvoiceModel) -> InvoiceModel:
        self.db.add(invoice)
        self.db.commit()
        self.db.refresh(invoice)
        return invoice

    def filter(self, id) -> InvoiceModel:
        return (
            self.db.query(InvoiceModel)
            .filter(InvoiceModel.extradata["id"] == id)
            .first()
        )
