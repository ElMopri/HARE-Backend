from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import user as user_model
from app.schemas import user as user_schema, token as token_schema
from app.auth.auth_handler import verify_password, create_access_token
from app.dependencies.auth import get_current_user, get_db

router = APIRouter()

def authenticate_user(db: Session, email: str, password: str):
    user = db.query(user_model.User).filter(user_model.User.email == email).first()
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user

@router.post("/token", response_model=token_schema.Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/users/me", response_model=user_schema.User)
async def read_users_me(current_user: user_model.User = Depends(get_current_user)):
    return current_user