from pydantic import BaseModel, EmailStr, Field,field_validator
from typing import Annotated


class UserRegister(BaseModel):
    email: EmailStr
    password: Annotated[str, Field(min_length=8,max_length=100)]

    @field_validator("password")
    @classmethod
    def password_must_have(cls, value):
        if not any(letter.isalpha() for letter in value):
            raise ValueError("Password must contain at least one letter")
        return value
    
class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    email: str

    class Config:   
        from_attributes = True

