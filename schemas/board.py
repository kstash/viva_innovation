from datetime import datetime
from beanie import Link, PydanticObjectId
from pydantic import BaseModel, ConfigDict, Field

from schemas.user import UserOut


class BoardOut(BaseModel):
    id: PydanticObjectId
    title: str = Field(max_length=100)
    # 이모지 작성 가능해야 함
    content: str
    author_id: PydanticObjectId
    views: int
    created_at: datetime
    updated_at: datetime

    class Collection:
        name = "board"

    class Config(ConfigDict):        
        json_encodable = True
        json_schema_extra = {
            "example": {
                "title": "sample title",
                "content": "sample content",
                "views": 0,
                "author": {
                    "id": "sample id",
                    "name": "John Doe",
                    "email": "john@example.com",
                    "created_at": "2022-01-01T00:00:00",
                    "updated_at": "2022-01-01T00:00:00",
                },
                "created_at": "2022-01-01T00:00:00",
                "updated_at": "2022-01-01T00:00:00",
            }
        }