from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.user import User
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

def create_user():
    db: Session = SessionLocal()

    new_user = User(
        email="admin@example.com",
        full_name="Admin Test",
        hashed_password=get_password_hash("1234"),
        disabled=False
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    print(f"Usuario creado: {new_user.email}")

if __name__ == "__main__":
    create_user()
