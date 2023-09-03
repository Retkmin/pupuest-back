import datetime
from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from api.data.core_aws_postgres.aws_db_models.rol import Rol
class User(SQLModel, table=True):
    
    __tablename__ = "Users"
    
    id_user: Optional[int] = Field(default=None, primary_key=True)
    id_rol: int = Field(default=None, foreign_key="Roles.id_rol")
    rol: "Rol" = Relationship()
    id_password: int = Field(
        nullable=False,
        default=0,
    )
    is_register: bool = Field(default=0)
    is_active: bool = Field(default=False, nullable=False)
    is_staff: bool = Field(default=False, nullable=False)
    is_admin: bool = Field(default=False, nullable=False)
    refresh_token: Optional[str] = Field(nullable=True) 
    access_token: Optional[str] = Field(nullable=True) 
    created_at: datetime.datetime = Field(default=datetime.datetime.now())
    updated_at: datetime.datetime = Field(default=datetime.datetime.now())