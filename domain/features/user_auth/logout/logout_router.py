from fastapi import APIRouter, Depends
from sqlmodel import Session

from data.core_aws_postgres.aws_database_config import get_session

router = APIRouter()

@router.delete("/logout", response_model=bool)
async def logout(
    session: Session = Depends(get_session)
):
    return True