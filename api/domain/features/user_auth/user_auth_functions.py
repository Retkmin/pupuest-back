from typing import Annotated

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlmodel import Session

from api.data.core_aws_postgres.aws_db_models.user_info.user_info import UserInfo
from api.data.core_aws_postgres.aws_db_models.user_info.user_info_crud import (
    get_user_info_by_username_or_email,
)
from api.domain.exceptions import credentials_exception
from api.domain.features.user_auth.user_auth_schemas import TokenData

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = "dbac624a60bf912bd795dbb747fb93ef2329ebc479170150331eaecda016b1b3"  # TODO Run openssl rand -hex 32 to get the SECRET_KEY   # noqa: E501
ALGORITHM = "HS256"

def get_password_hash(password):
    print("Password set: ", password)
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    hashing_password = get_password_hash(plain_password)
    print("\nPlain password: ", plain_password,
          "\nHashed password: ", hashing_password,
          "\nDB password: ", hashed_password
    )
    return pwd_context.verify(plain_password, hashed_password)


def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], session: Session):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        print(payload)
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    
    user_info: UserInfo = get_user_info_by_username_or_email(
        session=session,
        username=token_data.username,
        email=token_data.username,
    )
    if user_info is None:
        raise credentials_exception
    return user_info