import datetime

from sqlmodel import Field, SQLModel


class Strategy(SQLModel, table=True):
    
    __tablename__="Strategy"
    
    id_strategy: int
    id_asset: int
    strategy_name: str
    risk: int
    account_amount: int
    created_at: datetime.datetime = Field(
        nullable=False, default=datetime.datetime.now()
    )
    updated_at: datetime.datetime = Field(
        nullable=False, default=datetime.datetime.now()
    )