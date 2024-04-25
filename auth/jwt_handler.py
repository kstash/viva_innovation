from config.db import Settings

from typing import Dict
import jwt
from datetime import datetime, timezone, timedelta


secret_key = Settings().JWT_SECRET_KEY
algorithm = Settings().JWT_ALGORITHM


def sign_jwt(user_id: str) -> Dict[str, str]:
    access_payload = { "user_id": user_id, "exp": datetime.now(timezone.utc) + timedelta(hours=1) }
    refresh_payload = { "user_id": user_id, "exp": datetime.now(timezone.utc) + timedelta(hours=24) }
    access_token = jwt.encode(access_payload, secret_key, algorithm)
    refresh_token = jwt.encode(refresh_payload, secret_key, algorithm)
    return { "access_token": access_token, "refresh_token": refresh_token }
    

def decode_jwt(token: str) -> dict:
    decoded_token = jwt.decode(token, secret_key, algorithms=[algorithm])
    return decoded_token