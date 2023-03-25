import uuid
from sqlalchemy.sql import func
from src.infra.database.modelbase import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String, DateTime


class InvoiceModel(Base):
    __tablename__ = "invoice"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    password = Column(String(100), nullable=False)
    state = Column(String(50), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
