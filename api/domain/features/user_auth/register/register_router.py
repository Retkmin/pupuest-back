from fastapi import APIRouter, Depends
from sqlmodel import Session

from api.data.core_aws_postgres.aws_database_config import get_session
from api.data.core_aws_postgres.aws_db_models.user_info.user_info_crud import (
    check_email_async, check_username_async)
from api.domain.features.user_auth.register.register_functions import \
    create_user
from api.domain.features.user_auth.user_auth_functions import get_password_hash
from api.domain.features.user_auth.user_auth_schemas import RegisterUser

router = APIRouter()

@router.post("/register", response_model=bool)
async def login_for_access_token(
    register_data: RegisterUser,
    session: Session = Depends(get_session)
):
    return create_user(
        session,
        register_data,
        hashed_password=get_password_hash("1234")#generate_random_password())
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