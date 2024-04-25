from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
import jwt
from config.db import Settings

from typing import Dict, Optional
from datetime import datetime, timezone, timedelta
from fastapi import HTTPException
from rest_framework import status

from models.user import User


secret_key = Settings().JWT_SECRET_KEY
algorithm = Settings().JWT_ALGORITHM
access_token_exp = Settings().JWT_ACCESS_TOKEN_EXP_HR
refresh_token_exp = Settings().JWT_REFRESH_TOKEN_EXP_HR



def sign_jwt(user_email: str) -> Dict[str, str]:
    access_payload = { 
                      "user_email": user_email, 
                      "exp": datetime.now(timezone.utc) + timedelta(hours=access_token_exp)
                    }
    refresh_payload = { 
                       "user_email": user_email, 
                       "exp": datetime.now(timezone.utc) + timedelta(hours=refresh_token_exp) 
                    }
    access_token = jwt.encode(access_payload, secret_key, algorithm)
    refresh_token = jwt.encode(refresh_payload, secret_key, algorithm)
    return { "access_token": access_token, "refresh_token": refresh_token }
    

def decode_jwt(token: str) -> dict:
    decoded_token = jwt.decode(token, secret_key, algorithms=[algorithm])
    return decoded_token


async def get_current_user(token: str = Depends(OAuth2PasswordBearer(tokenUrl="token"))):
    try:
        payload = decode_jwt(token)
        user_email: Optional[str] = payload.get("user_email")
        if user_email is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token",
            )
        user = await User.find_one(User.email == user_email)
        return user
    except jwt.PyJWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )