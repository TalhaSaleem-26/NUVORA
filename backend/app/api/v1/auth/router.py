from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.db.session import get_session
from app.schemas.auth import AuthLogin 
from app.services.auth_service import user_login as user_login_service
from app.schemas.auth import TokenResponse

auth_router = APIRouter()


@auth_router.post(
    "/login",
    response_model=TokenResponse,
    status_code=200,
)
def user_login_route(
    user: AuthLogin,
    session: Session = Depends(get_session),
):
    return user_login_service(user, session)