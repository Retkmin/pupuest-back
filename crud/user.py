from sqlalchemy.orm import Session

from models.user import User


def get_users_list(session: Session) -> list[User]:
    return session.query(User).all()

def create_user(session: Session, new_user: User):
    print("\n Antes de añadir \n")
    print(new_user)
    session.add(new_user)
    session.commit()
    #session.refresh(new_user)
    print("\n Despues de añadirlo\n")
    print(new_user)
    #session.close()
    return new_user
        