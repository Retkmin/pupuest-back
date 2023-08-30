
from sqlmodel import Session, or_, select

from data.core_aws_postgres.aws_db_models.user_info.user_info import UserInfo


def check_username_async(session: Session, username: str):
    user_exists = get_user_info_by_username_or_email(session, username, None)
    if user_exists:
        return True
    return False

def check_email_async(session: Session, email: str):
    user_exists = get_user_info_by_username_or_email(session,  None, email)
    if user_exists:
        return True
    return False

def get_user_info_by_username_or_email(
    session: Session,
    username: str | None,
    email: str | None
):
    if not username and not email:
        print("\n No values have been provided to check.")
        return None
    statement = select(UserInfo).where(
        or_(UserInfo.username == username, UserInfo.email == email)
    )
    result = session.exec(statement=statement).first()
    return result

def get_users_list_test(session: Session):
    statement = select(UserInfo)
    results = session.exec(statement)
    users = results.all()
    print(users)
    return users

