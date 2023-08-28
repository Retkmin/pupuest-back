
from sqlmodel import Session

from data.core_aws_postgres.aws_db_models.password.password import Password


def get_password_by_id(session: Session, id_password: int):
    return session.get(Password, id_password)