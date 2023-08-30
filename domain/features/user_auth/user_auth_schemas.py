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
    token_type: str
class RefreshToken(Token):
    refresh_token: str
class AccessToken(Token):
    access_token: str

class LoginToken(Token):
    refresh_token: str
    access_token: str

class TokenData(SQLModel):
    username: str | None = None
