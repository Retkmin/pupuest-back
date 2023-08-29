import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


class Password(SQLModel, table=True):
    
    __tablename__="Passwords"
    
    id_password: Optional[int] = Field(primary_key=True, default=None)
    id_user: Optional[int] = Field(nullable=False, foreign_key="Users.id_user")
    password_hash: str = Field(nullable=False)
    creation_date: datetime.datetime = Field(default=datetime.datetime.now())
    created_at: datetime.datetime = Field()
    updated_at: datetime.datetime = Field()