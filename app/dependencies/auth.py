from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.auth.auth_handler import decode_token
from app.models import user as user_model
from app.schemas.token import TokenData

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_user(db: Session, email: str):
    return db.query(user_model.User).filter(user_model.User.email == email).first()

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    token_data: TokenData = decode_token(token)
    if not token_data or not token_data.email:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    user = get_user(db, token_data.email)
    if not user or user.disabled:
        raise HTTPException(status_code=401, detail="Inactive or invalid user")

    return user