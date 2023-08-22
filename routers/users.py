from fastapi import APIRouter, Depends
from sqlmodel import Session

from crud import crud
from crud import user as crud_user
from models.user import User

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/create", response_model=User)
async def create_user(user: User, session: Session() = Depends(crud.get_session)):
    """
    Create an User with all the information:

    - **nombre**: El nombre
    - **apellidos**: Los apellidos del usuario
    - **username**: El username con el que iniciara sesion.
    - **rol**: El rol del usuario
    - **estado**: El estado del usuario.
    \f
    :param usuario_nuevo: User input.
    """
    return crud_user.create_user(session=session, new_user=user)
    
@router.get("/list", response_model=list[User])
async def get_users_list(session: Session() = Depends(crud.get_session)):
    return crud_user.get_users_list(session=session)