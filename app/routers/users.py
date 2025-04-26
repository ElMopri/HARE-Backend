from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User as UserModel
from app.schemas.user import User, UserCreate
from app.auth.auth_handler import get_password_hash
from app.dependencies.auth import get_current_user

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/", response_model=list[User])
def get_users(db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    return db.query(UserModel).all()

@router.post("/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    db_user = UserModel(
        email=user.email,
        full_name=user.full_name,
        hashed_password=get_password_hash(user.password),
        disabled=user.disabled or False
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user