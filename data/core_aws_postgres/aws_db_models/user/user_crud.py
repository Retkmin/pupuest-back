
from sqlmodel import Session, select

from data.core_aws_postgres.aws_db_models.user.user import User


def get_user_by_username(session: Session, username: str):
    statement = select(User).where(User.username == username)
    result = session.exec(statement=statement).first()
    return result

def get_users_list_test(session: Session):
    statement = select(User)
    results = session.exec(statement)
    users = results.all()
    print(users)
    return users

def create_user(session: Session, new_user: User):
    session.add(new_user)
    session.refresh(new_user)
    return new_user