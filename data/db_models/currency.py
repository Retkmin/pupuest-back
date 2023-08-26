import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


class Currency(SQLModel, table=True):
    __tablename__ = "Currency"

    id_currency: Optional[int] = Field(primary_key=True)
    currency_code: str = Field(
        nullable=False,
        description="El código ISO o símbolo que representa la moneda (por ejemplo, USD para dólar estadounidense, EUR para euro, etc.).",
    )
    currency_name: str = Field(
        nullable=False,
        description='El nombre completo de la moneda (por ejemplo, "Dólar estadounidense", "Euro", etc.).',
    )
    exchange_rate: float = Field(
        nullable=False,
        description="La tasa de cambio actual de esta moneda en relación con una moneda base (puede ser útil para conversiones entre monedas).",
    )
    is_base: bool = Field(
        nullable=False,
        description="Un indicador booleano que indica si esta moneda es la moneda base utilizada en el sistema.",
    )
    country: str = Field(
        nullable=False,
        description="El país asociado a la moneda (no se si es relevante). ???",
    )
    decimal_places: float = Field(
        nullable=False,
        description="El número de decimales utilizados para representar esta moneda (por ejemplo, 2 para la mayoría de las monedas).",
    )
    total_amount: float = Field(
        nullable=False, description="Cantidad total de la factura."
    )
    symbol: str = Field(
        nullable=False,
        description='El símbolo utilizado para representar visualmente esta moneda (por ejemplo, "$" para dólar estadounidense, "€" para euro, etc.).',
    )
    created_at: datetime.datetime = Field(
        nullable=False, default=datetime.datetime.now()
    )
    updated_at: datetime.datetime = Field(
        nullable=False, default=datetime.datetime.now()
    )
