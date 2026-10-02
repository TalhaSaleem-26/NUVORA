from fastapi import FastAPI
from app.api.v1.router import router
from app.core.exceptions import AppException 
from app.core.exception_handlers import app_exception_handler

app = FastAPI()

app.add_exception_handler(
    AppException,
    app_exception_handler,
)
app.include_router(
    router,
    prefix="/api/v1"
)

@app.get("/")
def read_root():
    return {"message": "Hello World"}