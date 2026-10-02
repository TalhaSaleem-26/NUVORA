from sqlmodel import Session ,select
from app.models.school_application import SchoolApplication
from app.enums.enums import SchoolApplicationStatus
from uuid import UUID

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
    

def get_school_applications(session: Session)-> list[SchoolApplication] :
    
    statement=select(SchoolApplication)
    query=session.exec(statement).all()
    
    return query

def get_application_by_id(application_id: UUID,session: Session) -> SchoolApplication | None:

    statement = select(SchoolApplication).where(
        SchoolApplication.id == application_id
    )

    query = session.exec(statement).first()

    return query

def update_application(
    session: Session,
    application: SchoolApplication,
) -> SchoolApplication:

    session.add(application)


    return application
