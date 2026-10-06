from pydantic import BaseModel, ConfigDict, EmailStr, Field
from app.enums.enums import UserRoles

class AuthLogin(BaseModel):

    model_config = ConfigDict(
        extra="forbid",
        str_strip_whitespace=True,
    )

    email: EmailStr

    password: str = Field(
        min_length=8,
        max_length=128,
    )
    
class TokenResponse(BaseModel):
    access_token: str
    token_type: str
    role: UserRoles