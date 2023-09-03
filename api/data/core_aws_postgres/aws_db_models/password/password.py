import datetime
from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from api.data.core_aws_postgres.aws_db_models.user.user import User


class Password(SQLModel, table=True):
    
    __tablename__="Passwords"
    
    id_password: Optional[int] = Field(primary_key=True, default=None)
    id_user: int = Field(
        nullable=False,
        default=None,
        foreign_key="Users.id_user"
    )
    user: "User" = Relationship()
    password_hash: str = Field(nullable=False)
    creation_date: datetime.datetime = Field(default=datetime.datetime.now())
    created_at: datetime.datetime = Field(default=datetime.datetime.now())
    updated_at: datetime.datetime = Field(default=datetime.datetime.now())