import datetime
from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from data.core_aws_postgres.aws_db_models.language import Language
    from data.core_aws_postgres.aws_db_models.user.user import User


class UserInfo(SQLModel, table=True):
    
    __tablename__ = "Users_Info"

    id_users_info: Optional[int] = Field(primary_key=True)
    id_user: int = Field(foreign_key="Users.id_user")
    user: "User" = Relationship()
    id_language: int = Field(foreign_key="Languages.id_language")
    language: "Language" = Relationship()
    first_name: str = Field()
    last_name: str = Field()
    email: str = Field()
    username: str = Field()
    date_of_birth: datetime.date = Field()
    address: str = Field()
    phone_number: str = Field()
    gender: str = Field()
    country: str = Field()
    city: str = Field()
    postal_code: str = Field()
    profile_picture: str = Field()
    id_subscription_status: int = Field()
    company_conditions: Optional[bool] = Field(nullable=False, default=False)
    legal_conditions: Optional[bool] = Field(nullable=False, default=False)
    data_protection_conditions: Optional[bool] = Field(nullable=False, default=False)
    id_subscription_status: int = Field()
    des_subscription_status: str = Field()
    last_login: datetime.date = Field(default=datetime.date.today())
    registration_date: datetime.date = Field(default=datetime.date.today())
    is_verified: bool = Field(default=True)
    notes: str = Field(default="")