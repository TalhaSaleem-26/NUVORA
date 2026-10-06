from uuid import UUID

from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.core.dependencies import require_role
from app.db.session import get_session
from app.enums.enums import UserRoles
from app.schemas.school_application import (
    SchoolApplicationCreate,
    SchoolApplicationRead,
)
from app.services.school_application_service import (
    create_school_application,
    get_school_applications,
    school_application_approve,
    school_application_reject,
)


application_router = APIRouter()



@application_router.post(
    "",
    response_model=SchoolApplicationRead,
    status_code=201,
)
def create_school_application_route(
    school_application: SchoolApplicationCreate,
    session: Session = Depends(get_session),
) -> SchoolApplicationRead:

    return create_school_application(
        session,
        school_application,
    )



@application_router.get(
    "",
    response_model=list[SchoolApplicationRead],
    status_code=200,
    dependencies=[
        Depends(require_role(UserRoles.SUPER_ADMIN))
    ],
)
def get_school_applications_route(
    session: Session = Depends(get_session),
) -> list[SchoolApplicationRead]:

    return get_school_applications(session)



@application_router.post(
    "/{application_id}/approve",
    response_model=SchoolApplicationRead,
    status_code=200,
    dependencies=[
        Depends(require_role(UserRoles.SUPER_ADMIN))
    ],
)
def school_application_approve_route(
    application_id: UUID,
    session: Session = Depends(get_session),
) -> SchoolApplicationRead:

    return school_application_approve(
        application_id,
        session,
    )


@application_router.post(
    "/{application_id}/reject",
    response_model=SchoolApplicationRead,
    status_code=200,
    dependencies=[
        Depends(require_role(UserRoles.SUPER_ADMIN))
    ],
)
def school_application_reject_route(
    application_id: UUID,
    session: Session = Depends(get_session),
) -> SchoolApplicationRead:

    return school_application_reject(
        application_id,
        session,
    )