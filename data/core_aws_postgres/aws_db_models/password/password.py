import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


class Password(SQLModel, table=True):
    
    __tablename__="Passwords"
    
    id_password: Optional[int] = Field(primary_key=True, default=None)
    id_user: Optional[int] = Field(nullable=False, foreign_key="Users.id_user")
    password_temp: int = Field()
    password_hash: str = Field()
    salt: str = Field()
    creation_date: datetime.datetime = Field()
    created_at: datetime.datetime = Field(
        nullable=False, default=datetime.datetime.now()
    )
    updated_at: datetime.datetime = Field(
        nullable=False, default=datetime.datetime.now()
    )