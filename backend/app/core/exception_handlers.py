from fastapi import Request
from fastapi.responses import JSONResponse

from app.core.exceptions import DuplicateSchoolApplicationError


def duplicate_school_application_handler(
    request: Request,
    exc: DuplicateSchoolApplicationError,
) -> JSONResponse:

    return JSONResponse(
        status_code=409,
        content={
            "detail": "A pending school application already exists for this email."
        },
    )