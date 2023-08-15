from fastapi import APIRouter, HTTPException, status

from models.operation import Operation

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/create", response_model=bool)
async def create_user():
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
    raise HTTPException(
            status_code=status.HTTP_501_NOT_IMPLEMENTED,
            detail="User creation is not implemented yet.",
            headers={"WWW-Authenticate": "Bearer"},
        )