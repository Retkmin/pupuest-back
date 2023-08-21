import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


class Operation(SQLModel, table=True):
    
    __tablename__="Operations"
    
    operative_id: Optional[int] = Field(default=None, primary_key=True)
    strategy_id: int = Field(default=None,nullable=False)
    stop_lose_price: float = Field(nullable=False)
    max_value: float = Field(nullable=False)
    entry_price: float = Field(nullable=False)
    opening_datetime: datetime.datetime = Field(nullable=False)
    closing_datetime: datetime.datetime = Field(nullable=False)
    asset: str = Field(nullable=False)
    operation_type: str = Field(nullable=False)