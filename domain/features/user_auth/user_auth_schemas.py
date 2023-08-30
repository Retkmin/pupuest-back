import datetime

from sqlmodel import SQLModel


class RegisterUser(SQLModel, table=False):
    username: str
    email: str
    surname: str
    name: str
    company_conditions: bool
    legal_conditions: bool
    data_protection_conditions: bool
    birthdate: datetime.date


class Token(SQLModel):
    access_token: str
    token_type: str


class TokenData(SQLModel):
    username: str | None = None
