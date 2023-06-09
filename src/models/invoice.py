import uuid
from sqlalchemy.sql import func
from src.infra.database.modelbase import Base
from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID, JSON


class InvoiceModel(Base):
    __tablename__ = "invoice"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    datatype = Column(String(20), nullable=False)
    state = Column(String(50), nullable=False)
    correlation_id = Column(UUID(as_uuid=True), nullable=True)
    extradata = Column(JSON, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
