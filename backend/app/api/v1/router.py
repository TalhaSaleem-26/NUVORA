from fastapi import APIRouter
from app.api.v1.auth.router import auth_router

router = APIRouter()

router.include_router(auth_router,prefix='/auth')


