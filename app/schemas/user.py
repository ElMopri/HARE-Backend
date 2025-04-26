from pydantic import BaseModel

class UserBase(BaseModel):
    email: str
    full_name: str | None = None
    disabled: bool | None = None

class User(UserBase):
    pass

class UserInDB(UserBase):
    hashed_password: str

class UserCreate(UserBase):
    password: str