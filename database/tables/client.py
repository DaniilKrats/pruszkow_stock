from sqlalchemy import Integer, String, Column, Float, ForeignKey, Date, Boolean, Table
from sqlalchemy.orm import relationship
from .base import BaseModel

senders_clients = Table(
    "cargoes_dangerous_types",
    BaseModel.metadata,
    Column(
        "sender_id", ForeignKey("senders.id", ondelete="CASCADE"),  primary_key=True,
    ),
    Column(
        "client_id", ForeignKey("clients.id", ondelete="CASCADE"), primary_key=True
    ),
)

recipients_clients = Table(
    "cargoes_dangerous_types",
    BaseModel.metadata,
    Column(
        "recipient_id", ForeignKey("recipients.id", ondelete="CASCADE"),  primary_key=True,
    ),
    Column(
        "client_id", ForeignKey("clients.id", ondelete="CASCADE"), primary_key=True
    ),
)

class Client(BaseModel):
    __tablename__ = "clients"
    
    name = Column(String(1024), unique=True, nullable=False)
    comment = Column(String(1024), nullable=True)
    unique_param = Column(String(100), unique=True, nullable=False)
    # debt = Column(Float, default=0.00, nullable=False)
    allowed = Column(Boolean, default=False, nullable=False)
    
    senders = Column(String(1024), nullable=False)
    recipient = Column(String(1024), nullable=False)

    country = Column(String(56), nullable=False)
    adress = Column(String(1024), nullable=False)
    
    cargoes = relationship(
        "Cargo",
        back_populates="clients",
        # lazy = 'immediate'
    )

    recipients = relationship(
        "Sender",
        secondary=senders_clients,
        cascade="all,delete",
    )

    recipients = relationship(
        "Recipient",
        secondary=recipients_clients,
        cascade="all,delete",
    )
    def __str__(self) -> str:  # pragma: no cover
        return f"{self.name}"


class Sender(BaseModel):
    __tablename__ = "senders"

    name = Column(String(1024), unique=True, nullable=False)
    comment = Column(String(1024), nullable=True)
    customs_address = Column(String(1024), nullable=True)
    adress = Column(String(1024), nullable=True)

    clients = relationship(
        "Client",
        secondary=senders_clients,
        cascade="all,delete",
    )

class Recipient(BaseModel):
    __tablename__ = "recipients"

    name = Column(String(1024), unique=True, nullable=False)
    comment = Column(String(1024), nullable=True)
    customs_address = Column(String(1024), nullable=True)
    adress = Column(String(1024), nullable=True)
    clients = relationship(
        "Client",
        secondary=recipients_clients,
        cascade="all,delete",
    )