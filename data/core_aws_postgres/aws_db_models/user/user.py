import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    
    __tablename__ = "Users"
    
    id_user: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(nullable=False) 
    id_password: Optional[int] = Field(
        nullable=False,
        foreign_key="Passwords.id_password"
    )
    is_active: bool = Field(default=False, nullable=False)
    is_staff: bool = Field(default=False, nullable=False)
    is_admin: bool = Field(default=False, nullable=False)
    reset_token: str = Field(nullable=False)
    verification_token: str = Field(nullable=False)
    email: str = Field(nullable=False)
    created_at: datetime.datetime = Field()
    updated_at: datetime.datetime = Field()