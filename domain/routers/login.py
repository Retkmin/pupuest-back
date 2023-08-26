import os

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from data.db_models.token import Token

ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 0))

router = APIRouter(prefix="/login", tags=["Login"])


@router.post("", response_model=Token)
async def login_for_access_token(
    formData: OAuth2PasswordRequestForm = Depends(),
) -> dict[str, str]:
    print(formData.username, formData.password)
    """
    Login with user and password and return a token

    - **username**: The username
    - **password**: The password
    - **access_token**: The Token
    \f
    :param formData: Combination of username and password.
    """

    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Saving an operation is not implemented yet.",
        headers={"WWW-Authenticate": "Bearer"},
    )
