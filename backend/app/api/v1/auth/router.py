from fastapi import APIRouter

auth_router=APIRouter()

@auth_router.get("/")
def auth_route_check():
    return {
        "Name":"Muhammad_Talha_Saleem "
    }