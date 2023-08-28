
from fastapi import HTTPException
from sqlmodel import Session, or_, select

from data.core_aws_postgres.aws_db_models.password.password import Password
from data.core_aws_postgres.aws_db_models.user.user import User


def get_user_by_username_or_email(
    session: Session,
    username: str | None,
    email: str | None
):
    if not username and not email:
        print("\n No values have been provided to check.")
        return None
    statement = select(User).where(or_(User.username == username, User.email == email))
    result = session.exec(statement=statement).first()
    return result

def get_users_list_test(session: Session):
    statement = select(User)
    results = session.exec(statement)
    users = results.all()
    print(users)
    return users

def check_username_async(session: Session, username: str):
    user_exists = get_user_by_username_or_email(session, username, None)
    if user_exists:
        return True
    return False

def check_email_async(session: Session, email: str):
    user_exists = get_user_by_username_or_email(session, None, email)
    if user_exists:
        return True
    return False

def create_user(session: Session, new_user: User, hashed_password: str):
    user_exists = get_user_by_username_or_email(
        session,
        new_user.username,
        new_user.email
    )
    if user_exists:
        raise HTTPException(status_code=405, detail="That username/email already used.")
    new_password = Password(
        password_hash=hashed_password,
        password_temp=1,
        salt="holi"
    )
    new_user = User(
        username=new_user.username,
        email=new_user.email,
        #birthdate=new_user.birthdate,
        #company_conditions=new_user.company_conditions,
        #name=new_user.name
    )
    try:
        a = session.add(new_password)
        print("\n", a, "\n")
        b = session.add(new_user)
        print("\n", b, "\n")
        session.commit()
        return True
    except Exception as e:
        session.rollback()
        raise e