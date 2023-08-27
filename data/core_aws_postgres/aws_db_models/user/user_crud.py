from sqlmodel import Session

from data.core_aws_postgres.aws_db_models.user.user import User


def get_user_by_username(session: Session, username: str):
    return session.get(User, username)