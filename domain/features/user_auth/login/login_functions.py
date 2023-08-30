from datetime import datetime, timedelta

from fastapi import Depends, HTTPException
from jose import jwt
from sqlmodel import Session

from data.core_aws_postgres.aws_database_config import get_session
from data.core_aws_postgres.aws_db_models.password.password_crud import (
    get_password_by_id,
)
from data.core_aws_postgres.aws_db_models.user.user import User
from data.core_aws_postgres.aws_db_models.user.user_crud import get_user_by_id
from data.core_aws_postgres.aws_db_models.user_info.user_info import UserInfo
from data.core_aws_postgres.aws_db_models.user_info.user_info_crud import (
    get_user_info_by_username_or_email,
)
from domain.features.user_auth.user_auth_functions import (
    ALGORITHM,
    SECRET_KEY,
    verify_password,
)


def authenticate_user(
    *,
    session: Session = Depends(get_session),
    email: str | None,
    username: str | None,
    password: str
):
    user_info: UserInfo = get_user_info_by_username_or_email(session, username, email)
    if not user_info:
        raise HTTPException(status_code=404, detail="Username not found")
    user: User = get_user_by_id(session, user_info.id_user)

    user_password = get_password_by_id(session, user.id_password)

    if not user_password:
        raise HTTPException(
            status_code=404, detail="Couldn't find user's password in DB."
        )
    if not verify_password(password, user_password.password_hash):
        return False
    return user_info


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    print("\n Login, printing encoded_jwt: ", encoded_jwt)
    return encoded_jwt
