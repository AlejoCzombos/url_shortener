import jwt
import datetime
import hmac
import base64
import json
import hashlib

from app.config import API_SECRET_KEY

def generate_token() -> str:
    payload = {
        "iss": "API_Emisora",  # Quién emite el token
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=3),
        "iat": datetime.datetime.utcnow(),  # Fecha de emisión
        "sub": "ComunicacionSegura"  # Identificador del token
    }
    
    token = jwt.encode(payload, API_SECRET_KEY, algorithm='HS256')
    
    return token

def generate_token_api(iss:str, secret:str) -> str:
    payload = {
        "iss": iss,  # Quién emite el token
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=3),
        "iat": datetime.datetime.utcnow(),  # Fecha de emisión
    }
    
    token = jwt.encode(payload, secret, algorithm='HS256')
    
    return token

def is_token_valid(token: str) -> bool:
    try:
        payload = jwt.decode(token, API_SECRET_KEY, algorithms=["HS256"])

        if payload.get("iss") != "Eme_Local":
            return False

        return True

    except jwt.ExpiredSignatureError:
        return False
    except jwt.InvalidTokenError:
        return False