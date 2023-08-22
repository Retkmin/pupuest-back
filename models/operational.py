import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


class Operational(SQLModel, table=True):
    
    __tablename__="Operational"
    
    id_operation: Optional[int] = Field(default=None, primary_key=True)
    id_asset: int = Field(default=None,nullable=False)
    max_price: int
    operation_date: datetime.date
    stop_lose_operation: int
    id_operation_type: int
    operation_type: str
    id_result: int
    result: str
    created_at: datetime.datetime = Field(
        nullable=False, default=datetime.datetime.now()
    )
    updated_at: datetime.datetime = Field(
        nullable=False, default=datetime.datetime.now()
    )