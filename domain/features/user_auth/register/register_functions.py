
from fastapi import HTTPException
from sqlmodel import Session

from data.core_aws_postgres.aws_db_models.language import get_language_by_id
from data.core_aws_postgres.aws_db_models.password.password import Password
from data.core_aws_postgres.aws_db_models.rol import get_rol_by_id
from data.core_aws_postgres.aws_db_models.user.user import User
from data.core_aws_postgres.aws_db_models.user_info.user_info import UserInfo
from data.core_aws_postgres.aws_db_models.user_info.user_info_crud import (
    get_user_info_by_username_or_email,
)
from domain.features.user_auth.user_auth_schemas import RegisterUser


def create_user(session: Session, register_data: RegisterUser, hashed_password: str):
    user_exists = get_user_info_by_username_or_email(
        session,
        register_data.username,
        register_data.email
    )
    if user_exists:
        raise HTTPException(status_code=405, detail="That username/email already used.")

    rol_exists = get_rol_by_id(session, id_rol=3)
    if not rol_exists:
        raise HTTPException(status_code=404, detail="Rol not found.")


    new_user = User(rol=rol_exists, id_password=0)
    new_password = Password(
        password_hash=hashed_password,
        user=new_user
    )
    existe_language = get_language_by_id(session, id_language=1)
    if not existe_language:
        raise HTTPException(status_code=404, detail="Language not found.")
    new_user_info = UserInfo(
        user=new_user,
        username=register_data.username,
        birthdate=register_data.birthdate,
        company_conditions=register_data.company_conditions,
        name=register_data.name,
        address="",
        city="",
        country="",
        data_protection_conditions=register_data.data_protection_conditions,
        date_of_birth=register_data.birthdate,
        email=register_data.email,
        first_name=register_data.name,
        gender="Male",
        language=existe_language,
        last_name=register_data.surname,
        legal_conditions=register_data.legal_conditions,
        phone_number=123456,
        postal_code=403,
        profile_picture="src/assets/img",
        id_subscription_status=1,
        des_subscription_status="hola",
    )
    
    session.add_all(instances=[new_password, new_user,new_user_info])
    session.flush()
    
    session.refresh(new_user)
    new_user.id_password=new_password.id_password
    session.add(new_password)
    
    session.commit()
    return True