import datetime

from sqlmodel import Field, SQLModel


class PaymentMethod(SQLModel, table=True):
    __tablename__ = "Payment_Method"

    id_payment_method: int = Field(nullable=False, description="PK de la tabla.")
    id_user: int = Field(nullable=False)
    id_currency: int = Field(nullable=False)
    id_payment_status: int = Field(nullable=False)
    id_transaction: int = Field(nullable=False)
    id_invoice: int = Field(
        nullable=False,
        description="",
    )
    payment_amount: float = Field(
        nullable=False,
        description="Cantidad del pago realizado.",
    )
    payment_method: str = Field(
        nullable=False,
        description="El método utilizado para realizar el pago (tarjeta de crédito, PayPal, transferencia bancaria, etc.).",
    )
    des_payment_status: str = Field(
        nullable=False,
        description="Estado del pago en texto (Pendiente, Facturado, etc).",
    )
    billing_details: str = Field(
        nullable=False,
        description="Detalles de la factura asociada.",
    )
    payment_date: datetime.date = Field(
        nullable=False,
        default=datetime.date.today(),
        description="La fecha y hora en que se realizó la transacción.",
    )
    created_at: datetime.datetime = Field(
        nullable=False, default=datetime.datetime.now()
    )
    updated_at: datetime.datetime = Field(
        nullable=False, default=datetime.datetime.now()
    )
