import datetime

from sqlmodel import Field, SQLModel


class Password(SQLModel, table=True):
    
    __tablename__="Passwords"
    
    id_password: int
    id_user: int
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