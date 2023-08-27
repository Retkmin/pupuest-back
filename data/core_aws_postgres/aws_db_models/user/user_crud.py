from sqlmodel import Session, select

from data.core_aws_postgres.aws_db_models.user.user import User


def get_user_by_username(session: Session, username: str):
    return session.get(User, username)

def get_users_list_test(session: Session):
    statement = select(User)
    results = session.exec(statement)
    users = results.all()
    print(users)
    return users