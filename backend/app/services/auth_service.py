from sqlmodel import Session

from app.core.exceptions import AuthenticationError
from app.core.security import verify_password, create_access_token
from app.models.user import User, UserStatus
from app.repositories.user_repository import get_user_by_email
from app.schemas.auth import AuthLogin, TokenResponse


def user_login(
    user: AuthLogin,
    session: Session,
) -> TokenResponse:

    login_user = get_user_by_email(
        session,
        user.email,
    )

    if not login_user:
        raise AuthenticationError()

    if login_user.status != UserStatus.ACTIVE:
        raise AuthenticationError()

    if login_user.password_hash is None:
        raise AuthenticationError()

    is_password_valid = verify_password(
        user.password,
        login_user.password_hash,
    )

    if not is_password_valid:
        raise AuthenticationError()

    access_token = create_access_token(
        {
            "sub": str(login_user.id),
        }
    )
    return  TokenResponse(
    access_token=access_token,
    token_type="bearer",
    role=login_user.role,
)