import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


class Invoice(SQLModel, table=True):
    
    __tablename__ = "Invoices"
    
    id_invoice: Optional[int] = Field(primary_key=True)
    id_user: int = Field(
        nullable=False,
    )
    id_currency: int = Field(
        nullable=False,
    )
    num_invoice: int = Field(
        nullable=False,
        description="Número de la factura.",
    )
    des_invoice: str = Field(
        nullable=False,
        description="Descripción de la factura (0001, 0002, 6785)",
    )
    date_of_issue: datetime.date = Field(
        nullable=False,
        default=datetime.date.today(),
        description="Fecha de emisión de la factura."
    )
    date_of_due: datetime.date = Field(
        nullable=False,
        default=datetime.date.today(),
        description="Fecha de vencimiento de la factura."
    )
    total_amount: float = Field(
        nullable=False,
        description="Cantidad total de la factura.",
    )
    id_payment_status: int = Field(
        nullable=False,
        description="Id del estado del estado de pago (1, 2, 3, etc).",
    )
    des_payment_status: str = Field(
        nullable=False,
        description="El estado del pago (completado, pendiente, rechazado, etc.).",
    )
    created_at: datetime.datetime = Field(
        nullable=False,
        default=datetime.datetime.now()
    )
    updated_at: datetime.datetime = Field(
        nullable=False,
        default=datetime.datetime.now()
    )