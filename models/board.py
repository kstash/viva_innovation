from datetime import datetime
from typing import Optional
from beanie import Document, PydanticObjectId

from models.user import User

class Board(Document):
    title: str
    content: str | None
    author_id: Optional[PydanticObjectId] = None
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
    
    class Settings:
        name = "board"

    class Config:
        json_schema_extra = {
            "example": {
                "title": "sample title",
                "content": "sample content",
                "author_id": "sample id",
                "created_at": "2022-01-01T00:00:00",
                "updated_at": "2022-01-01T00:00:00",
            }
        }