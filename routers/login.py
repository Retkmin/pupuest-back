from fastapi import APIRouter, HTTPException, status

from models.token import Token

router = APIRouter(prefix="/login", tags=["Login"])

@router.post("", response_model=Token)
async def login_for_access_token():
    raise HTTPException(
            status_code=status.HTTP_501_NOT_IMPLEMENTED,
            detail="Login securizado todavia no implementado.",
            headers={"WWW-Authenticate": "Bearer"},
        )