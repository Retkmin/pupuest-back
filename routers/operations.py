from fastapi import APIRouter, HTTPException, status

from models.operation import Operation

router = APIRouter(prefix="/operations", tags=["Operation"])

@router.post("", response_model=Operation)
async def login_for_access_token():
    raise HTTPException(
            status_code=status.HTTP_501_NOT_IMPLEMENTED,
            detail="Saving an operation is not implemented yet.",
            headers={"WWW-Authenticate": "Bearer"},
        )