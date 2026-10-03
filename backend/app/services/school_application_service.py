from sqlmodel import Session
from uuid import UUID

from app.models.school_application import SchoolApplication
from app.schemas.school_application import SchoolApplicationCreate
from app.repositories.school_application_repository import (
    create_school_application as create_school_application_repo,
    find_pending_by_email as pending_application ,
    get_school_applications as get_school_applications_repo , 
    get_application_by_id ,
    update_application
)
from app.enums.enums import SchoolApplicationStatus
from app.core.exceptions import DuplicateSchoolApplicationError,SchoolApplicationNotFoundError,InvalidSchoolApplicationStateError
from app.services.school import create_school_from_application

def create_school_application(
    session: Session,
    school_application: SchoolApplicationCreate,
) -> SchoolApplication:

    application=pending_application(session,school_application.contact_email)
    if (application):
        raise DuplicateSchoolApplicationError()
    
    
    new_application = SchoolApplication(
        school_name=school_application.school_name,
        contact_name=school_application.contact_name,
        contact_email=school_application.contact_email,
        contact_phone=school_application.contact_phone,
        expected_students=school_application.expected_students,
    )

    
    return create_school_application_repo(
        session,
        new_application,
    )
    

def  get_school_applications(session: Session)->list[SchoolApplication] :
    
    return get_school_applications_repo(session)



def school_application_approve(
    application_id: UUID,
    session: Session,
) -> SchoolApplication:

    application = get_application_by_id(
        application_id,
        session,
    )

    if not application:
        raise SchoolApplicationNotFoundError()

    if application.status != SchoolApplicationStatus.PENDING:
        raise InvalidSchoolApplicationStateError()

    new_school = create_school_from_application(
        session,
        application,
    )

    application.status = SchoolApplicationStatus.APPROVED

    update_application(
        session,
        application,
    )

    session.commit()
    session.refresh(application)

    return application


def school_application_reject(
    application_id: UUID,
    session: Session,
) -> SchoolApplication:

    application = get_application_by_id(
        application_id,
        session,
    )

    if not application:
        raise SchoolApplicationNotFoundError()

    if application.status != SchoolApplicationStatus.PENDING:
        raise InvalidSchoolApplicationStateError()

    application.status = SchoolApplicationStatus.REJECTED

    update_application(
        session,
        application,
    )

    session.commit()
    session.refresh(application)

    return application