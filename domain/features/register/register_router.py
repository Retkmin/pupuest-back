

import datetime

from fastapi import APIRouter, Depends
from sqlmodel import Session, SQLModel

from data.core_aws_postgres.aws_database_config import get_session
from data.core_aws_postgres.aws_db_models.password.password_crud import (
    generate_random_password,
)
from data.core_aws_postgres.aws_db_models.user.user_crud import (
    check_email_async,
    check_username_async,
    create_user,
)

router = APIRouter(prefix="/login", tags=["Login"])

ACCESS_TOKEN_EXPIRE_MINUTES = 30

class RegisterUser(SQLModel):
    username: str
    email: str
    surname: str
    name: str
    company_conditions: bool
    legal_conditions: bool
    data_protection_conditions: bool
    birthdate: datetime.date


@router.post("/register", response_model=bool)
async def login_for_access_token(
    register_data: RegisterUser,
    session: Session = Depends(get_session)
):
    return create_user(
        session,
        register_data,
        hashed_password=generate_random_password()
    )

@router.get("/check_username", response_model=bool)
async def check_username_endpoint(
    *,
    session: Session = Depends(get_session),
    username: str
):
    return check_username_async(session, username)

@router.get("/check_email", response_model=bool)
async def check_email_endpoint(
    *,
    session: Session = Depends(get_session),
    email: str
):
    return check_email_async(session, email)