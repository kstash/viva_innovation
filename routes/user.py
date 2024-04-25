from fastapi import APIRouter, Body, HTTPException

from auth.jwt_handler import sign_jwt
from models.user import User
from schemas.user import UserLogin, UserSignUp
from rest_framework import status

from passlib.context import CryptContext


user = APIRouter(prefix='/user')

pwd_context = CryptContext(schemes=["bcrypt"])


@user.get('/', response_description='Get all users')
async def find_all_users() -> list:
    users = await User.all().to_list()
    return users


@user.post('/', response_description='Created user')
async def create_user(user: UserSignUp = Body(...)):
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
async def create_user(user_credentials: UserLogin = Body(...)):
    user_exists = await User.find_one(User.email == user_credentials.email)
    if user_exists:
        password = pwd_context.verify(user_credentials.password, user_exists.password)
        if password:
            return sign_jwt(user_credentials.email)
        
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect email or password",
    )

