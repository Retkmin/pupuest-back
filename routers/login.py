from datetime import timedelta
from typing import Literal

from fastapi import APIRouter, Depends, HTTPException, status

router = APIRouter(prefix="/login", tags=["Login"])

@router.post("/login")
async def login_for_access_token(
    
    usuario:  Literal[False]):
    
    raise HTTPException(
            status_code=status.HTTP_501_NOT_IMPLEMENTED,
            detail="Login secuizado todavia no implementado.",
            headers={"WWW-Authenticate": "Bearer"},
        )