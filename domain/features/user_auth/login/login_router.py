
from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session

from data.core_aws_postgres.aws_database_config import get_session
from data.core_aws_postgres.aws_db_models.user_info.user_info import UserInfo
from domain.features.user_auth.login.login_functions import (
    authenticate_user, create_access_token)
from domain.features.user_auth.user_auth_functions import get_current_user
from domain.features.user_auth.user_auth_schemas import (AccessToken,
                                                         LoginToken,
                                                         RefreshToken)

ACCESS_TOKEN_EXPIRE_MINUTES = 30
REFRESH_TOKEN_EXPIRE_HOURS = 12
router = APIRouter()

@router.post("/login", response_model=LoginToken)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    session: Session = Depends(get_session)
):
    user_info: UserInfo = authenticate_user(
        session=session,
        email=form_data.username,
        username=form_data.username,
        password=form_data.password
    )
    if not user_info:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    refresh_token_expires = timedelta(hours=REFRESH_TOKEN_EXPIRE_HOURS)
    access_token = create_access_token(
        data={"sub": user_info.username}, expires_delta=access_token_expires
    )
    refresh_token = create_access_token(
        data={"sub": user_info.username}, expires_delta=refresh_token_expires
    )
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }

@router.post("/refresh", response_model=AccessToken)
async def refresh_login_token(
    refresh_token: RefreshToken,
    session: Session = Depends(get_session)
):
    user_info: UserInfo = get_current_user(token=refresh_token.refresh_token, session=session)
    
    if not user_info:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user_info.username}, expires_delta=access_token_expires
    )
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }