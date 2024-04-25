from typing import List
from fastapi import APIRouter, Body, HTTPException
from pydantic import EmailStr
from rest_framework import status
from passlib.context import CryptContext

from auth.jwt_handler import sign_jwt
from models.user import User
from schemas.user import UserLogin, UserOut, UserUpdate

user = APIRouter(prefix='/user')

pwd_context = CryptContext(schemes=["bcrypt"])


@user.get('/', response_description='Get all users', response_model=List[UserOut])
async def find_all_users() -> list:
    users = await User.all().to_list()
    return users


@user.post('/', response_description='Created user', response_model=UserOut)
async def create_user(user: User = Body(...)):
    user_exists = await User.find_one(User.email == user.email)
    if user_exists:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with this email already exists",
        )
    user.password = pwd_context.encrypt(user.password)
    
    new_user = await User.create(user)

    return new_user


@user.post('/login', response_description='Login user')
async def create_user(user: UserLogin = Body(...)):
    user_exists = await User.find_one(User.email == user.email)
    if user_exists:
        password = pwd_context.verify(user.password, user_exists.password)
        if password:
            return sign_jwt(user.email)
        
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect email or password",
    )


# TODO: 사용자 본인만 수정 가능하도록 추가
@user.put('/{user_email}', response_description='Updated user', response_model=UserOut)
async def update_user(user_email: EmailStr, user: UserUpdate):
    user_exists = await User.find_one(User.email == user_email)
    if user_exists:
        user_dict = user.model_dump()
        for field, value in user_dict.items():
            # 비밀번호는 해싱해서 저장
            if field == 'password':
                value = pwd_context.encrypt(value)
            setattr(user_exists, field, value)

        await user_exists.save()

        return user_exists
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User not found",
    )