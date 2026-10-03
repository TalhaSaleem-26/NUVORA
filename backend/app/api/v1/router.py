from fastapi import APIRouter

from app.api.v1.auth.router import auth_router
from app.api.v1.school_applications.router import application_router
from app.api.v1.users.router import user_router


router = APIRouter()

router.include_router(
    auth_router,
    prefix="/auth",
)

router.include_router(
    application_router,
    prefix="/school-applications",
)

router.include_router(
    user_router,
    prefix="/users",
)