from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from api.data.core_aws_postgres.aws_database_config import get_session
from api.data.core_aws_postgres.aws_db_models.user.user_crud import logout_user
from api.domain.features.user_auth.user_auth_functions import get_current_user
from api.domain.features.user_auth.user_auth_schemas import AccessToken

router = APIRouter()

@router.delete("/logout", response_model=bool)
async def logout(
    token: AccessToken,
    session: Session = Depends(get_session)
):
    print(token)
    user_info = get_current_user(token=token.access_token, session=session)
    if not user_info:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect token, couldn't logout in the DB.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    logout_result = logout_user(user_info.username, session)
    
    if logout_result:
        raise HTTPException(
            status_code=status.HTTP_202_ACCEPTED,
            detail="User token has been deleted"
    )
    raise HTTPException(
        status_code=status.HTTP_304_NOT_MODIFIED,
        detail="Coudln't delete the acces token in the DB."
    )