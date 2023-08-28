
import random
import string

from sqlmodel import Session

from data.core_aws_postgres.aws_db_models.password.password import Password


def get_password_by_id(session: Session, id_password: int):
    return session.get(Password, id_password)

def generate_random_password(length=12):
    
    characters = string.ascii_letters + string.digits + string.punctuation
    print("\n Generating random password characters:", characters)
    
    password = ''.join(random.choice(characters) for _ in range(length))
    print("\n Temporary password created:", password, "\n")
    return password