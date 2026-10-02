from sqlmodel import Session

from app.models.school import School
from app.models.school_application import SchoolApplication
from app.core.exceptions import SchoolAlreadyExistsError

from app.repositories.school_repository import (
    create_school as create_school_repo,
  check_school_by_email as check_school_by_email_repo
)


def create_school_from_application(
    session: Session,
    application: SchoolApplication,
) -> School:

    is_school_exist=check_school_by_email_repo(session,application.contact_email)
    
    if (is_school_exist):
        raise  SchoolAlreadyExistsError()

    new_school = School(
        name=application.school_name,
        phone=application.contact_phone,
        email=application.contact_email,
    )

    return create_school_repo(
        session,
        new_school,
    )