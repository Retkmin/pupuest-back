from typing import Literal

from fastapi import APIRouter, HTTPException, status

router = APIRouter(prefix="/login", tags=["Login"])

@router.post("/login")
async def login_for_access_token():
    
    raise HTTPException(
            status_code=status.HTTP_501_NOT_IMPLEMENTED,
            detail="Login secuizado todavia no implementado.",
            headers={"WWW-Authenticate": "Bearer"},
        )