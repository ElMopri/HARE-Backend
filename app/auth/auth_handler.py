from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext
import jwt
from jwt import ExpiredSignatureError, InvalidTokenError

from app.schemas.token import TokenData

# Constantes de seguridad
SECRET_KEY = "6f37193a0abd5e61b8e2efb96c079d0c701bd34323a5c55e6c51c88db504bd40"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Contexto para hashing de contraseñas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def decode_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        # Retornar como objeto TokenData si lo deseas (opcional)
        return TokenData(email=payload.get("sub"))
    except ExpiredSignatureError:
        return None  # Token expirado
    except InvalidTokenError:
        return None  # Token inválido