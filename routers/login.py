from fastapi import APIRouter, HTTPException, status

from models.token import Token

router = APIRouter(prefix="/login", tags=["Login"])

@router.post("", response_model=Token)
async def login_for_access_token():
    """
    Login with user and password and return a token

    - **username**: The username
    - **password**: The password
    - **access_token**: The Token
    \f
    :param usuario_nuevo: User input.
    """
    raise HTTPException(
            status_code=status.HTTP_501_NOT_IMPLEMENTED,
            detail="Login securizado todavia no implementado.",
            headers={"WWW-Authenticate": "Bearer"},
        )