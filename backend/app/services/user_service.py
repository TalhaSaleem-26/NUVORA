from sqlmodel import Session 
from app.models.user import User
from app.schemas.user import UserInviteCreate , SuperAdminCreate
from app.repositories.user_repository import get_user_by_email
from app.core.exceptions import UserAlreadyExistsError
from app.repositories.user_repository import create_user
from uuid import UUID
from app.enums.enums import UserStatus , UserRoles
from app.core.security import get_password_hash



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
    
def create_super_admin(
    super_user: SuperAdminCreate,
    session: Session,
) -> User:
    
    is_user_exists = get_user_by_email(
        session,
        super_user.email,
    )

    if is_user_exists:
        raise UserAlreadyExistsError()

    hashed_password = get_password_hash(
        super_user.password,
    )

    new_super_user = User(
        name=super_user.name,
        email=super_user.email,
        password_hash=hashed_password,
        role=UserRoles.SUPER_ADMIN,
        school_id=None,
        status=UserStatus.ACTIVE,
    )

    create_user(
        session,
        new_super_user,
    )
    
    session.commit()
    session.refresh(new_super_user)

    return new_super_user