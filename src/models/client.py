import uuid
from sqlalchemy.sql import func
from src.infra.database.modelbase import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String, DateTime, Integer


class ClientModel(Base):
    __tablename__ = "client"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(100), nullable=False)
    cpf_cnpj = Column(String(14), nullable=False, unique=True)
    phone = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    cep = Column(String(8), nullable=False)
    address = Column(String(200), nullable=False)
    complement = Column(String(50), nullable=False)
    mumber = Column(Integer, nullable=False)
    neighborhood = Column(String(100), nullable=False)
    city = Column(String(100), nullable=False)
    state = Column(String(2), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
