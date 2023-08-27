import datetime
import uuid
from typing import Optional

from sqlmodel import Field, SQLModel

from data.core_aws_postgres.aws_db_models.password import Password


class User(SQLModel, table=True):
    
    __tablename__ = "Users"
    
    id_user: Optional[uuid.UUID] = Field(default=None, primary_key=True)
    username: str = Field(nullable=False) 
    id_password: Optional[uuid.UUID] = Field(
        nullable=False,
        foreign_key="Passwords.id_password"
    )
    password: Password()
    is_active: bool = Field(default=False, nullable=False)
    is_staff: bool = Field(default=False, nullable=False)
    is_admin: bool = Field(default=False, nullable=False)
    reset_token: str = Field(nullable=False)
    verification_token: str = Field(nullable=False)
    email: str = Field(nullable=False)
    created_at: datetime.datetime = Field(
        nullable=False,
        default=datetime.datetime.now()
    )
    updated_at: datetime.datetime = Field(
        nullable=False,
        default=datetime.datetime.now()
    )