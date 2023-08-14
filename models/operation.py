from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


class Operation(SQLModel, table=True):
    operative_id: Optional[int] = Field(default=None, primary_key=True)
    strategy_id: int = Field(default=None)
    stop_lose_price: float = Field()
    max_value: float = Field()
    entry_price: float = Field()
    opening_datetime: datetime = Field()
    closing_datetime: datetime = Field()
    asset: str = Field()
    operation_type: str = Field()