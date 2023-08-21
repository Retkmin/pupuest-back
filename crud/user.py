from sqlalchemy.orm import Session

from models.user import User


def get_users_list(db: Session) -> list[User]:
    return db.query(User).all()
