from fastapi import APIRouter, Depends

from sqlmodel import Session

from app.core.dependencies import get_current_user
from app.db.session import get_session
from app.models.user import User
from app.schemas.user import UserRead, UserInviteCreate
from app.services.user_service import create_user_invite


user_router = APIRouter()


@user_router.post(
    "/invite",
    response_model=UserRead,
    status_code=201,
)
def invite_user_route(
    user_data: UserInviteCreate,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session),
):
    return create_user_invite(
        session,
        user_data,
        current_user.school_id,
    )