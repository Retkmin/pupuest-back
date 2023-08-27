
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from sqlmodel import Session, SQLModel

from domain.core.crud import get_session

router = APIRouter(prefix="/login", tags=["Login"])

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class Token(SQLModel):
    access_token: str
    token_type: str


class TokenData(SQLModel):
    username: str | None = None
    

@router.post("", description="API Endpoint to login as a user.",
    summary="Endpoint to login as a user."
)
async def login_for_access_token(
    formData: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_session)
) -> Token:
    return HTTPException(status_code=501)
