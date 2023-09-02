from sqlmodel import Session, select

from data.core_aws_postgres.aws_db_models.user.user import User
from data.core_aws_postgres.aws_db_models.user_info.user_info import UserInfo
from data.core_aws_postgres.aws_db_models.user_info.user_info_crud import (
    get_user_info_by_username_or_email,
)
from domain.features.user_auth.user_auth_schemas import LoginToken


def get_user_by_id(session: Session, id_user: int):
    return session.get(User, id_user)

def save_login_token(id_user: int, login_token: LoginToken, session: Session):
    user = get_user_by_id(session=session, id_user=id_user)
    user.access_token = login_token.access_token
    user.refresh_token = login_token.refresh_token
    try:
        session.add(user)
        session.commit()
        return True
    except:
        return False
        raise 
    
def logout_user(username: str, session: Session):
    user_info: UserInfo = get_user_info_by_username_or_email(
        username=username,
        email=username,
        session=session
    )
    statement = select(User).where(User.id_user==user_info.id_user)
    result = session.exec(statement)
    
    user = result.one()
    user.access_token = None
    user.refresh_token = None
    session.add(user)
    session.commit()
    session.refresh(user)
    return True
    