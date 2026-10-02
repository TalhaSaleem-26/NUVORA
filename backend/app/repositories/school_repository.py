
from sqlmodel import Session ,select
from app.models.school import School

def check_school_by_email(session: Session , contact_email:str)->School | None:
    statement=select(School).where(School.email==contact_email)
    query=session.exec(statement).first()
    
    return query


def create_school(
    session: Session,
    new_school: School,
) -> School:

    session.add(new_school)

    return new_school