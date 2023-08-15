from typing import Optional

from sqlmodel import Field, SQLModel


class Operation(SQLModel, table=True):
    id_user: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field()
    id_password: int = Field()
    is_active: bool = Field()
    is_staff: bool = Field(default=False)
    is_active: bool = Field(default=False)
    reset_token: str = Field()
    verification_token: str = Field()
    email: str = Field()