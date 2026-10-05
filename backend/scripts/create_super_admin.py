from getpass import getpass

from sqlmodel import Session
from app.models.school import School
from app.models.user import User

from app.db.engine import engine
from app.schemas.user import SuperAdminCreate
from app.services.user_service import create_super_admin


def main():
    name = input("Super Admin name: ").strip()
    email = input("Super Admin email: ").strip()
    password = getpass("Super Admin password: ")

    super_admin_data = SuperAdminCreate(
        name=name,
        email=email,
        password=password,
    )

    with Session(engine) as session:
        try:
            user = create_super_admin(
                super_admin_data,
                session,
            )

            print(f"SUPER_ADMIN created successfully: {user.email}")

        except Exception as exc:
            session.rollback()
            print(f"Failed to create SUPER_ADMIN: {exc}")


if __name__ == "__main__":
    main()