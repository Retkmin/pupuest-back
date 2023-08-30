import datetime
from typing import Optional

from sqlmodel import Field, Session, SQLModel


class Rol(SQLModel, table=True):
    
    __tablename__ = "Roles"
    
    id_rol: Optional[int] = Field(primary_key=True, default=None)
    name_rol: str = Field(nullable=False)
    id_type_subscription: int = Field()
    des_type_subscription: str = Field(nullable=False)
    updated_at: datetime.date = Field()
    created_at: datetime.date = Field()
    
def get_rol_by_id(session: Session, id_rol: int):
    return session.get(Rol, id_rol)