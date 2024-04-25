from datetime import datetime
from typing import Optional
from beanie import Document, Link, PydanticObjectId
from pydantic import ConfigDict, Field

from schemas.user import UserOut


class Board(Document):
    title: str
    content: str | None
    author_id: Optional[PydanticObjectId] = None
    views: int = 0
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

    class Settings:
        name = "board"

    class Config(ConfigDict):
        json_schema_extra = {
            "example": {
                "title": "sample title",
                "content": "sample content",
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