import uuid
from sqlalchemy.sql import func
from src.infra.database.modelbase import Base
from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID, JSONB


class InvoiceModel(Base):
    __tablename__ = "invoice"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    type = Column(String(20), nullable=False)
    state = Column(String(50), nullable=False)
    metadata = Column(JSONB, nullable=False)
    extradata = Column(JSONB, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
