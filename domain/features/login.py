from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, SQLModel

from domain.core.crud import get_session

router = APIRouter(prefix="/login", tags=["Login"])

class UserPassword(SQLModel):
    username: str
    password: str
    
@router.post("/login")
async def login(form_data: UserPassword, session: Session = Depends(get_session)):
    check_password(form_data)
    raise HTTPException(status_code=500, detail="Not implemented yet.")

def check_password(password: str):
    hashed_value = calculate_hash(password)
    token = ""
    
    if validate_password(password, hashed_value):
        return token
    
    raise HTTPException(status_code=403, detail="Username or password not valid")

def calculate_hash(password: str):
    return password + "123"

def validate_password(password, hashed_value):
    if password == (hashed_value+"123"):
        return True
    return False