

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from api.data.core_aws_postgres.aws_database_config import get_session
from api.data.core_aws_postgres.aws_db_models.password.password_crud import (
    reset_password, set_new_password)
from api.data.core_aws_postgres.aws_db_models.user.user_crud import \
    get_user_by_id
from api.data.core_aws_postgres.aws_db_models.user_info.user_info import \
    UserInfo
from api.data.core_aws_postgres.aws_db_models.user_info.user_info_crud import \
    get_user_info_by_username_or_email
from api.domain.features.user_auth.user_auth_functions import (
    get_current_user, get_password_hash)
from api.domain.features.user_auth.user_auth_schemas import ResetToken

router = APIRouter()

@router.post("/recovery", response_model=bool)
async def recovery_password(
    username: str | None,
    email: str | None,
    session: Session = Depends(get_session)
):
    user_info = get_user_info_by_username_or_email(session, username, email)
    user = get_user_by_id(session, user_info.id_user)
    
    reset_password(session=session, user=user)
    
    raise HTTPException(
        status_code=status.HTTP_202_ACCEPTED,
        detail="A mail with the reset link has been sent to your mail."
    )
    

@router.post("/reset_password", response_model=bool)
async def recover_password_with_token(
    reset_token: ResetToken,
    password_1: str,
    password_2: str,
    session: Session = Depends(get_session)
):
    user_info: UserInfo = get_current_user(token=reset_token.reset_token)
    if not user_info:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The user hasn't been found."
        )
    user = get_user_by_id(user_info.id_user)
    if password_1 == password_2:
        set_new_password(session, user, get_password_hash(password_1))
    
    return  HTTPException(
        status_code=status.HTTP_200_OK,
        detail="Password has been changed.",
        headers={"WWW-Authenticate": "Bearer"},
)