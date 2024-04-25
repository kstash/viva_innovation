from pydantic_settings import BaseSettings
from motor.motor_asyncio import AsyncIOMotorClient
import models as models

from beanie import init_beanie
from typing import Optional

from models.board import Board
from models.user import User

class Settings(BaseSettings):
    # 데이터베이스
    DATABASE_URL: Optional[str] = None
    DATABASE_NAME: Optional[str] = None

    # JWT
    JWT_SECRET_KEY: str = "secretKey"
    JWT_ALGORITHM: str = "HS256"
    JWT_ACCESS_TOKEN_EXP_HR: int = 1
    JWT_REFRESH_TOKEN_EXP_HR: int = 24

    class Config:
        env_file = ".env.dev"
        from_attributes = True


async def init_db():
    client = AsyncIOMotorClient(Settings().DATABASE_URL)

    await init_beanie(
        database=client[Settings().DATABASE_NAME],
        document_models=[Board, User]
    )