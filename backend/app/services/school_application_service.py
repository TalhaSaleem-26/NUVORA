from sqlmodel import Session

from app.models.school_application import SchoolApplication
from app.schemas.school_application import SchoolApplicationCreate
from app.repositories.school_application_repository import (
    create_school_application as create_school_application_repo,
    find_pending_by_email as pending_application ,
    get_school_applications as get_school_applications_repo
)

from app.core.exceptions import DuplicateSchoolApplicationError

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