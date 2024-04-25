from datetime import datetime
from beanie import PydanticObjectId
from pydantic import BaseModel, EmailStr, constr, validator
from validators.user import validate_password


class UserOut(BaseModel):
    id: PydanticObjectId
    name: str
    email: EmailStr
    created_at: datetime
    updated_at: datetime | None

    class Collection:
        name = "user"

    class Config:
        json_schema_extra = {
            "example": {
                "id": "user id",
                "name": "John Doe",
                "email": "john@example.com",
                "created_at": "2022-01-01T00:00:00",
                "updated_at": "2022-01-01T00:00:00",
            }
        }


class UserLogin(BaseModel):
    email: EmailStr
    password: str

    class Config:
        json_schema_extra = {
            "example": {
                "email": "john@example.com",
                "password": "password123!@",
            }
        }


class UserUpdate(BaseModel):
    name: str
    password: constr(min_length=8)
    updated_at: datetime = datetime.now()

    class Config:
        json_schema_extra = {
            "example": {
                "name": "John Doe",
                "password": "password123!@",
            }
        }
    
    _validate_password = validator("password", allow_reuse=True)(validate_password)