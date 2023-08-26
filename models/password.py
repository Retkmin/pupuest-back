import datetime
import uuid
from typing import Optional

from sqlmodel import Field, SQLModel


class Password(SQLModel, table=True):
    
    __tablename__="Passwords"
    
    id_password: Optional[uuid.UUID] = Field(primary_key=True, default=None)
    id_user: Optional[uuid.UUID] = Field(nullable=False, foreign_key="Users.id_user")
    password_temp: int
    password_hash: str
    salt: str
    creation_date: datetime.datetime
    created_at: datetime.datetime = Field(
        nullable=False, default=datetime.datetime.now()
    )
    updated_at: datetime.datetime = Field(
        nullable=False, default=datetime.datetime.now()
    )