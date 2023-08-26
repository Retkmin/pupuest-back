import datetime
from typing import Optional

from sqlmodel import Field, SQLModel

from models.language import Language
from models.user import User


class UserInfo(SQLModel, table=True):
    
    __tablename__ = "Users_Info"

    id_user_info: Optional[int] = Field(primary_key=True)
    id_user: int = Field(foreign_key=User.id_user)
    id_lenguaje: int = Field(foreign_key=Language.id_language)
    first_name: str = Field(nullable=False)
    last_name: str = Field(nullable=False)
    email: str = Field(nullable=False)
    username: str = Field(nullable=False)
    date_of_birth: datetime.date = Field(nullable=False)
    address: str = Field(nullable=False)
    phone_number: str = Field(nullable=False)
    gender: str = Field(nullable=False, default="Male")
    country: str = Field(nullable=False)
    city: str = Field(nullable=False)
    postal_code: str = Field(nullable=False)
    profile_picture: str = Field(nullable=False)
    id_subscription_status: int = Field(nullable=False)