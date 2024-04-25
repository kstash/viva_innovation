from fastapi import APIRouter, Body, Depends
from passlib.context import CryptContext

from auth.jwt_handler import get_current_user
from models.board import Board
from models.user import User
from schemas.board import BoardCreate, BoardOut


board = APIRouter(prefix='/board')

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@board.post('/', response_description='Add a new board', response_model=BoardOut)
async def create_board(board_data: Board, current_user: User = Depends(get_current_user)):
    board_data.author_id = current_user.id
    new_board = await Board.create(board_data)

    return new_board


# pagination으로 게시글 가져오기
# >>> 따로 이야기는 없었으나 일반적으로 리스트를 전부 가져오는 경우는 없다고 생각하므로 추가함
@board.get('/', response_description='Get boards')
async def get_boards(skip: int = 0, limit: int = 10):
    boards = await Board.find().skip(skip).limit(limit).to_list()
    
    return boards