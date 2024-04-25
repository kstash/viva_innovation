from typing import List
from fastapi import APIRouter, Body, Depends
from passlib.context import CryptContext

from auth.jwt_handler import get_current_user
from models.board import Board
from models.user import User
from schemas.board import BoardOut
from rest_framework import status
from fastapi import HTTPException


board = APIRouter(prefix='/board')

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@board.post('/', response_description='Add a new board', response_model=BoardOut, tags=["board"])
async def create_board(board_data: Board, current_user: User = Depends(get_current_user)):
    board_data.author_id = current_user.id
    new_board = await Board.create(board_data)

    return new_board


# pagination으로 게시글 가져오기
# >>> 따로 이야기는 없었으나 일반적으로 리스트를 전부 가져오는 경우는 없다고 생각하므로 추가함
@board.get('/', response_description='Get boards', response_model=List[BoardOut], tags=["board"])
async def get_boards(skip: int = 0, limit: int = 10):
    boards = await Board.find().skip(skip).limit(limit).to_list()
        
    return boards


@board.get('/{board_id}', response_description='Get a single board', response_model=BoardOut, tags=["board"])
async def get_board(board_id: str):
    board = await Board.get(board_id)
    
    # 조회수 1 증가
    board.views += 1
    board = await board.save()

    return board

@board.put('/{board_id}', response_description='Updated board', response_model=BoardOut, tags=["board"])
async def update_board(board_id: str, board_data: Board = Body(...), current_user: User = Depends(get_current_user)):
    board = await Board.get(board_id)
    # 게시글은 작성자만 수정 가능
    if board.author_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authorized")

    board.title = board_data.title
    board.content = board_data.content
    board = await board.save()

    return board

@board.delete('/{board_id}', response_description='Delete board', tags=["board"])
async def delete_board(board_id: str, current_user: User = Depends(get_current_user)):
    board = await Board.get(board_id)
    # 게시글은 작성자만 삭제 가능
    if board.author_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authorized")

    await board.delete()
    
    return { "message": "board deleted successfully" }