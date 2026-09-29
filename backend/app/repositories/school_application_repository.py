from sqlmodel import Session ,select
from app.models.school_application import SchoolApplication
from app.enums.enums import SchoolApplicationStatus


def create_school_application(
    session: Session,
    new_application: SchoolApplication,
) -> SchoolApplication:

    session.add(new_application)
    session.commit()
    session.refresh(new_application)

    return new_application

def find_pending_by_email(session: Session,contact_email:str)->SchoolApplication | None:
    statement=select(SchoolApplication).where(SchoolApplication.contact_email==contact_email , SchoolApplication.status==SchoolApplicationStatus.PENDING)
    query=session.exec(statement).first()
    
    return query
    