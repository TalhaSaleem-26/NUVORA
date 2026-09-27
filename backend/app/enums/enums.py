from enum import Enum
class SchoolStatus(str, Enum):
    ACTIVE = "active"
    SUSPENDED = "suspended"
    
class SchoolApplicationStatus(str, Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
    
class UserRoles(str,Enum):
    SUPER_ADMIN="super_admin"
    SCHOOL_ADMIN = "school_admin"
    TEACHER = "teacher"
    ACCOUNTANT="accountant"
    PARENT="parent"
    STUDENT="student"
    
class UserStatus(str,Enum):
    INVITED="invited" 
    ACTIVE="active"
    SUSPENDED="suspended"
    