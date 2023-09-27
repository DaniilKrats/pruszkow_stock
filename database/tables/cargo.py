from sqlalchemy import Integer, String, Column, Float, ForeignKey, Date, Boolean, Table
from sqlalchemy.orm import relationship
from .base import BaseModel, Base  
from datetime import datetime

cargoes_dangerous_types = Table(
    "cargoes_dangerous_types",
    BaseModel.metadata,
    Column(
        "cargo_id", ForeignKey("cargoes.id", ondelete="CASCADE"),  primary_key=True,
    ),
    Column(
        "dangerous_type_id", ForeignKey("dangerous_types.id", ondelete="CASCADE"), primary_key=True
    ),
)

class Cargo(BaseModel):
    __tablename__ = "cargoes"
    
    name = Column(String(1024), nullable=True)
    comment = Column(String(1024), nullable=False)

    height = Column(Float, nullable=False)
    width = Column(Float, nullable=False)
    length = Column(Float, nullable=False)
    ldm = Column(Float, nullable=True)

    weight = Column(Float, nullable=True)

    arrival = Column(
        Date, default= datetime.now().date(), nullable=True
    )
    departure = Column(
        Date, default= datetime.now().date(), nullable=True
    )
    
    temperature_control = Column(Boolean, default=False, nullable=False)
    temperature_celsius = Column(Integer, nullable=True)

    auto_in_number = Column(String(200), nullable=True)
    auto_out_number = Column(String(200), nullable=True)

    client_id = Column(
        Integer, ForeignKey("clients.id", ondelete="CASCADE"), nullable=False
    )
    client = relationship(
        "Client",
        back_populates="cargoes",
        # lazy = 'immediate'
    )

    dangerous_types = relationship(
        "DangerousType",
        secondary=cargoes_dangerous_types,
        cascade="all,delete",
        # lazy = '
    )

    def __str__(self) -> str:  # pragma: no cover
        return f"{self.name}"


class DangerousType(BaseModel):
    __tablename__ = "cargoes"
    
    name = Column(String(1024), unique=True, nullable=False)
    coefficient = Column(Float, nullable=False)
    
    cargoes = relationship(
        "Cargo",
        secondary=cargoes_dangerous_types,
        cascade="all,delete",
    )