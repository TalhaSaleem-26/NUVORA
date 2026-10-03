from sqlmodel import Session, select

from app.models.user import User
from uuid import UUID

def get_user_by_email(
    session: Session,
    email: str,
) -> User | None:

    statement = select(User).where(
        User.email == email
    )

    query = session.exec(statement).first()

    return query


def create_user(
    session: Session,
    user: User,
) -> User:

    session.add(user)

    return user

def get_user_by_id(
    session: Session,
    user_id: UUID,
) -> User | None:

    statement = select(User).where(
        User.id == user_id
    )

    query = session.exec(statement).first()

    return query