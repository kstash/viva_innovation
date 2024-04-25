from datetime import datetime
from beanie import Document
from pydantic import EmailStr, constr, validator

from validators.user import validate_password


class User(Document):
    name: str
    email: EmailStr
    password: constr(min_length=8)
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
    
    class Settings:
        name = "user"
    
    class Config:
        json_schema_extra = {
            "example": {
                "name": "John Doe",
                "email": "john@example.com",
                "password": "password123!@",
                "created_at": "2022-01-01T00:00:00",
                "updated_at": "2022-01-01T00:00:00",
            }
        }

    _validate_password = validator("password", allow_reuse=True)(validate_password)