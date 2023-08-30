from datetime import datetime, timedelta
from typing import Annotated

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
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
from domain.exceptions import credentials_exception
from domain.features.user_auth.user_auth_schemas import TokenData

ACCESS_TOKEN_EXPIRE_MINUTES = 30


def get_password_hash(password):
    return pwd_context.hash(password)


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = "dbac624a60bf912bd795dbb747fb93ef2329ebc479170150331eaecda016b1b3"  # TODO Run openssl rand -hex 32 to get the SECRET_KEY   # noqa: E501
ALGORITHM = "HS256"


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


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


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user_info_by_username_or_email(
        session=Depends(get_session),
        username=token_data.username,
        email=token_data.username,
    )
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)]
):
    if current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
