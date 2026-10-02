class AppException(Exception):
    status_code = 500
    detail = "Application error"


class DuplicateSchoolApplicationError(AppException):
    status_code = 409
    detail = "A pending school application already exists for this email."


class SchoolApplicationNotFoundError(AppException):
    status_code = 404
    detail = "School application not found."


class InvalidSchoolApplicationStateError(AppException):
    status_code = 409
    detail = "School application is not in a valid state for approval."
    
class SchoolAlreadyExistsError(AppException):
    status_code = 409
    detail = "A school with this email already exists."