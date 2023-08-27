from fastapi import HTTPException, status

from data.core_aws_postgres.aws_database_config import SessionLocal


# Dependency
def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

def verify_password(plain_password, usuario_db_hashed_password):
    if get_password_hash(plain_password) != usuario_db_hashed_password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario o contraseña incorrectos.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return True


def get_password_hash(plain_password: str):
    return plain_password
