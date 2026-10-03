from uuid import UUID
from typing import Annotated

import jwt
from jwt.exceptions import InvalidTokenError
from fastapi import Depends

from sqlmodel import Session

from app.core.exceptions import AuthenticationError
from app.core.security import oauth2_scheme
from app.db.session import get_session
from app.models.user import User
from app.repositories.user_repository import get_user_by_id
from app.core.config import settings


def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    session: Annotated[Session, Depends(get_session)],
) -> User:

    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM],
        )

        user_id = payload.get("sub")

        if user_id is None:
            raise AuthenticationError()

        user_id = UUID(user_id)

    except (InvalidTokenError, ValueError):
        raise AuthenticationError()

    user = get_user_by_id(
        session,
        user_id,
    )

    if user is None:
        raise AuthenticationError()

    return user