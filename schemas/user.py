from datetime import datetime
from beanie import PydanticObjectId
from fastapi.security import HTTPBasicCredentials
from pydantic import BaseModel, EmailStr


class UserModel(BaseModel):
    id: PydanticObjectId
    name: str
    email: EmailStr
    password: str
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

    class Collection:
        name = "user"

    class Config:
        json_schema_extra = {
            "example": {
                "id": "user id",
                "name": "John Doe",
                "email": "john@example.com",
                "password": "password123!@",
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


class UserSignUp(BaseModel):
    name: str
    email: EmailStr
    password: str

    class Config:
        json_schema_extra = {
            "example": {
                "name": "John Doe",
                "email": "john@example.com",
                "password": "password123!@",
            }
        }