from fastapi import FastAPI
from app.api.v1.router import router
from app.core.exceptions import DuplicateSchoolApplicationError
from app.core.exception_handlers import duplicate_school_application_handler

app = FastAPI()

app.include_router(
    router,
    prefix="/api/v1"
)

@app.get("/")
def read_root():
    return {"message": "Hello World"}