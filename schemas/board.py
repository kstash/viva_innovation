from datetime import datetime
from beanie import PydanticObjectId
from pydantic import BaseModel, Field

from typing import Optional


class BoardOut(BaseModel):
    id: PydanticObjectId
    title: str = Field(max_length=100)
    # 이모지 작성 가능해야 함
    content: str 
    author_id: PydanticObjectId
    created_at: datetime
    updated_at: datetime = Field(default_factory=datetime.now)
    
    class Collection:
        name = "board"

    class Config:
        json_encodable = True
        json_schema_extra = {
            "example": {
                "title": "sample title",
                "content": "sample content",
                "author_id": "sample id",
                "created_at": "2022-01-01T00:00:00",
                "updated_at": "2022-01-01T00:00:00",
            }
        }


class BoardCreate(BaseModel):
    title: str = Field(max_length=100)
    content: str = Field(..., description="Content of the board, able to contain emojis")
    author_id: Optional[str] = Field(None, alias="ID of the author user")

    class Config:
        json_schema_extra = {
            "example": {
                "title": "sample title",
                "content": "sample content",
                "author_id": "user_id",
            }
        }
