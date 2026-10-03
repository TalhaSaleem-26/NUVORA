from sqlmodel import Session 
from app.models.user import User
from app.schemas.user import UserInviteCreate
from app.repositories.user_repository import get_user_by_email
from app.core.exceptions import UserAlreadyExistsError
from app.repositories.user_repository import create_user
from uuid import UUID
from app.enums.enums import UserStatus

def create_user_invite(
    session: Session,
    user_data: UserInviteCreate,
    school_id: UUID,
) -> User:

    is_user_exist = get_user_by_email(
        session,
        user_data.email,
    )

    if is_user_exist:
        raise UserAlreadyExistsError()

    new_user = User(
        name=user_data.name,
        email=user_data.email,
        role=user_data.role,
        school_id=school_id,
        status=UserStatus.INVITED,
    )

    return create_user(
        session,
        new_user,
    )