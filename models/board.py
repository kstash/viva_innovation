from datetime import datetime
from beanie import Document

from models.user import User

class Board(Document):
    title: str
    content: str | None
    author: User
    
    class Settings:
        name = "board"

    class Config:
        json_schema_extra = {
            "example": {
                "title": "sample title",
                "content": "sample content",
                "author": {
                    "name": "sample name",
                    "email": "sample@email.com",
                    "created_at": "2022-01-01T00:00:00",
                    "updated_at": "2022-01-01T00:00:00",
                },
                "created_at": "2022-01-01T00:00:00",
                "updated_at": "2022-01-01T00:00:00",
            }
        }