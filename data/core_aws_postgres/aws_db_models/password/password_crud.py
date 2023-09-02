
import random
import string

from sqlmodel import Session

from data.core_aws_postgres.aws_db_models.password.password import Password
from data.core_aws_postgres.aws_db_models.user.user import User


def get_password_by_id(session: Session, id_password: int):
    return session.get(Password, id_password)

def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def reset_password(session: Session, user: User):
    password_exists = get_password_by_id(session, user.id_password)
    password_exists.password_hash = None
    session.add(password_exists)
    session.commit()
    session.refresh(password_exists)
    return True

def set_new_password(session: Session, user: User, hashed_password: str):
    password_exists = get_password_by_id(session, user.id_password)
    password_exists.password_hash = hashed_password
    session.add(password_exists)
    session.commit()
    session.refresh(password_exists)
    return True