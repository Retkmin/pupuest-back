import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


class Asset(SQLModel, table=True):
    __tablename__ = "Assets"
    
    id_asset: Optional[int] = Field(primary_key=True)
    asset_name: str = Field(
        nullable=False,
        description='',
    )
    symbol: str = Field(
        nullable=False,
        description='',
    )
    description: str = Field(
        nullable=False,
        description='',
    )
    values: str = Field(
        nullable=False,
        description='',
    )
    created_at: datetime.datetime = Field(
        nullable=False, default=datetime.datetime.now()
    )
    updated_at: datetime.datetime = Field(
        nullable=False, default=datetime.datetime.now()
    )
    
