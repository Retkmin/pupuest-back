from fastapi import APIRouter, Depends
from sqlmodel import Session

from crud import crud
from crud import user as crud_user
from db_models.user import User

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/create")
async def create_user(user: User, session: Session() = Depends(crud.get_session)):
    return crud_user.create_user(session=session, new_user=user)
    
@router.get("/list", response_model=list[User])
async def get_users_list(session: Session() = Depends(crud.get_session)):
    return crud_user.get_users_list(session=session)