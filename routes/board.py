from fastapi import APIRouter
from passlib.context import CryptContext

from models.board import Board


board = APIRouter(prefix='/board')

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# pagination으로 게시글 가져오기
@board.get('/', response_description='Get boards')
async def get_boards(data):
    await Board.find_many()